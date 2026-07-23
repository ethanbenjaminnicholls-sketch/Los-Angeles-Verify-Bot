import discord
from discord.ext import commands
import os

# ─── CONFIG ───────────────────────────────────────────────
DISCORD_TOKEN     = os.environ["DISCORD_TOKEN"]   # Set this in Railway Variables
VERIFY_CHANNEL_ID = 1527458422138736660
VERIFIED_ROLE_ID  = 1484208135299272828
# ──────────────────────────────────────────────────────────

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

synced = False


class VerifyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="✅ Verify",
        style=discord.ButtonStyle.green,
        custom_id="verify_button"
    )
    async def verify(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = interaction.guild.get_role(VERIFIED_ROLE_ID)

        if role is None:
            await interaction.response.send_message("❌ Verified role not found.", ephemeral=True)
            return

        if role in interaction.user.roles:
            await interaction.response.send_message("✅ You are already verified!", ephemeral=True)
            return

        await interaction.user.add_roles(role)
        await interaction.response.send_message(
            "🎉 You have been successfully verified! Welcome to **Los Angeles State Roleplay**.",
            ephemeral=True
        )


@bot.tree.command(name="sendverify", description="Send the verification panel.")
@commands.has_permissions(administrator=True)
async def sendverify(interaction: discord.Interaction):
    channel = interaction.guild.get_channel(VERIFY_CHANNEL_ID)

    if channel is None:
        await interaction.response.send_message("❌ Verification channel not found.", ephemeral=True)
        return

    embed = discord.Embed(
        title="🔒 Los Angeles State Roleplay Verification",
        description=(
            "Welcome to **Los Angeles State Roleplay!**\n\n"
            "To gain access to all server channels, click the **Verify** button below.\n\n"
            "By verifying, you agree to follow all server rules.\n\n"
            "**Click the button below to continue.**"
        ),
        color=discord.Color.blue()
    )
    embed.set_footer(text="Los Angeles State Roleplay")
    if interaction.guild.icon:
        embed.set_thumbnail(url=interaction.guild.icon.url)

    await channel.send(embed=embed, view=VerifyView())
    await interaction.response.send_message(
        f"✅ Verification panel sent to {channel.mention}.", ephemeral=True
    )


@bot.event
async def on_ready():
    global synced
    bot.add_view(VerifyView())
    if not synced:
        await bot.tree.sync()
        synced = True
        print("✅ Slash commands synced.")
    print(f"✅ Logged in as {bot.user}")


bot.run(DISCORD_TOKEN)
