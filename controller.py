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
        self.n64_ps2()
        self.ps2_xbox()
        self.xbox_gamecube()
        self.gamecube_wii()
        self.wii_xbox360()

    def nes_snes(self):
        self.nes = SVGMobject(ASSETS_PATH + "nes.svg")
        self.snes = SVGMobject(ASSETS_PATH + "snes.svg")
        a_button = get_objs_by_ids(self.nes, ["a_button", "a"])
        b_button = get_objs_by_ids(self.nes, ["b_button", "b"])
        dpad = get_objs_by_ids(self.nes, ["dpad", "dpad_outter", "dpad_center"])
        dpad_snes = get_obj_by_id(self.snes, "dpad")
        red = get_obj_by_id(self.snes, "red")
        green = get_obj_by_id(self.snes, "green")
        start = get_obj_by_id(self.nes, "start")
        select = get_obj_by_id(self.nes, "select")
        ss = VGroup(start, select)
        start_s = get_obj_by_id(self.snes, "start_select")
        temp, body_nes = get_objs_by_ids_rest(self.nes, ["a_button", "a", "b", "b_button",
                                                   "dpad", "dpad_outter", "dpad_center",
                                                   "start", "select"])
        temp, body_snes = get_objs_by_ids_rest(self.snes, [
            "dpad", "green", "red", "start_select"
        ])
        print(body_snes)
        self.play(
            DrawBorderThenFill(self.nes)
        )

        for i in body_nes: i.z_index=-1
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
        self.ps1_dpad = ["up", "right", "down", "left"]
        self.ps1_buttons = ["triangle", "circle", "cross", "square"]
        snes_ss = ["start_select"]
        ps1_ss = ["start", "select"]
        snes_triggers = ["triggers"]
        self.ps1_triggers = ["left_trigger", "right_trigger"]

        snes_buttons_obj = get_objs_by_ids(self.snes, snes_buttons)
        snes_dpad_obj = get_objs_by_ids(self.snes, snes_dpad)
        self.ps1_dpad_obj = get_objs_by_ids(self.ps1, self.ps1_dpad)
        self.ps1_buttons_obj = get_objs_by_ids(self.ps1, self.ps1_buttons)
        snes_ss_obj = get_objs_by_ids(self.snes, snes_ss)
        snes_triggers_obj = get_objs_by_ids(self.snes, snes_triggers)
        self.ps1_ss_obj = get_objs_by_ids(self.ps1, ps1_ss)
        self.ps1_triggers_obj = get_objs_by_ids(self.ps1, self.ps1_triggers)

        temp, snes_body = get_objs_by_ids_rest(
            self.snes,
            snes_dpad+snes_buttons+snes_ss+snes_triggers
        )
        temp, self.ps1_body = get_objs_by_ids_rest(
            self.ps1,
            self.ps1_dpad + self.ps1_buttons + ps1_ss + self.ps1_triggers
        )
        for i in self.ps1_body: i.z_index=-1
        self.play(
            ShrinkToCenter(snes_body),
            LaggedStart(*[
                ReplacementTransform(i, j)
                for i,j in [(snes_buttons_obj, self.ps1_buttons_obj),
                            (snes_dpad_obj, self.ps1_dpad_obj),
                            (snes_ss_obj, self.ps1_ss_obj),
                            (snes_triggers_obj, self.ps1_triggers_obj)
                            ]
                ],
                rate_func=rush_into,
            ),
            GrowFromCenter(self.ps1_body, rate_func=slow_into, run_time=.5),
        )

    def ps1_n64(self):
        self.n64 = SVGMobject(ASSETS_PATH + "n64.svg")
        for i in self.n64:i.set_stroke(width=.5)
        self.n64_buttons = [f"yellow_{i}" for i in range(1, 5)]
        self.rgb = ["red", "green", "blue"]
        self.rgb = [i + "_button" for i in self.rgb]
        self.n64_dpad = get_obj_by_id(self.n64, "dpad")
        triggers = self.ps1_triggers
        self.rgb_obj = get_objs_by_ids(self.n64, self.rgb)
        print(10 * "*", len(self.rgb_obj))
        self.red, self.green, self.blue = self.rgb_obj
        self.n64_buttons_obj = get_objs_by_ids(self.n64, self.n64_buttons)
        self.n64_triggers = get_objs_by_ids(self.n64, self.ps1_triggers)
        temp, self.n64_body = get_objs_by_ids_rest(
            self.n64,
            self.ps1_triggers + self.n64_buttons + ["dpad"] + self.rgb
        )

        for i in self.n64_body: i.z_index=-1
        self.play(
            ReplacementTransform(
                self.ps1_body, self.n64_body
            ),
            LaggedStart(
                *[
                    ReplacementTransform(i, j)
                    for i, j in zip(self.ps1_buttons_obj, self.n64_buttons_obj)
                ]
            ),
            ReplacementTransform(self.ps1_dpad_obj, self.n64_dpad),
            ReplacementTransform(self.ps1_triggers_obj, self.n64_triggers),
            FadeOut(self.ps1_ss_obj),
            rate_func = rush_into,
        )
        self.play(
            LaggedStart(*[
                GrowFromCenter(i)
                for i in self.rgb_obj
            ],lag_ratio=.4),
            rate_func = rush_into,
            run_time=.7
        )

    def n64_ps2(self):
        self.ps2 = SVGMobject(ASSETS_PATH + "ps2").scale(.8)
        for i in self.ps2:i.set_stroke(width=.5)
        handles = ["left_handle", "right_handle"]
        ps2_handles = get_objs_by_ids(self.ps2, handles)
        n64_handles = get_objs_by_ids(self.n64, handles)
        self.ps2_buttons = self.ps1_buttons
        self.ps2_buttons_shapes = [i + "_button" for i in self.ps2_buttons]
        self.ps2_buttons_obj = get_objs_by_ids(self.ps2, self.ps2_buttons)
        self.ps2_buttons_shapes_obj = get_objs_by_ids(self.ps2, self.ps2_buttons_shapes)
        self.ps2_dpad_obj = get_objs_by_ids(self.ps2, self.ps1_dpad)
        self.ps2_ssa = ["start", "select", "analog"]
        self.ps2_ssa_obj = get_objs_by_ids(self.ps2, self.ps2_ssa)
        self.ps2_triggers_obj = get_objs_by_ids(self.ps2, self.ps1_triggers)
        for i in self.ps2_triggers_obj: i.z_index=-2
        for i in self.n64_triggers: i.z_index=-2

        rest, self.ps2_body = get_objs_by_ids_rest(
            self.ps2,
            handles+self.ps2_buttons+self.ps2_buttons_shapes+
            self.ps2_ssa+self.ps1_triggers+self.ps1_dpad
        )
        for i in self.ps2_body: i.z_index=-1

        temp, self.n64_body = get_objs_by_ids_rest(
            self.n64,
            self.ps1_triggers+self.n64_buttons+["dpad"]+handles
        )

        for i in self.n64_body: i.z_index=-1



        self.play(
            ReplacementTransform(n64_handles, ps2_handles)
        )
        self.play(ReplacementTransform(self.n64_body, self.ps2_body))
        self.play(
            LaggedStart(*[
                ReplacementTransform(i, j)
                for i,j in [
                    (self.n64_dpad, self.ps2_dpad_obj),
                    (self.n64_buttons_obj, self.ps2_buttons_shapes_obj),
                    (self.n64_triggers, self.ps2_triggers_obj)
                ]
            ])
        )
        for i in self.ps2_buttons_obj:
            i.save_state()
            i.scale(10)
        self.play(
            LaggedStart(
                LaggedStart(*[
                    GrowFromCenter(i)
                    for i in self.ps2_ssa_obj
                ]),
                LaggedStart(*[
                    Succession(
                        FadeIn(i, run_time=.2),
                        Restore(i, run_time=.5)
                    )
                    for i in self.ps2_buttons_obj
                ], lag_ratio=.3),
                lag_ratio=1
            )
        )
        self.wait(.2)

    def ps2_xbox(self):
        self.xbox = SVGMobject(ASSETS_PATH + "xbox_fat.svg")
        for i in self.xbox: i.set_stroke(BLACK, width=.1)
        self.xbox_button = [
            "green", "yellow", "blue", "red"
        ]
        self.xbox_letters = list("abxy")
        self.analogs = ["left_analog", "right_analog"]
        self.xbox_button_obj = get_objs_by_ids(self.xbox, self.xbox_button)
        self.xbox_letters_obj = get_objs_by_ids(self.xbox, self.xbox_letters)
        self.xbox_analogs = get_objs_by_ids(self.xbox, self.analogs)
        self.xbox_dpad = get_objs_by_ids(self.xbox, "dpad")
        self.ps2_analogs = get_objs_by_ids(self.ps2, self.analogs)

        rest, self.ps2_body = get_objs_by_ids_rest(
            self.ps2,
            self.ps2_buttons+self.ps2_buttons_shapes+
            self.analogs+self.ps1_dpad
        )
        for i in self.ps2_body: i.z_index=-1

        rest, self.xbox_body = get_objs_by_ids_rest(
            self.xbox,
            self.xbox_button+self.analogs+self.xbox_letters+self.ps1_dpad
        )
        for i in self.xbox_body: i.z_index=-1

        self.play(
            ApplyMethod(self.ps2_buttons_obj.shift, 2 * UP, rate_func=rush_from),
            LaggedStart(
                ReplacementTransform(self.ps2_body, self.xbox_body),
                LaggedStart(*[
                    ReplacementTransform(i, j)
                    for i,j in [
                        (self.ps2_analogs, self.xbox_analogs),
                        (self.ps2_dpad_obj, self.xbox_dpad),
                        (self.ps2_buttons_shapes_obj, self.xbox_button_obj)
                    ]
                ]),
                lag_ratio=.6
            ),
            rate_func=rush_into
        )
        self.play(
            ReplacementTransform(self.ps2_buttons_obj, self.xbox_letters_obj),
            rate_func=rush_into
        )

        self.wait(.2)

    def xbox_gamecube(self):
        self.handles = ["left_handle", "right_handle"]
        self.gamecube = SVGMobject(ASSETS_PATH + "gamecube.svg")
        x_body, x_rest = get_objs_by_ids_rest(self.xbox, ["body", "upper_body"])
        g_body, g_rest = get_objs_by_ids_rest(self.gamecube,
                                          ["body"]+self.handles)
        self.g_triggers = get_objs_by_ids(self.gamecube, self.ps1_triggers)
        g_rest.remove(*self.g_triggers)
        for i in self.g_triggers: i.z_index == -2
        self.play(
            LaggedStart(*[
                ApplyMethod(i.shift, 5 * DOWN)
                for i in x_rest
            ], lag_ratio=.2),
            run_time=3
        )
        self.play(
            ApplyMethod(x_body.set_color, "#565E9E")
        )
        self.play(
            LaggedStart(
                FadeTransformPieces(x_body, g_body),
                FadeInFrom(self.g_triggers, 5 * UP),
                lag_ratio=.2
            )
        )
        self.play(
            LaggedStart(*[
                GrowFromCenter(i)
                for i in g_rest
            ], lag_ratio=.15),
            run_time=2
        )

        self.wait(.3)

    def gamecube_wii(self):
        self.wii = SVGMobject(ASSETS_PATH + "wii.svg")
        g_handles = get_objs_by_ids(self.gamecube, self.handles)
        right_buttons = get_objs_by_ids(self.gamecube,
                                   [f"{i}_button" for i in "abxy"]+list("abxy")+
                                   ["analog_base", "analog", "c"]
                                   )
        g_handles[1].add(right_buttons)
        left_buttons = get_objs_by_ids(self.gamecube,
                                       ["dpad", "left_analog_base", "left_analog"])
        g_handles[0].add(left_buttons)
        body = get_objs_by_ids(self.gamecube,
                               self.ps1_triggers+["right_trigger_thing", "body", "middle_button"])

        wii_body, buttons = get_objs_by_ids_rest(self.wii, ["body"])


        alpha = ValueTracker(0)

        def updater_handles(obj, dt):
            h1, h2 = obj
            value = dt
            speed = 4
            rot_speed = 3
            h1.shift(value * speed * UL)
            h2.shift(value * speed * DR)
            h1.rotate(value * rot_speed * PI)
            h2.rotate(value * rot_speed * PI)

        g_handles = g_handles.clear_updaters()
        g_handles.add_updater(updater_handles)


        self.play(
            Rotate(body, 90 * DEGREES),
            g_handles.animate.update()
        )
        g_handles.clear_updaters()
        self.remove(g_handles)
        self.play(
            LaggedStart(
                FadeTransformPieces(body, wii_body),
                LaggedStart(*[
                    GrowFromCenter(i)
                    for i in buttons
                ])
            )
        )

        self.wait(.3)

    def wii_xbox360(self):
        self.xbox360 = SVGMobject(ASSETS_PATH + "xbox_360.svg")
        self.play(
            FadeTransformPieces(self.wii, self.xbox360)
        )

