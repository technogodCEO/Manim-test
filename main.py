from manim import *

class HelloWorld(Scene):
    def construct(self):
        circ = Circle()
        sq = Square()
        self.add(circ) 
        self.add(sq)