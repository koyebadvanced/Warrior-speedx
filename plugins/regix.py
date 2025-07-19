from premium import is_premium
import asyncio
from pyrogram import Client
from plugins.utils import forward_message

# 👇 Chat & Message Range Settings — customize as needed
FROM_CHAT_ID = -1001234567890   # Source chat ID
TO_CHAT_ID = -1009876543210     # Destination chat ID
START_FROM = 1                  # Starting message ID
END_AT = 100                    # Ending message ID

async def restart_forwards(bot: Client):
    print("🔁 Starting message forwarding...")

    for msg_id in range(START_FROM, END_AT + 1):
        try:
            await forward_message(bot, FROM_CHAT_ID, TO_CHAT_ID, msg_id)
            await asyncio.sleep(0.5)  # Sleep to avoid rate limit
            print(f"✅ Forwarded message {msg_id}")
        except Exception as e:
            print(f"❌ Error at message {msg_id}: {e}")

    print("🎉 Forwarding Complete!")