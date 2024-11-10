from manim import *

class UpdaterExample(Scene):

    def construct(self):
        nl = NumberLine(include_numbers=True)
        selector = Triangle(fill_opacity=1).scale(0.2).rotate(PI/3)

        dn = DecimalNumber(0) # <-- needs a start value

        def update_selector(mob):
            mob.next_to(nl.n2p(dn.get_value()),UP,buff=0)
            #                  --------------
            #  In this way we can acces to the DecimalNumber value

        def update_dn(mob):
            mob.next_to(selector,UP,buff=0.1)

        selector.add_updater(update_selector)
        dn.add_updater(update_dn)

        self.add(nl,selector,dn)
        self.wait(0.5)
        self.play(
            ChangeDecimalToValue(dn, 4),
            run_time=2
        )
        self.wait(0.5)
        self.play(
            ChangeDecimalToValue(dn, -1),
            run_time=2
        )
        self.wait(0.5)
        self.play(
            ChangeDecimalToValue(dn, -4),
            run_time=2
        )
        self.wait(0.5)
        self.play(
            ChangeDecimalToValue(dn, 7),
            run_time=3
        )
        self.wait(0.5)

        

       