import discord
import random
import requests
import os
from bs4 import BeautifulSoup

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith("$joke"):
        api_url = "https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Dark,Pun,Spooky,Christmas?blacklistFlags=racist,sexist&type=single"

        try:
            response = requests.get(api_url)
            data = response.json()
            await message.channel.send(data['joke'])

        except Exception as e:
            await message.channel.send(f"Error fetching API: {e}")

    elif msg.startswith("$chiste"):
        api_url = "https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Dark,Pun,Spooky,Christmas?lang=es&blacklistFlags=racist,sexist&type=single"

        try:
            response = requests.get(api_url)
            data = response.json()
            await message.channel.send(data['joke'])

        except Exception as e:
            await message.channel.send(f"Error fetching API: {e}")

    elif msg.startswith("$meme"):
        n = random.randint(1, 40)
        # print(f"For n: {n}")

        source = requests.get('https://www.cuantocabron.com/ultimos/p/' + str(n)).text
        # soup = BeautifulSoup(source, "lxml")
        soup = BeautifulSoup(source, "html.parser")
        img = soup.find_all("img")

        gallery = []
        for i in img:
            if "facebook" not in i.get("src") and "twitter" not in i.get("src") and "thumb" not in i.get("src"):
                gallery.append(i.get("src"))

        e = discord.Embed()
        e.set_image(url=random.choice(gallery))
        await message.channel.send(embed=e)

    elif msg.startswith("$help"):
        em = discord.Embed(
            title="Help",
            description="***$chiste*** retorna un chiste\n\n***$joke*** returns a joke\n\n***$meme*** retorna un momazo"
        )
        await message.channel.send(embed=em)


client.run(os.environ["TOKEN"])
