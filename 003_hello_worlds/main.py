from manim import *

class HelloWorlds(Scene):
    def construct(self):
        text= Text("Hello, Worlds!")

        self.play(Write(text), run_time= 2)
