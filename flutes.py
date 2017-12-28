import botobject
bot = botobject.bot


@bot.command(pass_context=True)
async def SetFP(ctx, status):
    """Used to set the various flute player channels. Only accessible to Game Masters.\n\nThe <status> argument can be either 'victim' or 'master' (without the quotes)"""
    roles = []
    for role in ctx.message.author.roles:
        roles.append(role.name)

    if "Game Master" in roles:
        if status == "victim":
            ChannelID = ctx.message.channel.id
            with open("data/victim.channel", "w") as victim_set_file:
                victim_set_file.write(str(ChannelID))
                await bot.say("Flute Victim channel set successfully!")

        elif status == "master":
            ChannelID = ctx.message.channel.id
            with open("data/master.channel", "w") as master_set_file:
                master_set_file.write(str(ChannelID))
                await bot.say("Flute Master channel set successfully!")

        else:
            await bot.say("Invalid usage. Usage is: `!SetFP [status]`.\n\nStatus can be either `victim` or `master`")
    else:
        await bot.say("You don't have permission to do that!")

@bot.command(pass_context=True)
async def w(ctx, *, message):
    """Whisper to your flute victims >:)\n\nNote: Only avaliable in the Flute Master channel."""
    print("Test C Passed")
    with open ("data/victim.channel", "r") as victim_file:
        VictimID=victim_file.readlines()
        VictimID = str(VictimID[0])
        VictimChannel = bot.get_channel(VictimID)

    with open ("data/master.channel", "r") as master_file:
        MasterID=master_file.readlines()
        MasterID = str(MasterID[0])
        MasterChannel = bot.get_channel(MasterID)  

    if ctx.message.channel.id == MasterID:
        print("Test case A")
        await bot.send_message(VictimChannel, message)

    else:
        print("Test case B")
        await bot.delete_message(ctx.message)
        await bot.say("That's the wrong channel! I have deleted your original message to protect your identity.")

@bot.event
async def on_message(message):
    with open ("data/victim.channel", "r") as victim_file:
        VictimID=victim_file.readlines()
       # print("a:" + str(VictimID))
        VictimID = str(VictimID[0])
        #print("b:" + VictimID)
        VictimChannel = bot.get_channel(VictimID)

    with open ("data/master.channel", "r") as master_file:
        MasterID=master_file.readlines()
        MasterID = str(MasterID[0])
        MasterChannel = bot.get_channel(MasterID)

    # print(str(message.channel.id) + "\n" + VictimID + "\n" + MasterChannel)



    if str(message.channel.id) == str(VictimID):
        if message.author != bot.user:
            await bot.send_message(MasterChannel, "One of your victims said something! - " + message.author.mention + " said \n'`" + message.content + "`'!")
    else:
       python = "dum"

    await bot.process_commands(message)
