from manim import *

class Errors(Scene):
    def construct(self):
        
        c = Circle(radius=2)

        self.play(Write(c))