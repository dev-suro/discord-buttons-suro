from discord import Embed, Colour
from discord.utils import get
from discord_slash import SlashContext
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle
from utilities import get_rgb_from_hex

def register(slash, guild_id):
    """Register the command

    Args:
        slash ([type]): [description]
        guild_id ([type]): [description]
    """
    
    @slash.slash(name="vacation", guild_ids=[guild_id])
    async def role_buttons(ctx: SlashContext):
        """Handle role buttons

        Args:
            ctx (SlashContext): [description]
        """

        # Define role buttons
        buttons = [
            # Add first role
            create_button(
                style=ButtonStyle.blurple,
                label='Suro Vacation',
                emoji='🧳',

                # custom_id must be set to roleID!!!
                custom_id='934894056318840872'
            )
        ]
        action_row = create_actionrow(*buttons)

        # Message to appear above the buttons
        embed = Embed(
            title="🧳Suro Vacation🧳",
            description="**Sign up for the Suro Vacation Role if you are planning on attending.**\n\n> • Press the Button to get access.\n> • Press the button again to remove access.\n> • **Message a Madmin if an error occurs!**",
            color=Colour.from_rgb(*get_rgb_from_hex('FFFF00')))
        embed.set_image(url="https://cdn.discordapp.com/attachments/556945291417223218/934895468469690398/unknown.png")
        await ctx.send(embed = embed, components=[action_row])