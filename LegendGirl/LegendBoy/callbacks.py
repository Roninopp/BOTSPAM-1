

@Client.on_callback_query()
async def _callbacks(Legend: Client, callback_query: CallbackQuery):
    user = await Legend.get_me()
    mention = user.mention
    query = callback_query.data.lower()
    if query.startswith("helpmenu1"):
        if query == "helpmenu1":
            chat_id = callback_query.from_user.id
            message_id = callback_query.message.id
            await Legend.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text="testing",
                reply_markup=InlineKeyboardMarkup(Data.HELP_MENU1),
            )
    elif query == "helpmenu2"
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.id
        await Legend.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="testing",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.HELP_MENU2),
        )
    elif query == "helpmenu3"
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.id
        await Legend.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="testing",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.HELP_MENU3),
        )
   
