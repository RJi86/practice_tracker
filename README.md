# Piano Practice Reminder Discord Bot

The Piano Practice Reminder Discord Bot is a bot designed to help piano teachers ensure that their students are practicing piano regularly. Instead of manually sending reminders to each student, the bot automates the process by sending daily direct messages to the students, prompting them to confirm if they have practiced piano. The bot also notifies the teacher about the students' practice status.

## Features

- Sends daily practice reminders via direct message to all students.
- Students can confirm their practice by reacting with a checkmark emoji.
- Teacher receives notifications when a student has practiced piano.
- Sends a reminder to the teacher if a student hasn't practiced by 10 PM.
- Customizable time for sending reminders.
- Customizable messages and reaction emojis.
- Whitelist feature to exclude specific users from receiving reminders.
- Easy-to-use commands for triggering reminders and testing the bot.

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