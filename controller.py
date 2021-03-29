from manim import *
import os
ASSETS_PATH = os.getcwd() + "/assets/"



def get_obj_by_id(obj, id):
    for i in obj.submobjects:
        if i.id == id:
            return i
    return None

def get_objs_by_ids_rest(obj, ids):
    """
    This function gets all objects by id in ids
    and the rest as a VGroup
    Returns tuple(objs_by_ids, VGroup)
    """
    objs = VGroup()
    rest = VGroup()
    for i in obj.submobjects:
        if i.id not in ids:
            rest.add(i)

    for i in ids:
        found = False
        for subm in obj.submobjects:
            if subm.id == i:
                print("found", i)
                objs.add(subm)
                break
                
    return (objs, rest)


class Test(Scene):
    """
    This scene is for testing svg files and some transition
    """

    def construct(self):
        xbox = SVGMobject(ASSETS_PATH + "xbox_360.svg")
        xbox_fat = SVGMobject(ASSETS_PATH + "xbox_fat.svg")
        ps2 = SVGMobject(ASSETS_PATH + "ps2.svg")
        switch = SVGMobject(ASSETS_PATH + "switch.svg")
        switch_pro = SVGMobject(ASSETS_PATH + "switch_pro.svg").scale(1.0)
        square_button_ = get_obj_by_id(ps2, "square_button")
        square_button_.set_stroke("#FF01DB", 3)
        self.play(DrawBorderThenFill(switch))
        """
        a_button = get_obj_by_id(xbox, "a_button")
        b_button = get_obj_by_id(xbox, "b_button")
        x_button = get_obj_by_id(xbox, "x_button")
        y_button = get_obj_by_id(xbox, "y_button")
        x_button_ = get_obj_by_id(ps2, "x_button")
        triangle_button_ = get_obj_by_id(ps2, "triangle_button")
        circle_button_ = get_obj_by_id(ps2, "circle_button")
        square_button_ = get_obj_by_id(ps2, "square_button")
        square_button_.set_stroke("#FF01DB", 3)
        transforms = [
            (a_button, x_button_),
            (b_button, circle_button_),
            (x_button, square_button_),
            (y_button, triangle_button_)
        ]
        for i,j in transforms: print(i, j)
        self.play(ShowCreation(xbox))
        self.wait(.4)
        self.play(
            LaggedStart(*[
                ReplacementTransform(i, j)
                for i, j in transforms
            ]
            )
        )
        xbox_ids = ["a_button", "b_button", "x_button", "y_button", "right_analog", "left_analog"]
        ps2_ids = ["x_button", "circle_button", "square_button", "triangle_button", "right_analog", "left_analog"]
        xbox_obj, xbox_rest = get_objs_by_ids_rest(xbox, xbox_ids)
        ps2_obj, ps2_rest = get_objs_by_ids_rest(ps2, ps2_ids)
        self.play(
            *[
                ApplyMethod(i.shift, 2 * UP)
                for i in xbox_obj
            ]
        )
        self.play(ReplacementTransform(xbox_rest, ps2_rest))
        self.play(
            LaggedStart(*[
                ReplacementTransform(i, j)
                for i,j in zip(xbox_obj, ps2_obj)
            ]),
            #ReplacementTransform(xbox_rest, ps2_rest)
        )
        """
        left_con, *t = get_objs_by_ids_rest(switch, ["left_trigger", "left_con", "left_analog"])
        screen, t = get_objs_by_ids_rest(switch, ["screen", "screen_border", "bezels", "lower_bezel"])
        right_con = get_obj_by_id(switch, "right_con")
        left_con = VGroup(*left_con)
        print(len(screen))
        screen = VGroup(*screen)
        for i in left_con:
            i.z_index = 2
        right_con.z_index = 2
        self.play(
            ApplyMethod(left_con.shift, UP),
            ApplyMethod(right_con.shift, UP),
        )
        self.play(Transform(screen, switch_pro))
        self.play(
            ApplyMethod(left_con.move_to, ORIGIN + .7 * LEFT),
            ApplyMethod(right_con.move_to, ORIGIN + .7 * RIGHT),
        )
        #self.play()
        #self.play(ReplacementTransform(xbox, ps2))
        # self.play(ReplacementTransform(ps2, nes))
        self.wait()

class TestZIndex(Scene):

    def construct(self):
        ps4 = SVGMobject(ASSETS_PATH + "n64.svg").scale(2)
        self.play(ShowCreation(ps4))
        self.wait()


