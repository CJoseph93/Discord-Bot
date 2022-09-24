import discord
import asyncio
import random

memecount = 0
memes = []
client = discord.Client()

@asyncio.coroutine
@client.event
async def on_message(message):
	if message.content == '!corby help':
		await client.send_message(message.channel, content=helpContent())
	elif message.content.startswith('!corby nc'):
		test = message.content
		serv = message.server
		whatevs, command, name, change = test.split(" ")
		await client.change_nickname(serv.get_member_named(name), change)
	elif message.content == '!corby rock':
		RPS(1)
	elif message.content == '!corby paper':
		RPS(2)
	elif message.content == '!corby scissors':
		RPS(3)
	elif message.content.startswith('!corby tts'):
		test = message.content
		author = message.author
		whatevs, command, texttospeech = test.split(" ", 2)
		vc = await client.join_voice_channel(author.voice_channel)
		await client.send_message(message.channel, content=texttospeech, tts=True)
		await vc.disconnect()
	elif message.content == '!corby what game?' or message.content == '!corby what game? tts':
		ts = False
		if message.content == '!corby what game? tts':
			ts = True
		game = gameChoose()
		await client.send_message(message.channel, content=game, tts=ts)
	elif message.content == '!corby meme':
		await client.send_message(message.channel, content=generateMeme())
	elif message.content.startswith('!corby addmeme'):
		test = message.content
		whatevs, command, memeToAdd = test.split(" ", 2)
		addMeme(memeToAdd)
	#	player = await vc.create_ffmpeg_player('vent.wav', after=lambda: player.disconnect())
	#	player.start()
		
def gameChoose():
		gamelist = ["PUBG","Counter Strike","Overwatch","Golf with friends","Hand Simulator","GTA V","Garry's mod","Civilization V","Warframe"]
		x = random.randint(1, len(gamelist))
		return gamelist[x]
			
def addMeme(memeToAdd):
	global memecount
	global memes
	memes.append(memeToAdd)
	memecount += 1
	
def generateMeme():
	global memes
	global memecount
	if memecount > 0:
		x = random.randint(1, memecount)
		return memes[x - 1]
	else:
		return 'no memes available'
			
def RPS(playerSection):
	botChoice = random.randint(1,3)
	resultmessage = "You tie!"
	result = playerSection - botChoice
	if result == -2 or (result > 0 and result != 2):
		resultmessage = "You win!"
	elif result < 0 or result == 2:
		resultmessage = "you lose"
	await client.send_message(message.channel, content=result)
			
def helpContent():
	x = 'Try these commands:\n'
	x += '1. !corby nc "nickname to change" "nickname to be changed to"\n'
	x += '2. !corby "rock" or "paper" or "scissors"\n'
	x += '3. !corby tts "your message" (for a text to speech message)\n'
	x += '4. !corby what game? or !corby what game? tts\n'
	x += '5. !corby addmeme (link meme here)\n'
	x += '6. !corby meme (to generate meme)'
	return x
		

