import discord
import random

# Botun ayrıcalıklarını tanımlayalım
intents = discord.Intents.default()
intents.message_content = True

# Bot oluşturalım ve ayrıcalıkları aktaralım
client = discord.Client(intents=intents)

# Plastik el işleri fikirleri içeren bir liste oluşturalım
plastik_el_isleri = [
    "Plastik bir tabağı kalınlaştırıp arkadaşında bir frizbi oyna!",
    "Plastik bardaklarla bir kule yap sonrada nişancılığını göster :) ",
    "Strafor köpüklerle bir güneş sistemi yap!",
    "Plastik tabakları bir çerçeve gibi boya!",
    "Plastik tabaklara emoji,hayvan,desen,şekil çizip bir hafıza oyunu yap!",
    "Plastik şişelerden gemi yapıp arkadaşlarınla yarıştır!"
]

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!plastik_el_isleri'):
        # Rastgele bir plastik el işi fikri seçelim
        fikir = random.choice(plastik_el_isleri)
        await message.channel.send(f"İşte bir plastik el işi fikri: {fikir}")

# Botu çalıştıralım
client.run("your token")
