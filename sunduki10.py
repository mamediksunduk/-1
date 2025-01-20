from vkbottle.bot import Bot, Message
from vkbottle import BotLabeler, GroupEventType, Keyboard, Text
import logging

logging.basicConfig(level=logging.INFO)

bot = Bot("YOUR_ACCESS_TOKEN")
labeler = BotLabeler()


CHAT_ID = -123456789 


@bot.on.event(GroupEventType.WALL_POST_NEW)
async def wall_post_new(event):
    post = event.object
    author_id = post.from_id  
    post_id = post.id         
    owner_id = post.owner_id 

   
    author_info = await bot.api.users.get(user_ids=author_id)
    author_name = f"{author_info[0].first_name} {author_info[0].last_name}"

    
    message = (
        f"Новый пост на стене сообщества!\n"
        f"Автор: {author_name} (ID: {author_id})\n"
        f"Пост: https://vk.com/wall{owner_id}_{post_id}"
    )

   
    await bot.api.messages.send(chat_id=CHAT_ID, message=message, random_id=0)


@bot.on.event(GroupEventType.WALL_REPLY_NEW)
async def wall_reply_new(event):
    reply = event.object
    post_id = reply.post_id
    owner_id = reply.owner_id
    author_id = reply.from_id

    
    author_info = await bot.api.users.get(user_ids=author_id)
    author_name = f"{author_info[0].first_name} {author_info[0].last_name}"

   
    message = (
        f"Новая запись из предложки!\n"
        f"Автор: {author_name} (ID: {author_id})\n"
        f"Пост: https://vk.com/wall{owner_id}_{post_id}"
    )

    
    await bot.api.messages.send(chat_id=CHAT_ID, message=message, random_id=0)

if __name__ == "__main__":
    bot.run_polling()
