from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler

# Room class to represent each room in the hotel
class Room:
    def __init__(self, room_id, room_type, description):
        self.id = room_id
        self.type = room_type
        self.description = description
        self.is_free = True
        self.dates = []

# Create an array or dictionary to store room objects
rooms = {
    "room1": Room("room1", "Single", "This is a single room."),
    "room2": Room("room2", "Double", "This is a double room."),
    # Add more rooms here
}

# Handler to handle /start command
def start(update: Update, context) -> None:
    # Display available room types
    room_types = list(rooms.keys())
    update.message.reply_text("Please choose a room type: " + ", ".join(room_types))

# Handler to handle user input after room type selection
def process_room_selection(update: Update, context) -> None:
    # Get the chosen room type
    room_type = update.message.text.strip()
    if room_type.startswith("/"):
        return
    if room_type in rooms:
        room = rooms[room_type]
        if room.is_free:
            update.message.reply_text("Room description: " + room.description)
            update.message.reply_text("Please provide the dates (start and end) for reservation.")
            # Implement logic to store the reservation dates
            # Update room.is_free and room.dates accordingly
        else:
            update.message.reply_text("This room is currently taken. It will be available on: " + ", ".join(room.dates))
    else:
        update.message.reply_text("Invalid room type. Please choose a valid room type.")

# Create the Telegram bot
bot_token = "6277072307:AAHk63pZ2zj-oGMkT9kTLtngaU9cnn2FTik"
bot = Bot(token=bot_token)
updater = Updater(bot=bot)

# Add handlers to the bot
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(MessageHandler(None, process_room_selection))

# Start the bot
updater.start_polling()