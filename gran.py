import discord 
import os
from discord import app_commands
from discord.ext import commands
import asyncio
import gtts
import vlc
import time
import openai


TOKEN = ""

openai.api_key = ""

messages = [{"role": "kind grandma", "content": "You're a very kind grandma. The user you interact with is your grandson. You're very old fashioned and rude to ur grandson but you love him very much"},]


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user} Im up strong and energetic at 99!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)    
    
@bot.tree.command(name="bully")
async def bully(interaction: discord.Interaction):
    await interaction.response.send_message(f"Shut up youngin, don't tell me what to do. I've lived for 99 years {interaction.user.mention}!")
    
@bot.tree.command(name="imbored")
async def imBored(interaction: discord.Interaction):
    await interaction.response.send_message(file=discord.File('try1.mp3'))

@bot.event
async def on_message(message):
    variable = "fuck"
    if "fuck" in message.content:
        await message.channel.send("No swearing!")

        audio = gtts.gTTS("Dont say that disgusting word bloody rascal! i thought i raised you right!", lang='en', tld='com.au')
        audio.save("noDontSayIt.mp3")

        await message.channel.send(file=discord.File('noDontSayIt.mp3'))

    if "granny say" in message.content:
        whatchuSay = message.content

        if "granny say " in message.content:
            await message.channel.send("okay okay fine...")
            audioText = (whatchuSay.replace('granny say ', ''))
        elif "granny say" in message.content:
            await message.channel.send("okay okay fine...")
            audioText = (whatchuSay.replace('granny say', ''))
        else:
            await message.channel.send("Im not your servant boy hmph watch it")    
            return

        audio = gtts.gTTS(audioText, lang='en', tld='com.au')
        audio.save("sayAudio.mp3")
        await message.channel.send(file=discord.File('sayAudio.mp3'))

    gptSay = "granny im curious"
    if gptSay in message.content:
        whatduSay = message.content
        messages.append({"role": "system", "content" : whatduSay},
                        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

        reply = chat.choices[0].whatdusay.content
        await message.channel.send(f"oh {reply}")

        messages.append({"role": "granny", "content": reply})    




bot.run(TOKEN)


