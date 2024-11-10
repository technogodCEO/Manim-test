from manim import *

class MakingSquare(Scene):
    def construct(self):
        sq = VMobject(fill_color=GREEN)
        points = [[1,1,0], [1,-1, 0], [-1,-1,0], [-1,1,0], [1,1,0]]
        dots = VGroup(*[Dot(p) for p in points])

        self.add(dots)
        sq.set_points_as_corners(points)
        
        self.play(Create(sq), run_time = 2)
