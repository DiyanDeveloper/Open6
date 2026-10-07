# Open6 — The Definitive Open-Source Community Bot
<div align="center">
<img src="image_0.png" alt="Open6 Logo" width="250px" height="250px"/>


<p><strong>Like MEE6, but for everyone. Entirely open-source, forever free.</strong></p>
</div>
<div align="center">
License: AGPL v3

Python Version

Discord.py

OpenRouter

Issues

Stars
</div>
**Open6** is a powerful, all-in-one Discord bot built from the ground up to be a true open-source alternative to premium, closed-source community bots like MEE6. Designed for modern servers, Open6 combines essential community management tools, advanced engagement features, and robust utility—giving you complete control without hidden costs or feature gating.
Why pay for basic functionality when you can host it yourself, configure it to your needs, and contribute to its future?
## 🚀 Key Features
Open6 matches the heavy hitters feature-for-feature, completely for free.
### 🛡️ Advanced Moderation (Slash Commands)
Keep your community safe with robust, slash-command based moderation tools. Includes beautiful embed responses for clarity.
 * /kick: Kick members with reasons.
 * /ban: Permanently ban members with reasons.
 * /clear: Bulk delete messages from a channel (purge).
### 🌟 Leveling & Economy (MEE6-Style)
Drive engagement with a fully integrated XP and leveling system.
 * **Automatic XP:** Members gain XP just by chatting (rate-limited).
 * **Level Up:** Automatic notifications when members reach new levels with flashy embeds.
 * **Ranking:** Visual rank cards with /rank.
### 🤖 AI-Powered Integration (OpenRouter)
Leverage the power of modern LLMs directly in your server. Use OpenRouter to access numerous free or paid models.
 * /ask: Get intelligent answers to any question, seamlessly integrated into your chat.
### 🎮 Dynamic Utility & Fun
Modern features that make your server stand out.
 * **Slash Games:** Interactive, button-based mini-games like /rps (Rock, Paper, Scissors).
 * **Welcome System:** Automated, embed-based welcomes for new arrivals, including server member counts.
## 🛠️ Built With
Open6 is lightweight, efficient, and uses modern libraries.
 * **Python:** The core language for development.
 * **Discord.py:** The definitive Python API wrapper for Discord.
 * **OpenRouter SDK:** Efficient AI communication.
 * **Dotenv:** Secure configuration management.
## 💻 Installation & Setup
Running Open6 is straightforward for any server administrator or developer.
### Prerequisites
 1. Python 3.10+ installed.
 2. A Discord Bot Token with Message Content Intent enabled.
 3. (Optional) An OpenRouter API Key for the /ask feature.
### Step-by-Step Installation
 1. **Clone the Repository:**
   ```bash
   git clone https://github.com/DiyanDeveloper/Open6.git
   cd Open6
   
   ```
 2. **Install Dependencies:**
   ```bash
   pip install -r requirements.get
   
   ```
   *(A default requirements.txt might contain: discord.py, python-dotenv, openai)*
 3. **Configure Environment Variables:**
   Create a file named exactly .env in the root directory and paste your keys:
   ```env
   # Your Discord Bot Token (REQUIRED)
   DISCORD_TOKEN=your_discord_bot_token_here
   
   # Your OpenRouter API Key (Optional for AI features)
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   
   ```
 4. **Run the Bot:**
   ```bash
   python bot.py
   
   ```
Once the console displays Logged in as Open6 and synced slash commands!, your bot is live.
## 📖 Commands
All commands are implemented using modern **Slash Commands**.
| Command | Description | Example Usage | Permission Required |
|---|---|---|---|
| /ask | Ask the AI anything (OpenRouter). | /ask question:What is the AGPL? | Everyone |
| /ban | Ban a member. | /ban member:@user reason:Breaking rules | Ban Members |
| /clear | Clear messages in a channel. | /clear amount:10 | Manage Messages |
| /kick | Kick a member. | /kick member:@user reason:Disruptive | Kick Members |
| /rank | Check your level and XP. | /rank | Everyone |
| /rps | Play Rock, Paper, Scissors. | /rps | Everyone |
## 🤝 Contributing
We love our contributors! As an open-source project, Open6 is shaped by its community. Whether it's reporting bugs, suggesting features, or submitting code, every contribution is valuable.
 1. Fork the Project.
 2. Create your Feature Branch (git checkout -b feature/AmazingFeature).
 3. Commit your Changes (git commit -m 'Add some AmazingFeature').
 4. Push to the Branch (git push origin feature/AmazingFeature).
 5. Open a Pull Request.
## 📄 License
Open6 is distributed under the AGPL v3 License. See LICENSE for more information.
## 💬 Support & Community
 * Report Bugs/Feature Requests
 * Join our Community Discord Server
 * Email the developers
