import discord
from discord.ext import commands, tasks
from datetime import datetime 
import dotenv
import os
import asyncio
# from discord import app_commands

intents = discord.Intents.all()
intents.message_content = True

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")
CREATOR_ID = os.getenv("CREATOR_ID")
STUDENT_1 = os.getenv("STUDENT_1")
STUDENT_2 = os.getenv("STUDENT_2")
STUDENT_3 = os.getenv("STUDENT_3")

student_list = {STUDENT_1, STUDENT_2, STUDENT_3}

bot = commands.Bot(command_prefix="!", intents=intents)
last_reminder_time = None
practiced_members = set()
# slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    await bot.change_presence(status = discord.Status.online, activity = discord.Activity(type = discord.ActivityType.watching, name = f'{len(bot.guilds)} servers!'))
    print(f"Logged in as {bot.user.name} ({bot.user.id})")
    # check_practice.start()

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

async def check_permissions():
    for guild in bot.guilds:
        for member in guild.members:
            if member.id == bot.user.id:
                if member.guild_permissions.administrator:
                    check_practice.start()
                else:
                    await member.send("I require administrator permissions to work properly. Please make sure I have the necessary permissions.")
                    
@tasks.loop(hours=1)
async def check_practice():
    creator = bot.get_user(CREATOR_ID)
    current_time = datetime.datetime.now().strftime("%H:%M")

    global last_reminder_time

    if current_time == "19:27" and last_reminder_time != "19:27":
        last_reminder_time = "19:27"
        for guild in bot.guilds:
            for member in guild.members:
                if not member.bot:
                    try:
                        dm_channel = await member.create_dm()
                        message = await dm_channel.send("Have you practiced piano today? React with ✅ if you have.")

                        def check(reaction, user):
                            return user != bot.user and str(reaction.emoji) == "✅" and reaction.message.id == message.id

                        try:
                            reaction, user = await bot.wait_for("reaction_add", timeout=60*60, check=check)
                        except asyncio.TimeoutError:
                            await creator.send(f"{member.mention} has not practiced piano.")
                        else:
                            await creator.send(f"{member.mention} has practiced piano.")

                    except discord.Forbidden:
                        print(f"Could not send DM to {member.name} ({member.id})")

    elif current_time == "22:00" and last_reminder_time != "22:00":
        last_reminder_time = "22:00"
        for guild in bot.guilds:
            for member in guild.members:
                if not member.bot:
                    await creator.send(f"{member.mention} has not practiced piano.")

@check_practice.before_loop
async def before_check_practice():
    await bot.wait_until_ready()

# members = [member async for member in guild.fetch_members()]

@bot.command(name="send_msg_everyone")
@commands.has_permissions(administrator=True)
async def send_message_to_everyone(ctx):
    print("Executing send_message_to_everyone command...")
    creator = await bot.fetch_user(CREATOR_ID)
    for guild in bot.guilds:
        try:
            print(f"Processing guild: {guild.name} ({guild.id})")
            members = [member async for member in guild.fetch_members()]
            for member in members:
                if (
                    not member.bot
                    and member.id not in practiced_members
                    and member.id in student_list
                ):
                    try:
                        print(f"Processing member: {member.name} ({member.id})")
                        dm_channel = await member.create_dm()
                        message = await dm_channel.send("Have you practiced piano today? React with ✅ if you have, or 💤 to snooze for 2 hours, or 🚫 if you cannot practice piano today.")
                        
                        await message.add_reaction("✅")
                        await message.add_reaction("💤")
                        await message.add_reaction("🚫")
                        
                        asyncio.create_task(wait_for_reaction(message, member, creator))

                        # Add a delay between sending messages to members
                        await asyncio.sleep(1)

                    except discord.Forbidden:
                        print(f"Could not send DM to {member.name} ({member.id})")
        
        except Exception as e:
            print(f"An error occurred while processing guild: {guild.name} ({guild.id})")
            print(e)

    await ctx.send(f"Practice reminder sent to all piano students!", hidden=True)

async def wait_for_reaction(message, member, creator):
    try:
        def check(reaction, user):
            return (
                user != bot.user
                and str(reaction.emoji) in ["✅", "💤", "🚫"]
                and reaction.message.id == message.id
            )

        reaction, user = await bot.wait_for("reaction_add", timeout=5*60*60, check=check)
        
        if str(reaction.emoji) == "✅":
            practiced_members.add(member.id)
            await creator.send(f"{member.mention} has practiced piano.")
        elif str(reaction.emoji) == "💤":
            await asyncio.sleep(4*60*60)  # Snooze for 4 hours
            await creator.send(f"{member.mention} will practice piano later.")
        elif str(reaction.emoji) == "🚫":
            await message.edit(content="Please enter the reason why you cannot practice piano today (one line only).")
            
            def reason_check(msg):
                return msg.author == member and msg.channel == message.channel
            
            try:
                reason_msg = await bot.wait_for("message", timeout=60, check=reason_check)
                await creator.send(f"{member.mention} cannot practice piano today. Reason: {reason_msg.content}.")
                practiced_members.add(member.id)
            except asyncio.TimeoutError:
                await creator.send(f"{member.mention} did not provide a reason for not practicing piano.")
            
            # Edit the message to remove reactions
            await message.edit(content="You cannot practice piano today.")
            await message.clear_reactions()

    except asyncio.TimeoutError:
        current_time = datetime.now().strftime("%H:%M")
        if "22:00" <= current_time <= "06:00":
            practiced_members.add(member.id)
            await creator.send(f"{member.mention} has not practiced piano.")

@send_message_to_everyone.error
async def send_message_to_everyone_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have the necessary permissions to use this command.")


@bot.command(name="test")
async def test_command(ctx):
    creator = await bot.fetch_user(CREATOR_ID)
    await creator.send("Your command worked! I have been summoned!")

# "Have you practiced piano today? If you have, use ✅. If you need more time, use 💤 (If you react with this message, I will give you 2 hour extra before sending the same message again). If you don't reply in 3 hours from this message being sent, you will be logged as 'NOT PRACTICED!!!'"
# Have you practiced piano today? React with ✅ if you have. BTW, this is an automated message. If there is not response, you will be logged as 'Not practiced!'. To get more time, just react with 💤 for snooze and I will send the message 5 hours later.

bot.run(TOKEN)