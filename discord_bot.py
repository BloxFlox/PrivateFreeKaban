import discord
import pyfiglet
import random

intents = discord.Intents.all()
Perm = discord.Permissions.all() 

Perm.ban_members = True
Perm.kick_members = True
intents.members = True
intents.message_content = True

TOKEN = 'MTI2NDEzMTk2NjI1MzY2NjM2NQ.GkSOi4.cVYOg8yF1aMKXaEY8NwzrVt07Vw6siyWG7zdwA'

hello = pyfiglet.figlet_format('Discord','slant')

intents = discord.Intents.default()
intents.message_content = True

words = ['Привет!','Ура ты вернулся!','Наконец-то ты вернулся!','О,какие люди']

client = discord.Client(intents=intents, permissions=Perm)

ANSWERS = {
    '!прив': random.choice(words),
    '!как дела?': 'У меня всё отлично!',
    '!поиграем?': 'Да! Но я не знаю во что ты играешь('
}

GREETINGS = ['!прив','!добр','!здра']

HOWAREYOU = {
    '!хорошо': 'Это хорошо что хорошо',
    '!ок': 'Немногословно',
    '!эх': 'Эх, хотел бы я помочь, но я всего лишь бот',
    '!так себе': 'Ну нечего, сейчас поиграешь с друзьями и твоё настроение улучшится',
}

@client.event
async def on_ready():
    print(hello)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------')

@client.event
async def on_message(message):
    channel = message.channel

    for key in GREETINGS:
        if message.content.lower().startswith(key):
            await channel.send(ANSWERS['!прив'])
    
    def checkfunc(m):
        return m.content.lower() in HOWAREYOU and m.channel == channel

    if message.content.lower().startswith('!как дела?'):
        await channel.send(ANSWERS['!как дела?'])
        msg = await client.wait_for('message', check=checkfunc)
        await channel.send(HOWAREYOU[msg.content.lower()])

    if message.content.lower().startswith('!забанить'):
        list = message.content.split()
        for member in client.get_all_members():
            if str(member) == str(list[1]):
                await channel.send(f"{member} был забанен!")
                await member.ban(reason='Так нужно')

print("Hello")

    if message.content.lower().startswith('!кик'):
        list = message.content.split()
        for member in client.get_all_members():
            if str(member) == str(list[1]):
                await channel.send(f"{member} был кикнут!")
                await member.kick(reason='Так нужно')
                
client.run(TOKEN)
