from controller import get_objs_by_ids_rest
from manim import *
import os
from easings import *
from manim.utils.rate_functions import ease_in_expo
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
            x -= 1 * radius * (x - width / 2) / width
            y -= 1 * radius * (y - height / 2) / height
            obj.move_to(np.array([x, y, 0]))

        r = Rectangle(width=6, height=3)
        s.z_index = -1
        self.play(FadeIn(c))
        s.add_updater(upd)
        self.add(s)
        self.play(MoveAlongPath(c, r), run_time=3)
        self.play(ShowCreation(Circle()))


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


def get_obj_by_id(
        obj: typing.Union[Mobject, VGroup],
        index: str):
    for i in obj.submobjects:
        if i.id == index:
            print("found", i)
            return i
    return None


def get_objs_by_ids(
        obj: typing.Union[Mobject, VGroup],
        ids: list) -> VGroup:
    """
    This function gets all objects by id in ids
    and the rest as a VGroup
    Returns tuple(objs_by_ids, VGroup)
    """
    objs = VGroup()
    for i in ids:
        for submobject in obj.submobjects:
            if submobject.id == i:
                print("found", i)
                objs.add(submobject)
                break

    return objs


class UpdateRot(Scene):
    """
    Testing what happens one an object with a time updater gets
    transformed
    """

    def construct(self):
        self.ps3 = SVGMobject(ASSETS_PATH + "ps3.svg")
        for i in self.ps3.submobjects:
            i.set_stroke(width=.5)
        self.ps4 = SVGMobject(ASSETS_PATH + "ps4_2.svg")
        left_handle = get_obj_by_id(self.ps3, "left_handle")
        right_handle = get_obj_by_id(self.ps3, "right_handle")
        left_handle_4 = get_obj_by_id(self.ps4, "left_handle")
        right_handle_4 = get_obj_by_id(self.ps4, "right_handle")

        lights = [f"light_{i}" for i in range(1, 5)]
        analogs = ["_analog_base", "_analog", "_analog_inner"]
        left_analog = ["left"+i for i in analogs]
        right_analog = ["right"+i for i in analogs]
        logo = ["ps_logo_bg", "ps_logo"]

        logo_ps3 = get_objs_by_ids(self.ps3, logo)
        logo_ps4 = get_objs_by_ids(self.ps4, logo)

        analogs_ps3 = get_objs_by_ids(self.ps3,
                                      left_analog+right_analog)
        analogs_ps4 = get_objs_by_ids(self.ps4,
                                      left_analog+right_analog)

        body_ps3 = get_objs_by_ids(self.ps3, [
            "body_center",
            "body_center_inner",
        ])
        for i in body_ps3:
            i.z_index = -2
        lights_ps3 = get_objs_by_ids(self.ps3, lights)
        ss = get_objs_by_ids(self.ps3, [
            "start",
            "select"
        ])
        sm = get_objs_by_ids(self.ps4, [
            "share",
            "menu"
        ])

        ss_text = get_objs_by_ids(self.ps3, [
            "start_txt",
            "select_txt"
        ])

        body_ps4 = get_obj_by_id(self.ps4, "body_center")
        body_ps4.z_index = -2

        # Buttons

        animations = []
        transforms = []
        for i in ("cross", "triangle", "square", "circle"):
            # button: the circle
            # shape: cross, triangle, etc...
            button_ps3 = get_obj_by_id(self.ps3, f"{i}_button")
            button_ps4 = get_obj_by_id(self.ps4, f"{i}_button")
            shape_ps3 = get_obj_by_id(self.ps3, i)
            shape_ps4 = get_obj_by_id(self.ps4, i)
            shape_ps3.z_index = 3
            shape_ps4.z_index = 3
            button_ps4.z_index = 2
            button_ps3.z_index = 2

            animations.append(button_ps3.animate.match_style(button_ps4))
            animations.append(button_ps3.animate.move_to(button_ps4))
            transforms.append(Transform(shape_ps3, shape_ps4))

        holders_ps3 = get_objs_by_ids(self.ps3, ["buttons_holder", "dpad_holder"])
        holders_ps4 = get_objs_by_ids(self.ps4, ["left_circle", "right_circle"])
        dpad = get_obj_by_id(self.ps4, "arrows")
        dpad_ps3 = get_objs_by_ids(self.ps3, ["up", "down", "left", "right"])


        self.play(
            ShowCreation(self.ps3),
            rate_func=ease_in_circ,
        )
        self.play(
            LaggedStart(*[
                ShrinkToCenter(i)
                for i in [*lights_ps3, *ss_text]
            ]),
            run_time=1.0,
            rate_func=ease_in_circ,
        )
        self.play(
            FadeTransform(ss[0], sm[1]),
            FadeTransform(ss[1], sm[0]),
            FadeTransform(analogs_ps3, analogs_ps4),
            rate_func=ease_in_circ,
        )
        self.play(*[
            i.animate.match_style(j)
            for i, j in zip(holders_ps3, holders_ps4)
        ])

        self.play(FadeTransformPieces(dpad_ps3, dpad))
        self.play(
            *animations,
            *transforms
        )
        self.play(
            FadeTransform(left_handle, left_handle_4),
            FadeTransform(right_handle, right_handle_4),
            FadeTransform(body_ps3, body_ps4),
            logo_ps3.animate.move_to(logo_ps4),
            rate_func=ease_in_circ,
            run_time=.7
        )
        self.wait()


class Coords(Scene):
    """
    This one is for transition from 1D -> 2D -> 3D
    """

    def construct(self):
        dot = Dot(color=RED).scale(.5)
        self.play(GrowFromCenter(dot))
        new_dot = Dot(color=BLUE).scale(.5)
        new_dot.set_y(5)
        self.play(
            new_dot.animate.shift(3 * DOWN),
            rate_func=ease_in_elastic
        )
        line = Line(ORIGIN, new_dot, stroke_width=2)
        line.z_index = -1
        self.play(
            ShowCreation(line),
            rate_func=ease_in_circ
        )
        self.wait(.3)
        self.play(
            Rotating(line, radians=90 * DEGREES, about_point=dot.get_center()),
            Rotating(new_dot, radians=90 * DEGREES, about_point=dot.get_center()),
            run_time=2
        )
        new_line = Line(ORIGIN, 2 * RIGHT, stroke_width=2)
        new_line.z_index = -1
        self.play(
            ShowCreation(new_line),
            dot.animate.shift(2*RIGHT),
        )

        def test(p):
            x, y, z = p
            y = np.random.rand()
            if x == -2 or x == 2:
                y = 0

            y = np.clip(y, 0, 1)
            return [x, y, 0]
        self.play(
            ApplyPointwiseFunction(
                test,
                VGroup(line, new_line)
            )
        )
        self.wait()
