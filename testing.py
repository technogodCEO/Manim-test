from manim import *

class Testing(Scene):
    def construct(self):
        
        name = Tex("Roshan").to_edge(UL, buff=0.5)
        sq = Square(side_length=0.5, color = WHITE, fill_color = GREEN, fill_opacity = 0.75).shift(LEFT * 3)
        tri = Triangle().scale(0.6).to_edge(DR)

        self.play(Write(name))
        self.play(DrawBorderThenFill(sq), run_time = 2)
        self.play(Create(tri))
        self.wait()

        self.play(name.animate.to_edge(UR), run_time = 2)
        self.play(sq.animate.scale(2),tri.animate.to_edge(DL), run_time = 2)
        self.wait()