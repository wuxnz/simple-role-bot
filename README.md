# Discord Auto Role Bot

A simple Discord bot that automatically assigns a role when a user sends a message in a specific channel and removes a default role.

---

## Features
- Assigns a specified role when a user sends a message in a configured channel.
- Removes a default role upon assigning the new role.

---

## Configuration
The bot requires a `config.json` file with the following structure:

```json
{
  "botInfo": {
    "botToken": "YOUR_BOT_TOKEN",
    "serverId": "YOUR_SERVER_ID",
    "channelId": "YOUR_CHANNEL_ID",
    "roleToGiveId": "ROLE_ID_TO_GIVE",
    "roleToRemoveId": "ROLE_ID_TO_REMOVE"
  }
}
```

---

## Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/wuxnz/simple-role-bot.git
   cd simple-role-bot
   ```
2. Install dependencies:
   ```sh
   pip install discord.py
   ```
3. Add your bot token and other required details to `config.json`.
4. Run the bot:
   ```sh
   python main.py
   ```

---

## Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request.

---

## License
This project is open-source and available under the MIT License.

