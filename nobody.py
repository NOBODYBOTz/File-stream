import os
import pytz
import time, re
from datetime import datetime

var myEmoji = ["👍", "❤", "🔥", "🥰", "😁", "🎉", "🤩", "🕊", "🥱","😍", "🐳", "❤‍🔥", "🌭", "💯", "⚡", "😇", "🤝", "✍", "🤗", "🎅", "🎄", "☃", "💘", "🦄", "😘", "😎"]

var doEmoji = myEmoji[Math.floor(Math.random() * myEmoji.length)];

HTTP.post({
  url: "https://api.telegram.org/bot" + bot.token + "/setMessageReaction",
  body: {
    chat_id: request.chat.id,
    message_id: request.message_id,
    reaction: JSON.stringify([
      {
        type: "emoji",
        emoji: doEmoji,
        is_big: true 
      }
    ])
  }
});

def get_wish():
    tz = pytz.timezone('Asia/Colombo')
    time = datetime.now(tz)
    now = time.strftime("%H")
    if now < "12":
        status = "ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ 🌞"
    elif now < "18":
        status = "ɢᴏᴏᴅ ᴀꜰᴛᴇʀɴᴏᴏɴ 🌗"
    else:
        status = "ɢᴏᴏᴅ ᴇᴠᴇɴɪɴɢ 🌘"
    return status
