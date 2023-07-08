# Piano Practice Reminder Discord Bot

The Piano Practice Reminder Discord Bot is a bot designed to help piano teachers send practice reminders to their students. Instead of individually messaging each student, the bot automatically sends direct messages to all students at a specified time, asking if they have practiced piano. The students can then respond with various reactions to indicate their practice status.

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
- dotenv library (for loading environment variables, if used)

## Installation

1. Clone the repository or download the project files to your machine.

2. Install the required Python packages using pip:

   ```shell
   pip install -r requirements.txt
Set up a bot account on the Discord Developer Portal and obtain the bot token.

Create a .env file in the project directory and add the following:

plaintext
Copy code
DISCORD_TOKEN=YOUR_BOT_TOKEN
Replace YOUR_BOT_TOKEN with your actual bot token.

Invite the bot to your Discord server using the OAuth2 URL generated in the Developer Portal.

Customize the bot's behavior by modifying the code in main.py to fit your specific requirements, such as changing the time for reminders or adjusting the messages sent.

Start the bot by running the following command:

shell
Copy code
python main.py
Usage
Use the command !send_msg_everyone to trigger the practice reminder messages to all students in the server.

Students will receive a direct message asking if they have practiced piano. They can react with the respective emojis to indicate their practice status.

The bot will notify the creator when a student has practiced piano or provides a reason for not practicing.

Use the command !test to check if the bot is functioning correctly and receive a response from the bot.

Customization
You can customize the bot's behavior by modifying the code in main.py. Some aspects you may consider customizing include:

Modifying the time when the reminder messages are sent (send_message_to_everyone function).

Changing the messages sent to students and the creator.

Adjusting the reaction emojis and their corresponding actions (wait_for_reaction function).

Updating the whitelist or student list to include specific users who won't receive the reminders.

Please ensure you have the necessary permissions to run and modify the bot.

Contributions
Contributions to the Piano Practice Reminder Discord Bot are welcome! If you have any ideas, improvements, or bug fixes, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License.

Feel free to modify and adapt this README.md file to best suit your project's specific details and requirements.