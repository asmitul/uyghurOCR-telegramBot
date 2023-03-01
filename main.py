# 6157615014:AAHXI_XulttiQWYmcSa0lYRiCRZRihsYcRY

from telegram import Chat, ChatMember, ChatMemberUpdated, Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    ChatMemberHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from PIL import Image

import pytesseract


async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Stores the photo and asks for a location."""
    user = update.message.from_user
    photo_file = await update.message.photo[-1].get_file()
    await photo_file.download_to_drive("test_ug.png")
    # await update.message.reply_text(
    #     "you send me a photo , and saved."
    # )

    # ukij
    await update.message.reply_text(pytesseract.image_to_string(
        Image.open('test_ug.png'), lang='ukij'))

    # uig
    # await update.message.reply_text(pytesseract.image_to_string(
    #     Image.open('test_ug.png'), lang='uig'))


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(
        "6157615014:AAHXI_XulttiQWYmcSa0lYRiCRZRihsYcRY").build()

    # Interpret any other command or text message as a start of a private chat.
    # This will record the user as being in a private chat with bot.
    # application.add_handler(MessageHandler(filters.ALL, start))

    application.add_handler(MessageHandler(filters.PHOTO, photo))

    # Run the bot until the user presses Ctrl-C
    # We pass 'allowed_updates' handle *all* updates including `chat_member` updates
    # To reset this, simply pass `allowed_updates=[]`
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
