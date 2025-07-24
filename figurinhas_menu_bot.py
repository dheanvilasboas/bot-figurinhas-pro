
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio

TOKEN = "8384470504:AAE7au9gsdij5A4riVZiDFEBh5HDP0BH2Mc"  # Seu token real

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🌟 Grau 244 (Principal)", url="https://t.me/+bhl8ZK-lOiUwMDc5")],
        [InlineKeyboardButton("🌅 Bom Dia", url="https://t.me/+_Mzmw2KLYa8zYzgx")],
        [InlineKeyboardButton("🌙 Boa Tarde / Noite", url="https://t.me/+NyA42A9eDq0zZWYx")],
        [InlineKeyboardButton("💼 Empresários", url="https://t.me/+MA2LqHh6gKI1ZjFh")],
        [InlineKeyboardButton("👑 Mães / Mulheres", url="https://t.me/+l3sm4E8_Wx84ZjNh")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "**Escolha sua categoria de figurinhas abaixo 👇**",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("menu", menu))
    print("🤖 Bot de Figurinhas Pro rodando!")
    app.run_polling()

if __name__ == "__main__":
    main()
