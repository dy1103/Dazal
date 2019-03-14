import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print("-------------------")
    await client.change_presence(game=discord.Game(name='!명령어', type=1))
    
    
@client.event
async def on_message(message):
    if message.content.startswitch('!트위치'):
        await client.send_message(message.channel, "https://www.twitch.tv/dazal3635")

    if message.content.startswitch('!유튜브'):
        await client.send_message(message.channel, "https://www.youtube.com/channel/UCntJ_88iKtM0LE4dX5ovqFw?view_as=subscriber")

    if message.content.startswitch('!카페'):
        await client.send_message(message.channel, "https://cafe.naver.com/twitchdazal")

    if message.content.startswitch('!시참'):
        await client.send_message(message.channel, "주소 : handazal.kro.kr / 1.7.10 + 디코 시참방 무조건 들어와야 함")

    if message.content.startswitch('!명령어'):
        await client.send_message(message.channel,"명령어 ")
        embed = discord.Embed(title="명령어", description="!트위치, !시참, !카페, !유튜브", color=0x00ff00)
        embed.set_footer(text = "DaZal★Bot")
        await client.send_message(message.channel, embed=embed)

    
       
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
