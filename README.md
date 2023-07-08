# Piano Practice Reminder Discord Bot

The Piano Practice Reminder Discord Bot is a bot designed to help piano teachers ensure that their students are practicing piano regularly. Instead of manually sending reminders to each student, the bot automates the process by sending daily direct messages to the students, prompting them to confirm if they have practiced piano. The bot also notifies the teacher about the students' practice status.

## Features

- Automatic practice reminder messages sent to all students in the server via direct messages.
- Students can react with ✅ if they have practiced piano.
- Students can react with 💤 to snooze the reminder for 2 hours.
- Students can react with 🚫 if they cannot practice piano, and provide a reason.
- The bot notifies the creator when a student has practiced piano or provides a reason for not practicing.
- The bot handles different time ranges to mark students as "not practiced" if they haven't responded.
- Option to whitelist certain users who won't receive the practice reminder message.
- Easy-to-use commands to trigger the practice reminder and test the bot's functionality.

## Requirements

- Python 3.9 or higher
- discord.py library
- python-dotenv library

## Installation

1. Install the required Python packages using pip:

   ```shell
   pip install -r requirements.txt

2. Set up a bot account on the Discord Developer Portal and obtain the bot token.

3. Create a .env file in the project directory and add the following:

    ```shell
    TOKEN=YOUR_BOT_TOKEN
    Replace YOUR_BOT_TOKEN with your actual bot token.

    CREATOR_ID = YOUR_DISCORD_ID
    Replace YOUR_DISCORD_ID with your Discord ID

4. Invite the bot to your Discord server using the OAuth2 URL generated in the Developer Portal.

## Customization 

You can customize the bot's behavior by modifying the code in main.py. Some aspects you may consider customizing include:

- Modifying the time when the reminder messages are sent (send_message_to_everyone function).
- Changing the messages sent to students and the creator.
- Adjusting the reaction emojis and their corresponding actions (wait_for_reaction function).
- Updating the whitelist to include students who will receive the reminders.
- Please ensure you have the necessary permissions to run and modify the bot.

## Usage

- Use the command !send_msg_everyone to trigger the practice reminder messages to all students in the server.
- Students will receive a direct message asking if they have practiced piano. They can react with the respective emojis to indicate their practice status.
- The bot will notify the creator when a student has practiced piano or provides a reason for not practicing.
- Use the command !test to check if the bot is functioning correctly and receive a response from the bot.

## Contributions 

Contributions to the Piano Practice Reminder Discord Bot are welcome! If you have any ideas, improvements, or bug fixes, feel free to open an issue or submit a pull request.