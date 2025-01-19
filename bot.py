import discord

# สร้าง client ของ Discord
client = discord.Client()

# เมื่อบอทออนไลน์
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    # ส่งข้อความไปยังช่องที่ต้องการ
    channel = client.get_channel(YOUR_CHANNEL_ID)  # ใช้ Channel ID ที่ต้องการ
    await channel.send('Hello from my bot!')

# ใช้ Token ของบอทในการเข้าสู่ระบบ
client.run('MTMzMDU4MTY3MjkwNjcyMzMzOA.GqmdT2.Uw_ne6H3BjG7urAPHsda64CLwtSKIbif6JhWjA')  # ใส่ Token ที่คุณได้จาก Discord Developer Portal
