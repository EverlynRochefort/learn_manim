from manim import *

class LogoAnimation(Scene):
    def construct(self):
        # 1. Load your SVG logo
        # Replace "your_logo.svg" with the actual path to your SVG file.
        # Make sure the SVG file is in the same directory as your Python script,
        # or provide the full path to it.
        logo = SVGMobject("neovim-logo.svg")

        # 2. Adjust the logo's properties (optional)
        logo.set_color(BLUE_C)  # Set a color for the logo (e.g., a shade of blue)
                                # You can remove this line if your SVG already has colors.
        logo.set_height(4)      # Set the height of the logo to 4 units
        logo.center()           # Center the logo on the screen

        # 3. Animate the logo
        self.play(GrowFromCenter(logo)) # Makes the logo grow from its center
        self.wait(1)                     # Pause for 1 second

        # 4. (Optional) Add a simple fade out animation
        self.play(FadeOut(logo))
        self.wait(0.5)
