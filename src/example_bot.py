# pulled from https://discordpy.readthedocs.io/en/latest/quickstart.html#a-minimal-bot

import discord
import os 

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith("$comeback "):
        list=message.content.split()
        if(len(list)>1):
            fullName=""
            for i in range(1,len(list)-1):
                fullName+=list[i]+" "
            fullName+=list[len(list)-1]
            await message.channel.send('This is still under construction. But I see that you want comebacks for ' + fullName + ".")


    if message.content.startswith('$help'):
        embed = discord.Embed(
            colour=discord.Colour.green(),
            title="Help",
            #description="Command Listing"
        )

        embed.set_author(name="Author", icon_url="https://cdn.discordapp.com/attachments/625510693499568138/771565443461808128/twice-fingerheart-prints.jpg")
        #embed.set_image(url="https://cdn.discordapp.com/attachments/443208943213477889/601699371221909504/imagesfidosfhdis.jpg")
        #embed.set_thumbnail(url="shows at the top right")
        embed.add_field(name="$comeback [group-name-goes-here]", value="Looks for a recent or upcoming comeback for the specified group", inline=False)
        embed.add_field(name="$filler1", value="Nothing happens!", inline=False)
        embed.add_field(name="$filler2", value="Nothing! :D", inline=False)
        #embed.set_footer(text="This is a footer")

        await message.channel.send(embed=embed)

client.run('token-goes-here')

