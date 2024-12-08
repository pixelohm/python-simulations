from src.components.Text import Text
from src.constants.window import WIN_WIDTH, WIN_HEIGHT
from src.constants.colours import HEX_WINDOW_BG_COLOUR
from src.components.Button import Button
from src.utils.simulations_list import simulations

import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.width = WIN_WIDTH
        self.height = WIN_HEIGHT
        self.geometry(f"{self.width}x{self.height}")
        self.configure(fg_color=HEX_WINDOW_BG_COLOUR)

        self.title_section()
        self.simulation_button_section()

    def title_section(self):
        """Create the title section with the app name or header."""
        self.title_label = Text(self, text="Salkaro", font_size=24)
        self.title_label.pack(pady=20)

    def simulation_button_section(self):
        """Create the section with simulation buttons."""

        # Define a callback function for the buttons
        def on_button_click(simulation_id):
            simulations[simulation_id].run()

        # Create and pack simulation buttons
        self.sim_button1 = Button(
            self,
            text="Conways Game of Life",
            command=lambda: on_button_click("conways_game_of_life"),
        )
        self.sim_button1.pack(pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()
