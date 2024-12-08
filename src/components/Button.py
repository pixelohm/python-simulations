import customtkinter as ctk
from ..constants.colours import HEX_ORANGE, HED_DARK_ORANGE


class Button(ctk.CTkButton):
    def __init__(
        self,
        master,
        text,
        command,
        width=150,
        height=40,
        bg_color=HEX_ORANGE,
        text_color="white",
        corner_radius=12,
        border_width=0,
        border_spacing=2,
        hover_color=HED_DARK_ORANGE,
        border_color=HEX_ORANGE,
        text_color_disabled="gray",
        font=("Arial", 14),
        image=None,
        state="normal",
        hover=True,
        compound="left",
        anchor="center",
        **kwargs
    ):
        super().__init__(master, text=text, command=command, **kwargs)

        # Configure the button with all passed arguments
        self.configure(
            width=width,
            height=height,
            corner_radius=corner_radius,
            border_width=border_width,
            border_spacing=border_spacing,
            fg_color=bg_color,
            hover_color=hover_color,
            border_color=border_color,
            text_color=text_color,
            text_color_disabled=text_color_disabled,
            font=font,
            image=image,
            state=state,
            hover=hover,
            compound=compound,
            anchor=anchor,
        )
