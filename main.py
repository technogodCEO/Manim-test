from manim import *

class FirstExample(Scene):
    def construct(self):
        sq = Square()

        def square_update(s):
            s.shift(0.2*RIGHT)

        conter = 0 

        while conter<5:
            conter +=1
            sq = Square()
            self.play(Create(sq))
            sq.add_updater(square_update)
            self.play(sq.animate())
            if sq.get_x() >= 7.1:
                self.remove(sq)
                
            