import discord

intents = discord.Intents.default()
intents.message_content = True  
client = discord.Client(intents=intents)

import random


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('mona'):
        await message.channel.send("mona.jpeg")
    if message.content.startswith('yazitura'):
        await message.channel.send("yazi_tura()")
    elif message.content.startswith('şifre?'):
          password = sifre_olusturucu(10)
          await message.channel.send(password)
    else:
          await message.channel.send("meow...meow....meow")


    
def sifre_olusturucu(sifre_uzunlugu):
    ogeler = "+-/*!&$#?=@<>"
    sifre = ""

    for i in range(sifre_uzunlugu):
        sifre += random.choice(ogeler)

    return sifre   

def yazi_tura():
    para = random.randint(0, 2)
    if para == 0:
        return "meow"
    else:
        return "meow"

client.run("token")
