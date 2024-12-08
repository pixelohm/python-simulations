# Local Imports
from ..utils.simulations_list import simulations
from ..constants.colours import HEX_WINDOW_BG_COLOUR

# External Imports
from PIL import Image, ImageTk

import customtkinter
import tkinter as tk
import pygame


class SimulationCanvas(customtkinter.CTkFrame):
    def __init__(self, master, simulation_id, width, height, **kwargs):
        super().__init__(master, **kwargs)
        
        # Initialize Pygame
        pygame.init()
        
        # Set up Pygame screen (surface)
        self.pygame_screen = pygame.Surface((width, height)) 
        self.pygame_screen.fill(HEX_WINDOW_BG_COLOUR)
        
        # Set up Tkinter Canvas
        self.canvas = tk.Canvas(self, width=width, height=height)
        self.canvas.pack(fill="both", expand=True)

        self.img_on_canvas = None

        # Load the appropriate simulation function from the simulations dictionary
        self.simulation_function = simulations.get(simulation_id, None)
        if self.simulation_function is None:
            raise ValueError(f"Simulation {simulation_id} not found.")
        
        # Initialize the simulation
        self.simulation_function.run(self.pygame_screen)

        # Call the update method to start drawing
        self.update_canvas()


    def update_canvas(self):
        """Update the tkinter canvas with the Pygame surface as an image."""
        
        # Convert the Pygame surface to a format that can be displayed in tkinter
        pygame_image = pygame.image.tostring(self.pygame_screen, "RGB")
        pil_image = Image.frombytes("RGB", (self.pygame_screen.get_width(), self.pygame_screen.get_height()), pygame_image)
        pil_image = pil_image.transpose(Image.FLIP_TOP_BOTTOM)  # Flip for proper orientation
        
        # Convert to ImageTk format
        photo_image = ImageTk.PhotoImage(pil_image)
        
        # If image exists on canvas, delete it
        if self.img_on_canvas:
            self.canvas.delete(self.img_on_canvas)
        
        # Display the image on the canvas
        self.img_on_canvas = self.canvas.create_image(0, 0, anchor=tk.NW, image=photo_image)
        
        # Keep a reference to the image to prevent garbage collection
        self.canvas.image = photo_image
        
        # Call the update method every 10 ms (to create a game loop)
        self.after(10, self.update_canvas)
