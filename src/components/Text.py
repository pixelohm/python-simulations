import customtkinter as ctk


class Text(ctk.CTkLabel):
    def __init__(
        self,
        master,
        text,
        font_size=14,
        font_family="Arial",
        text_color="white",
        anchor="center",
        compound="center",
        justify="center",
        padx=1,
        pady=1,
        width=10,
        height=10,
        corner_radius=0,
        fg_color="transparent",
        textvariable=None,
        **kwargs
    ):
        """
        Custom Text class to create and configure labels with advanced options.

        :param master: The parent widget (e.g., a window or frame).
        :param text: The text to display on the label.
        :param font: Tuple containing font name and size.
        :param text_color: The color of the text.
        :param anchor: Alignment of the text inside the label (default is center).
        :param compound: Position of image relative to text (default is center).
        :param justify: Justification of multiple lines of text ("left", "center", "right").
        :param padx: Extra space added left and right of the text.
        :param pady: Extra space added above and below the text.
        :param width: The width of the label (in px).
        :param height: The height of the label (in px).
        :param corner_radius: The corner radius of the label (for rounded corners).
        :param fg_color: Foreground color of the label (can be a tuple or single color).
        :param textvariable: `StringVar` to dynamically update the text of the label.
        :param kwargs: Any additional arguments passed to the CTkLabel widget.
        """
        super().__init__(
            master,
            text=text,
            font=(font_family, font_size),
            text_color=text_color,
            anchor=anchor,
            compound=compound,
            justify=justify,
            padx=padx,
            pady=pady,
            width=width,
            height=height,
            corner_radius=corner_radius,
            fg_color=fg_color,
            textvariable=textvariable,
            **kwargs
        )

        # Configure the label with the passed or default properties
        self.configure(
            text=text,
            font=(font_family, font_size),
            text_color=text_color,
            anchor=anchor,
            compound=compound,
            justify=justify,
            padx=padx,
            pady=pady,
            width=width,
            height=height,
            corner_radius=corner_radius,
            fg_color=fg_color,
            textvariable=textvariable,
        )
