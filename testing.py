from manim import *


class TestShadow(Scene):

    def construct(self):
        radius = .5
        c = Circle(
            radius=radius,
            stroke_width=0,
            fill_color=YELLOW_B,
            fill_opacity=1
        )
        s = c.copy().scale(.85)
        s.set_fill(color=GREY, opacity=1)

        height = config.frame_height

        width = config.frame_width
        print(width, height)

        def upd(obj, dt):
            x = c.get_x()
            y = c.get_y()
            x -= 1 * radius * (x - width / 2) / width;
            y -= 1 * radius * (y - height / 2) / height;
            obj.move_to(np.array([x, y, 0]))

        r = Rectangle(width=6, height=3)
        s.z_index = -1
        get_shaded_rgb()
        self.play(FadeIn(c))
        s.add_updater(upd)
        self.add(s)
        self.play(MoveAlongPath(c, r), run_time=3)
        self.play(ShowCreation(Circle()))


class FadeTransformSubmobjects(Scene):
    def construct(self):
        src = VGroup(Square(), Circle().shift(LEFT + UP))
        src.shift(3*LEFT + 2*UP)
        src_copy = src.copy().shift(4*DOWN)

        target = VGroup(Circle(), Triangle().shift(RIGHT + DOWN))
        target.shift(3*RIGHT + 2*UP)
        target_copy = target.copy().shift(4*DOWN)

        self.play(FadeIn(src), FadeIn(src_copy))
        self.play(
            FadeTransform(src, target),
            FadeTransformPieces(src_copy, target_copy)
        )
        self.play(*[FadeOut(mobj) for mobj in self.mobjects])

class TestMoveRot(Scene):

    def construct(self):
        obj = Square(fill_color=BLUE, fill_opacity=1).scale(.3)

        self.play(
            obj.animate.shift(2 * RIGHT).rotate(.5 * PI)
        )