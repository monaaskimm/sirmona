import discord
import os
import random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'merhaba hazırım ben {client.user}' ) 

def yazi_tura():
    para = random.randint(0, 2)
    if para == 0:
        return "yazı meow....meow..."
    else:
        return "tura meow...meow..."
    
def e_o():
    emoji = ["🙀", "😻", "😿", "😺"]
    return random.choice(emoji)
    

@client.event
async def on_message(message):
 
    randomCatFileName = random.choices(os.listdir('img') , weights=[0.5,10,10,10,10,10,10,10,10,19.5] , k=10)
    randomCat = random.choice(randomCatFileName)
    for i in randomCatFileName:
        print(i)    
    with open(f"img/{randomCat}" , "rb") as file:
        picture = discord.File(file)
    if message.author == client.user:
        return
    if message.content.startswith('cat'):
        await message.channel.send(file=picture)
    elif message.content.startswith('kedi'):
        await message.channel.send(file=picture)
    elif message.content.startswith('beni tekrar etme'):
        await message.channel.send("🐱 meow....meow...meow") 
    elif message.content.startswith('meow'):
        await message.channel.send("🐱 meow....meow...meow") 
    elif message.content.startswith('para at'):
        await message.channel.send(yazi_tura())
    elif message.content.startswith('emoji at'):
        await message.channel.send(e_o())   
    else:
        await message.channel.send(message.content)
    
client.run("token")



    
