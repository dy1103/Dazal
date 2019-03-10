import discord
import asyncio
import os

client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print("-------------------")
    await client.change_presence(game=discord.Game(name='아무짓도 안하는중', type=1))


@client.event
async def on_message(message):
    if message.content.startswith('!트위치'):
        await client.send_message(message.channel,"https://www.twitch.tv/dazal3635")


@client.event
async def on_message(message):
    if message.content.startswith('!유튜브'):
        await client.send_message(message.channel,"https://www.youtube.com/channel/UCntJ_88iKtM0LE4dX5ovqFw?view_as=subscriber")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
