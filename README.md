# Spambot

idk what is it with me and spamming but....... I just made a spam bot in case you haven't seen my [spam script](https://github.com/PrathamX595/spam-script) go ahead take a look, similar to that here is a discord spam bot which helps you to spam messages. Perfect for testing, pranks, or just having a bit of fun in your server.


## Features

- **Spam Command**: Allows users with the "Spammer" role to send a message multiple times.
- **Easy Setup**: Just a few steps to get the bot up and running.
- **Customizable Prefix**: Change the command prefix to suit your server's needs.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- `discord.py` library
- `python-dotenv` library

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/spambot.git
   cd spambot
   ```
2. **Install the required libraries**:
   ```sh
   pip install discord.py python-dotenv
   ```
3. **Set up .env**:
   
   make sure to add your discord bot token in the `.env` file take reference from the `.env.example` file
### Running the Bot
   ```sh
   python spamBot.py
   ```
### Usage
1.**Spam command**: `/spam <message>`
- Users with the "Spammer" role can use this command to send `<message>` 100 times in the channel.
### Example 
- Assign the "Spammer" role to a user (can ofcourse be changed).
- Use the following command in any discord channel:
  ```
  /spam Hello World
  ```
  The bot will send "Hello, World" 100 times in the channel.

 
  and that's it a fun and simple discord spam bot...... ৻(  •̀ ᗜ •́  ৻)
