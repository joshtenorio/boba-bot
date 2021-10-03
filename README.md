# boba-bot
Team Poggies' submission for Sunhacks 2021. Find our project page on Devpost [here](https://devpost.com/software/boba-bot).

## Build Instructions
1. Create a `auth.py` with a variable `botToken` that contains the bot token for your bot
### Windows
```bat
:: Create virtual environment
$ python -m venv venv

:: Start virtual environment
$ call venv/scripts/activate.bat

:: Install required packages
$ pip install -r requirements.txt

:: Run the bot
$ python main.py

:: Leave the virtual environment
$ deactivate
```

### Linux
```bash
# Create virtual environment
$ python3 -m venv venv

# Start virtual environment
$ source venv/bin/activate

# Install requried packages
$ pip install -r requirements.txt

# Run the bot
$ python3 main.py

# Leave the virtual environment
$ deactivate
```