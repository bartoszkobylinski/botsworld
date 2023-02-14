import discord

client = discord.Client()

@client.event
async def on_member_join(member):
    #  Send message when a new member joins the server
    await member.send("Welcome to the server")

@client.event
async def on_member_move(member):
    #  Send message when a member leaves the server
    await member.send("We're sorry to see you go")

@client.event
async def on_member_update(before, after):
    #  Check if teh member's role chas changed
    if before.roles != after.roles:
        #  If the member has been given a new role
        if len(before.roles) < len(after.roles):
            new_role = list(set(after.roles) - set(before.roles))[0]
            await after.send(f"Congratulation, YOu have been given the {new_role} role.")
        #  If the member has had a role removed
        else:
            removed_role = list(set(before.roles) - set(after.roles))[0]
            await after.send(f"Sorry, you have had the {removed_role} role removed")

@client.event
async def on_ready():
    print("Bot is ready")

client.run("API_BOT_TOKIEn")