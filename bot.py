from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Replace 'YOUR_TELEGRAM_USER_ID' with your actual Telegram user ID
ADMIN_ID = 6881440290

# Function to delete messages with links
async def delete_links(update: Update, context):
    user_id = update.message.from_user.id
    if user_id != ADMIN_ID:  # If the user is not the admin
        if any(entity.type in ['url', 'text_link'] for entity in update.message.entities):
            await update.message.delete()  # Delete message if it contains a link

# Start command to check bot is working
async def start(update: Update, context):
    await update.message.reply_text('Bot is active and running!')

# Main function to run the bot
def main():
    # Replace 'YOUR_BOT_TOKEN' with your bot token from BotFather
    bot_token = '7599471712:AAHRORncxEGR9ZkTZaLuUlyUm-EfsS9n7H0'
    
    # Create Application instance
    application = Application.builder().token(bot_token).build()

    # Command handler to check bot's status
    application.add_handler(CommandHandler("start", start))

    # Message handler to delete messages with links (except admin)
    application.add_handler(MessageHandler(filters.Entity("url") | filters.Entity("text_link"), delete_links))

    # Start polling to handle updates
    application.run_polling()

if __name__ == '__main__':
    main()
