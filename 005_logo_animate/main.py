from manim import *

class LogoAnimation(Scene):
    def construct(self):
        logo = SVGMobject("neovim-logo.svg")
        
        logo.set_color(BLUE_C)

        logo.set_height(4)     
        logo.center()           

        self.play(GrowFromCenter(logo)) 
        self.wait(1)                    

        self.play(FadeOut(logo))
        self.wait(0.5)
