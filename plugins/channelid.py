from pyrogram import filters
from pyrogram import Client
from pyrogram.file_id import FileId
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helper.utils import not_subscribed
from helper.ban import BanChek

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    await message.reply_text(
       text="**β οΈSorry bro,You didn't Joined Our Updates Channel Join now and start againπ**",
       reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton(text="π’πΉπππ πΌπ’ ππππππ π²πππππππ’", url=client.invitelink)
           ],[
           InlineKeyboardButton("π πππ’ π°ππππ π", url=f"https://t.me/{client.username}?start=start")            
           ]]
           )
       )

@Client.on_message(filters.private & filters.forwarded)
async def info(motech, msg):
    kikked = await BanChek(motech, msg)
    if kikked == 400:
        return 
    if msg.forward_from:
        text = "<u>ππ¨π«π°ππ«π ππ§ππ¨π«π¦ππ­π’π¨π§ π</u> \n\n"
        if msg.forward_from["is_bot"]:
            text += "<u>π€ ππ¨π­ ππ§ππ¨</u>"
        else:
            text += "<u>π€ππ¬ππ« ππ§ππ¨</u>"
        text += f'\n\nπ¨βπΌ πππ¦π : {msg.forward_from["first_name"]}'
        if msg.forward_from["username"]:

            text += f'\n\nπ ππ¬ππ«πππ¦π : @{msg.forward_from["username"]} \n\nπ ID : <code>{msg.forward_from["id"]}</code>\n\nπ«DC : {msg.forward_from["dc_id"]}'           
        else:
            text += f'\n\nπ ππ : `{msg.forward_from["id"]}`\n\n\n\nπ«DC : {msg.forward_from["dc_id"]}'

        await msg.reply(text, quote=True)
    else:
        hidden = msg.forward_sender_name
        if hidden:
            await msg.reply(
                f"βοΈππ«π«π¨π« <b><i>{hidden}</i></b> βοΈππ«π«π¨π«",
                quote=True,
            )
        else:
            text = f"<u>ππ¨π«π°ππ«π ππ§ππ¨π«π¦ππ­π’π¨π§ π</u>.\n\n"
            if msg.forward_from_chat["type"] == "channel":
                text += "<u>π’ ππ‘ππ§π§ππ₯</u>"
            if msg.forward_from_chat["type"] == "supergroup":
                text += "<u>π£οΈ ππ«π¨π?π©</u>"
            text += f'\n\nπ πππ¦π {msg.forward_from_chat["title"]}'
            if msg.forward_from_chat["username"]:

                text += f'\n\nβ‘οΈ ππ«π¨π¦ : @{msg.forward_from_chat["username"]}'
                text += f'\n\nπ ππ : `{msg.forward_from_chat["id"]}`\n\nπ«DC : {msg.forward_from_chat["dc_id"]}'
            else:
                text += f'\n\nπ ππ `{msg.forward_from_chat["id"]}`\n\n{msg.forward_from_chat["dc_id"]}'                                           

            await msg.reply(text, quote=True)









