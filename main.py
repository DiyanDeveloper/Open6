import discord
from discord.ext import commands
from discord import app_commands
import os
import random
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')

openrouter_client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='!', 
            intents=discord.Intents.all(),
            help_command=None
        )
        self.xp_data = {}

    async def setup_hook(self):
        await self.tree.sync()
        print(f"Logged in as {self.user} and synced slash commands!")

bot = MyBot()

@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel:
        embed = discord.Embed(
            title=f"Welcome to the server, {member.name}! 🎉",
            description=f"You are our {len(member.guild.members)}th member! Please check the rules.",
            color=discord.Color.brand_green()
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        await channel.send(embed=embed)

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    user_id = message.author.id
    if user_id not in bot.xp_data:
        bot.xp_data[user_id] = {"xp": 0, "level": 1}
    
    bot.xp_data[user_id]["xp"] += random.randint(15, 25)
    current_xp = bot.xp_data[user_id]["xp"]
    current_level = bot.xp_data[user_id]["level"]
    xp_needed = current_level * 100
    
    if current_xp >= xp_needed:
        bot.xp_data[user_id]["level"] += 1
        bot.xp_data[user_id]["xp"] = 0
        embed = discord.Embed(
            title="Level Up! 🌟",
            description=f"Congratulations {message.author.mention}, you advanced to **Level {current_level + 1}**!",
            color=discord.Color.gold()
        )
        await message.channel.send(embed=embed)
        
    await bot.process_commands(message)

@bot.tree.command(name="ask", description="Ask the AI anything!")
@app_commands.describe(question="What do you want to know?")
async def ask(interaction: discord.Interaction, question: str):
    await interaction.response.defer()
    
    try:
        response = await openrouter_client.chat.completions.create(
            model="meta-llama/llama-3-8b-instruct:free",
            messages=[{"role": "user", "content": question}],
        )
        
        answer = response.choices[0].message.content[:4000]
        
        embed = discord.Embed(
            title=f"Question: {question}", 
            description=answer, 
            color=discord.Color.blurple()
        )
        
        avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
        embed.set_footer(text=f"Requested by {interaction.user.display_name}", icon_url=avatar_url)
        
        await interaction.followup.send(embed=embed)
    except Exception as e:
        await interaction.followup.send(f"Error connecting to OpenRouter: {str(e)[:1000]}")

@bot.tree.command(name="rank", description="Check your current level and XP")
async def rank(interaction: discord.Interaction):
    user_id = interaction.user.id
    stats = bot.xp_data.get(user_id, {"xp": 0, "level": 1})
    xp_needed = stats['level'] * 100
    
    embed = discord.Embed(title=f"{interaction.user.name}'s Rank", color=discord.Color.blurple())
    embed.add_field(name="Level", value=f"**{stats['level']}**", inline=True)
    embed.add_field(name="XP", value=f"{stats['xp']} / {xp_needed}", inline=True)
    embed.set_thumbnail(url=interaction.user.display_avatar.url)
    
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="clear", description="Clear a specified number of messages")
@app_commands.checks.has_permissions(manage_messages=True)
async def clear(interaction: discord.Interaction, amount: int):
    await interaction.response.defer(ephemeral=True)
    deleted = await interaction.channel.purge(limit=amount)
    await interaction.followup.send(f"🧹 Swept away {len(deleted)} messages.", ephemeral=True)

@bot.tree.command(name="kick", description="Kick a member from the server")
@app_commands.checks.has_permissions(kick_members=True)
async def kick(interaction: discord.Interaction, member: discord.Member, reason: str = None):
    await member.kick(reason=reason)
    embed = discord.Embed(
        title="Member Kicked 👢", 
        description=f"**{member.mention}** was kicked.\n**Reason:** {reason or 'No reason provided'}", 
        color=discord.Color.orange()
    )
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="ban", description="Ban a member from the server")
@app_commands.checks.has_permissions(ban_members=True)
async def ban(interaction: discord.Interaction, member: discord.Member, reason: str = None):
    await member.ban(reason=reason)
    embed = discord.Embed(
        title="Member Banned 🔨", 
        description=f"**{member.mention}** was banned.\n**Reason:** {reason or 'No reason provided'}", 
        color=discord.Color.red()
    )
    await interaction.response.send_message(embed=embed)

class RPSView(discord.ui.View):
    def __init__(self, player: discord.Member):
        super().__init__(timeout=60)
        self.player = player

    @discord.ui.button(label="Rock", style=discord.ButtonStyle.secondary, emoji="🪨")
    async def rock(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.play_game(interaction, "Rock")

    @discord.ui.button(label="Paper", style=discord.ButtonStyle.secondary, emoji="📄")
    async def paper(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.play_game(interaction, "Paper")

    @discord.ui.button(label="Scissors", style=discord.ButtonStyle.secondary, emoji="✂️")
    async def scissors(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.play_game(interaction, "Scissors")

    async def play_game(self, interaction: discord.Interaction, user_choice: str):
        if interaction.user != self.player:
            return await interaction.response.send_message("This isn't your game!", ephemeral=True)

        bot_choice = random.choice(["Rock", "Paper", "Scissors"])
        
        if user_choice == bot_choice:
            result = "It's a tie!"
            color = discord.Color.light_grey()
        elif (user_choice == "Rock" and bot_choice == "Scissors") or \
             (user_choice == "Paper" and bot_choice == "Rock") or \
             (user_choice == "Scissors" and bot_choice == "Paper"):
            result = "You win! 🎉"
            color = discord.Color.green()
        else:
            result = "I win! 🤖"
            color = discord.Color.red()

        embed = discord.Embed(title="Rock Paper Scissors", color=color)
        embed.add_field(name="You Chose", value=user_choice, inline=True)
        embed.add_field(name="I Chose", value=bot_choice, inline=True)
        embed.add_field(name="Result", value=f"**{result}**", inline=False)
        
        for child in self.children:
            child.disabled = True
            
        await interaction.response.edit_message(embed=embed, view=self)

@bot.tree.command(name="rps", description="Play a game of Rock, Paper, Scissors against me!")
async def rps(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Rock, Paper, Scissors!", 
        description="Click a button below to make your move.", 
        color=discord.Color.gold()
    )
    view = RPSView(interaction.user)
    await interaction.response.send_message(embed=embed, view=view)

if __name__ == '__main__':
    bot.run(DISCORD_TOKEN)
