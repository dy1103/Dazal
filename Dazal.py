import discord
import asyncio
import os

client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print("-------------------")
    await client.change_presence(game=discord.Game(name='!명령어', type=1))
    
    
@client.event
async def on_message(message):
    if message.content.startswith('!명령어'):
        await client.send_message(message.channel, "명령어, 트위치, 시참, 카페, 유튜브")
        
    if message.content.startswith('!트위치'):
        
        await client.send_message(message.channel, "https://www.twitch.tv/dazal3635")
        
    if message.content.startswith('!유튜브'):
        await client.send_message(message.channel, "https://www.youtube.com/channel/UCntJ_88iKtM0LE4dX5ovqFw?view_as=subscriber")
        
    if message.content.startswith('!카페'):
        await client.send_message(message.channel, "https://cafe.naver.com/twitchdazal")
        
    if message.content.startswith('!시참'):
        await client.send_message(message.channel, "주소 : handazal.kro.kr / 1.7.10 + 디코 시참방 무조건 들어와야 함")
        
    if message.content.startswith('!선택'):
        choice = message.content.split(" ")
        choicenumber = random.randint(1, len(choice)-1)
        choiceresult = choice[choicenumber]
        await client.send_message(message.channel, choiceresult)
    
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
