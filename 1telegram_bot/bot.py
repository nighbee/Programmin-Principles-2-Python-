from aiogram import Bot, Dispatcher, executor, types
import re
import telegram
from sympy import *
from telegram.ext import Updater, CommandHandler, MessageHandler
# Function to perform basic math operations

def do_math(operation, num1, num2):
    if operation == 'add':
        return num1 + num2
    elif operation == 'sub':
        return num1 - num2
    elif operation == 'mul':
        return num1 * num2
    elif operation == 'div':
        return num1 / num2

# Function to handle /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the math bot! You can use /add, /sub, /mul, and /div to perform basic math operations.")

# Function to handle /add, /sub, /mul, and /div commands
def operation(update, context):
    operation = context.args[0]
    num1 = int(context.args[1])
    num2 = int(context.args[2])
    result = do_math(operation, num1, num2)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Result: {result}")

# Function to handle any other messages
def echo(update, context):
    text = update.message.text
    match = re.search("(\d+) (\S+) (\d+)", text)
    if match:
        num1 = int(match.group(1))
        operation = match.group(2)
        num2 = int(match.group(3))
        result = do_math(operation, num1, num2)
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Result: {result}")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="I am sorry, I am not able to understand your command. Please use /add, /sub, /mul, and /div to perform basic math operations.")

# Main function
def main():
    # Get the Telegram API token
    token = '5965750764:AAHcEVzjjcWDsipsPI-rmXEJIUtIbAGPuVM'
    # Create an Updater object
    updater = Updater(token, use_context=True)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("add", operation, pass_args=True))
    dp.add_handler(CommandHandler("sub", operation, pass_args=True))
    dp.add_handler(CommandHandler("mul", operation, pass_args=True))
    dp.add_handler(CommandHandler("div", operation, pass_args=True))
    # Register message handler
    dp.add_handler(MessageHandler(echo))
    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()