from manim import *
import os
from easings import *
ASSETS_PATH = os.getcwd() + "/assets/"


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
        c = Square(fill_color=RED, fill_opacity=1).set_x(-3)
        s1 = SVGMobject(ASSETS_PATH + "gamecube.svg")
        s2 = SVGMobject(ASSETS_PATH + "wii.svg")


        self.play(
            TransformMatchingShapes(obj, c)
        )

class TextTest(Scene):

    def construct(self):
        t1 = Text(
            "slot machine",
            font="DINOT-Bold",
            color=WHITE,
        )
        t2 = Text(
            "time lost in me",
            font="DINOT-Bold",
            color=WHITE,
        ).rotate(45*DEGREES)

        t2.set_y(2)
        t2.set_x(2)

        self.play(
            Write(t1)
        )

        self.play(
            TransformMatchingShapes(t1, t2, path_arc=PI/8)
        )



def get_obj_by_id(obj, id):
    for i in obj.submobjects:
        if i.id == id:
            print("found", i)
            return i
    return None


def get_objs_by_ids(obj, ids):
    """
    This function gets all objects by id in ids
    and the rest as a VGroup
    Returns tuple(objs_by_ids, VGroup)
    """
    objs = VGroup()
    for i in ids:
        found = False
        for subm in obj.submobjects:
            if subm.id == i:
                print("found", i)
                objs.add(subm)
                break

    return objs

class UpdateRot(Scene):
    """
    Testing what happens one an object with a time updater gets
    transformed
    """


    def construct(self):
        self.ps3 = SVGMobject(ASSETS_PATH + "ps3.svg")
        self.ps4 = SVGMobject(ASSETS_PATH + "ps4_2.svg")
        left_handle = get_obj_by_id(self.ps3, "left_handle")
        right_handle = get_obj_by_id(self.ps3, "right_handle")
        left_handle_4 = get_obj_by_id(self.ps4, "left_handle")
        right_handle_4 = get_obj_by_id(self.ps4, "right_handle")

        body_ps3 = get_objs_by_ids(self.ps3, [
            "body_center",
            "body_center_inner",
        ])
        body_ps4 = get_obj_by_id(self.ps4, "body_center")

        self.play(
            ShowCreation(left_handle),
            ShowCreation(right_handle),
            ShowCreation(body_ps3),
        )
        self.play(
            FadeTransform(left_handle, left_handle_4),
            FadeTransform(right_handle, right_handle_4),
            FadeTransform(body_ps3, body_ps4),
            rate_func=ease_in_circ,
            run_time=.7
        )
        self.wait()

class MovingSquare(Scene):

    def construct(self):

        sq = Square(
            fill_color=YELLOW_D,
            fill_opacity=1,
            stroke_width=0
        ).scale(.8)
        sq2 = sq.copy().set_fill(color=BLUE_B, opacity=1)
        sq2.set_y(-2)
        sq2.set_x(-2)

        self.play(
            GrowFromCenter(sq),
            rate_func=ease_in_circ
        )

        self.play(FadeInFrom(sq2, 2*UP), rate_func=ease_in_elastic)

        self.play(
            ShrinkToCenter(sq),
            rate_func=ease_out_elastic
        )
        self.play(
            FadeOutAndShift(sq2, RIGHT),
            rate_func=ease_out_circ
        )



