import asyncio
from pyrogram import Client


api_id = 10999414
api_hash = "c25eb4e3283f5fad6f0397e0463b4eef"
channel_id = -1001761095736
mes_id = 357
message = "тест"
from_chat = '@spamtext2'
#залупа

async def main():
    async with Client("my_account", api_id, api_hash) as app:
        async for users in app.get_chat_join_requests(chat_id=channel_id):
            print(users.user.first_name, users.user.last_name)
            mes_count = await app.get_chat_history_count(users.user.id)
            print(mes_count)
            if mes_count == 0:
                await app.copy_message(users.user.id, message_id=mes_id, from_chat_id=from_chat)
                await asyncio.sleep(15)
                await app.approve_chat_join_request(chat_id=channel_id, user_id=users.user.id)
                print(f"{users.user.first_name}Принят в канал, сообщение отправлено ")
                await asyncio.sleep(5)
            else:
                await asyncio.sleep(15)
                await app.approve_chat_join_request(chat_id=channel_id, user_id=users.user.id)
                print(f"{users.user.first_name}Принят в канал, диалог уже есть ")
                await asyncio.sleep(5)
                
        # async for dialog in app.get_dialogs():
        #     print(dialog.chat.first_name or dialog.chat.title, dialog.chat.id)
        
        # async for dialog in app.get_chat_history(from_chat):
        #     print(dialog)

        # await app.copy_message(chat_id="shalto_balto", from_chat_id="from_chat", message_id=mes_id)


asyncio.run(main())