class ControllerEvolution(MovingCameraScene):

    def construct(self):
        self.nes_snes()
        self.snes_ps1()
        self.ps1_n64()

    def nes_snes(self):
        self.nes = SVGMobject(ASSETS_PATH + "nes.svg")
        self.snes = SVGMobject(ASSETS_PATH + "snes.svg")
        a_button, rest = get_objs_by_ids_rest(self.nes, ["a_button", "a"])
        b_button, red = get_objs_by_ids_rest(self.nes, ["b_button", "b"])
        a_button = VGroup(*a_button)
        for i in a_button: i.z_index = 3
        b_button = VGroup(*b_button)
        for i in b_button: i.z_index = 3
        dpad, rest = get_objs_by_ids_rest(self.nes, ["dpad", "dpad_outter", "dpad_center"])
        dpad = VGroup(*dpad)
        for i in dpad: i.z_index = 3
        dpad_snes = get_obj_by_id(self.snes, "dpad")
        dpad_snes.z_index = 3
        red = get_obj_by_id(self.snes, "red")
        red.z_index = 3
        green = get_obj_by_id(self.snes, "green")
        green.z_index = 3
        start = get_obj_by_id(self.nes, "start")
        start.z_index = 3
        select = get_obj_by_id(self.nes, "select")
        select.z_index = 3
        ss = VGroup(start, select)
        start_s = get_obj_by_id(self.snes, "start_select")
        start_s.z_index = 3
        temp, body_nes = get_objs_by_ids_rest(self.nes, ["a_button", "a", "b", "b_button",
                                                   "dpad", "dpad_outter", "dpad_center",
                                                   "start", "select"])
        temp, body_snes = get_objs_by_ids_rest(self.snes, [
            "dpad", "green", "red", "start_select"
        ])
        self.play(
            DrawBorderThenFill(self.nes)
        )
        self.wait(.2)
        self.play(
            ReplacementTransform(
                body_nes,
                body_snes
            ),
            LaggedStart(
                ReplacementTransform(
                    a_button,
                    red
                ),
                ReplacementTransform(
                    b_button,
                    green
                ),
                ReplacementTransform(
                    dpad,
                    dpad_snes
                ),
                ReplacementTransform(
                    start,
                    start_s
                ),
                ReplacementTransform(
                    ss,
                    start_s
                ),
           ),
            rate_func=slow_into,

        )

    def snes_ps1(self):
        self.ps1 = SVGMobject(ASSETS_PATH + "ps1")
        snes_dpad = ["dpad_circle", "dpad"]
        snes_buttons = ["red", "green", "blue","yellow"]
        ps1_dpad = ["up", "right", "down", "left"]
        ps1_buttons = ["triangle", "circle", "cross", "square"]
        snes_ss = ["start_select"]
        ps1_ss = ["start", "select"]
        snes_triggers = ["triggers"]
        ps1_triggers = ["left_trigger", "right_trigger"]

        snes_buttons_obj, rest = get_objs_by_ids_rest(self.snes, snes_buttons)
        snes_dpad_obj, rest = get_objs_by_ids_rest(self.snes, snes_dpad)
        ps1_dpad_obj, rest = get_objs_by_ids_rest(self.ps1, ps1_dpad)
        ps1_buttons_obj, rest = get_objs_by_ids_rest(self.ps1, ps1_buttons)
        snes_ss_obj, rest = get_objs_by_ids_rest(self.snes, snes_ss)
        snes_triggers_obj, rest = get_objs_by_ids_rest(self.snes, snes_triggers)
        ps1_ss_obj, rest = get_objs_by_ids_rest(self.ps1, ps1_ss)
        ps1_triggers_obj, rest = get_objs_by_ids_rest(self.ps1, ps1_triggers)

        temp, snes_body = get_objs_by_ids_rest(
            self.snes,
            snes_dpad+snes_buttons+snes_ss+snes_triggers
        )
        temp, ps1_body = get_objs_by_ids_rest(
            self.ps1,
            ps1_dpad + ps1_buttons + ps1_ss + ps1_triggers
        )
        for i in ps1_body: i.z_index=-1
        self.play(
            ShrinkToCenter(snes_body),
            LaggedStart(*[
                ReplacementTransform(i, j)
                for i,j in [(snes_buttons_obj, ps1_buttons_obj),
                            (snes_dpad_obj, ps1_dpad_obj),
                            (snes_ss_obj, ps1_ss_obj),
                            (snes_triggers_obj, ps1_triggers_obj)
                            ]
                ],
                rate_func=rush_into,
            ),
            GrowFromCenter(ps1_body, rate_func=slow_into, run_time=.5),
        )
        self.wait()

    def ps1_n64(self):
        self.n64 = SVGMobject(ASSETS_PATH + "n64.svg")
        self.play(ReplacementTransform(self.ps1, self.n64), run_time=1, rate_func=rush_from)
        self.wait()
