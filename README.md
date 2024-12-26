# Discord Chatbot
Developed a Discord chatbot that provides an interactive experience for users. The bot allows users to perform a variety of tasks, such as checking the weather, translating text, retrieving football match details, and managing personal tasks like a happiness journal. It uses Python to implement core functionalities, with discord.py for bot interactions. Additionally, the bot integrates with APIs to provide real-time data and offers a seamless user experience through thoughtful command designs.

# Setup Instructions (Required)
1. Python 3.8 or later
2. A Discord account and bot token
3. API keys for - WeatherAPI and Google Translate API

# Installation
1. **Clone the repository**

   git clone https://github.com/Rohpar1504/Discord-Chatbot.git

2. **Create a virtual environment**
   
   python3 -m venv venv

3. **Activate virtual environment**
   
   for MacOS: source venv/bin/activate

   for Windows: source venv\Scripts\activate

4. **Install required dependencies**
   
   pip install -r requirements.txt

5. **Add API key**
   
   Create a file named *api_key.txt* and add your respective API keys.

6. **Add Bot Token**

   Create a file named *bot_token.txt* and add your Discord bot token.

7. **Run the Discord Bot**

   python3 main.py

# Discord Bot Commands
| Command                               | Description                                                            |
|---------------------------------------|------------------------------------------------------------------------|
| `!hello`                              | Greets the user.                                                       |
| `!cat`                                | Sends a random cat video link.                                         |
| `!happy [item]`                       | Adds the item as a happy moment to the bot's list.                     |
| `!sad`                                | Sends a random happy moment to cheer up the user.                      |
| `!calc [x] [op] [y]`                  | Performs basic arithmetic operations.                                  |
| `!weather [location]`                 | Retrieves the current weather for a specified location.                |
| `!football_matches [location]`        | Fetches upcoming football matches for a specified location.            |
| `!translate [text] [source] [target]` | Translates text from one language to another.                          |

# Examples
1. **Greet the bot:** !hello
   
   **Response:** hello [Your Username]

2. **Fetch weather:** !weather Dubai

   **Response:** Weather in Dubai: 20°C, Clear Sky"

3. **Tranlate text:** !translate Hello en es

   **Response:** Hola

4. **Calculate sum of two numbers:** !calc 1 + 2

   **Response:** 3.0
