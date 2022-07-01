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
    
    @slash.slash(name="LostLands", guild_ids=[guild_id])
    async def role_buttons(ctx: SlashContext):
        """Handle role buttons

        Args:
            ctx (SlashContext): [description]
        """

        # Define role buttons
        buttons = [
            # Add first role
            create_button(
                style=ButtonStyle.orange,
                label='Lost Lands',
                emoji='🐱‍🐉',

                # custom_id must be set to roleID!!!
                custom_id='992483399212224562'
            )
        ]
        action_row = create_actionrow(*buttons)

        # Message to appear above the buttons
        embed = Embed(
            title="🐱‍🐉Lost Lands🐱‍🐉",
            description="**Sign up for the Lost Lands Role if you are planning on attending.**\n\n> • Press the Button to get access.\n> • Press the button again to remove access.\n> • **Message a Madmin if an error occurs!**",
            color=Colour.from_rgb(*get_rgb_from_hex('6AFE00')))
        embed.set_image(url="https://www.lostlandsfestival.com/wp-content/uploads/2019/10/5.-LOSTLANDS2021_092521_182205-3964_@jakewestphoto.jpg")
        await ctx.send(embed = embed, components=[action_row])