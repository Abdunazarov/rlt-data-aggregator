import json

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from db_connector import DataAggregator
from initialize_db import initialize_db
from settings import BOT_TOKEN, REPLY_TEXT

aggregator = DataAggregator()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(REPLY_TEXT)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        input_data = json.loads(update.message.text)
        result = aggregator.aggregate_data(
            input_data["dt_from"], input_data["dt_upto"], input_data["group_type"]
        )
        response_message = json.dumps(result, ensure_ascii=False, indent=2)
        await update.message.reply_text(response_message)

    except json.decoder.JSONDecodeError:
        await update.message.reply_text("Данные должны быть в формате JSON")

    except Exception as e:
        print(f"Ошибка: {e}")


def main():
    initialize_db()
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )
    application.run_polling()


if __name__ == "__main__":
    main()
