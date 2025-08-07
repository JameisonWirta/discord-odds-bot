import discord
from discord.ext import commands
import os
import re

CUSTOM_MULTIPLIER = 0.9
decimal_pattern = re.compile(r"^-?\d+(\.\d{1,2})?$")

intents = discord.Intents.default()
intents.message_content = True  # ← This is required
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.command()
async def odds(ctx, *args):
    try:
        for arg in args:
            if not decimal_pattern.match(arg):
                raise ValueError("Invalid decimal format")

        numbers = [float(arg) for arg in args]
        result = 1
        for number in numbers:
            result *= number

        final_result = round(result * CUSTOM_MULTIPLIER, 2)
        await ctx.send(f"here are your odds x{final_result}")
    except ValueError:
        await ctx.send("Please enter only numbers with up to two decimal places, like: \\`!odds 2.35 3 1.5\\`")

bot.run(os.getenv("DISCORD_TOKEN"))
