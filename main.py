import discord

# Functions
def check_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Set up Intents for Discord
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('!spamDM'):
        commands = message.content.split()
        # Validate the params
        # First param validation
        param1 = commands[1]
        if check_int(param1):
            num_spam = int(param1)
        

        # Check if there are at least two parameters
        if len(commands) == 2 and check_int(param1):
            
            # Do something with the parameters
            await message.channel.send(f"Command received with parameters: {num_spam}")
            user_id = "253009433972441089"
            user = await client.fetch_user(user_id)
            if user is None:
                await message.channel.send(f"Invalid user ID: {user_id}")
            else:
                for i in range(num_spam):
                    print(i)
                    await user.send("Zac go fuck yourself. Dont report this tho")
        else:
            await message.channel.send("Invalid command. Usage: !spamDM [Number of spams]")

# Replace BOT_TOKEN with your bot's token
client.run('MTA5NTM1NzUyNzI3NDgzNjA0OA.GkVZjt.Uv0jRhtXz8ab-eEX8tNbvejKsx3Sxh2RCZ8ZTU')