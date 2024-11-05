import asyncio
import time

import pyrogram.errors
from pyrogram import Client

api_id = 10999414
api_hash = "c25eb4e3283f5fad6f0397e0463b4eef"
channel_id = -1001761095736
mes_id = "https://t.me/shalto_balto/742"
message = "тест"
from_chat = '@spamtext2'

# залупа
while True:
    async def main():

        async with Client("my_account", api_id, api_hash) as app:
            async for users in app.get_chat_join_requests(chat_id=channel_id):
                try:
                    print(users.user.first_name, users.user.last_name)
                    mes_count = await app.get_chat_history_count(users.user.id)
                    print(mes_count)
                    if mes_count == 0:
                        await app.send_voice(chat_id=users.user.id, voice=mes_id)
                        await asyncio.sleep(15)
                        await app.approve_chat_join_request(chat_id=channel_id, user_id=users.user.id)
                        print(f"{users.user.first_name}Принят в канал, сообщение отправлено ")
                        await asyncio.sleep(5)
                    else:
                        await asyncio.sleep(15)
                        await app.approve_chat_join_request(chat_id=channel_id, user_id=users.user.id)
                        print(f"{users.user.first_name}Принят в канал, диалог уже есть ")
                        await asyncio.sleep(5)
                except pyrogram.errors.UserChannelsTooMuch as ex:
                    print(ex)
                    continue
        # async for dialog in app.get_dialogs():
        #     print(dialog.chat.first_name or dialog.chat.title, dialog.chat.id)

        # async for dialog in app.get_chat_history(from_ch м at):
        #     print(dialog)

        # await app.copy_message(chat_id="shalto_balto", from_chat_id="from_chat", message_id=mes_id)


    asyncio.run(main())
    print("Курс приема окончен, ждем 1ч")
    time.sleep(3600)
