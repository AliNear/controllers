# Author Grib ALI
# From nes to ps3, all in one class
# Not a good design decision
# From ps4, every transition on it's own scene.


from manim import *
import os

from manim.utils.rate_functions import ease_in_circ, ease_in_expo

ASSETS_PATH = os.getcwd() + "/assets/"


def easeInOutCubic(x):
    from math import pow
    if x < .5:
        return 4 * x * x * x
    else:
        return 1 - pow(-2 * x + 2, 3) / 2

def get_obj_by_id(obj: VMobject, index: str) -> VMobject:
    for i in obj.submobjects:
        if i.id == index:
            print("found", i.id)
            return i
    return None

def get_objs_by_ids_rest(obj, ids):
    """
    This function gets all objects by id in ids
    and the rest as a VGroup
    Returns tuple(objs_by_ids, VGroup rest)
    """
    objs = VGroup()
    rest = VGroup()
    for i in obj.submobjects:
        if i.id not in ids:
            rest.add(i)

    for i in ids:
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
        for subm in obj.submobjects:
            if subm.id == i:
                print("found", i)
                objs.add(subm)
                break

    return objs


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
        self.xbox360_ps3()
        self.ps3_ps4()

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
        for i in body_nes:
            i.z_index =- 1
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
        for i in self.ps2:i.set_stroke(width=.1)
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
        for i in self.ps2_body:
            if i.id != "body":
                i.z_index = -1
            else:
                i.z_index = -3

        temp, self.n64_body = get_objs_by_ids_rest(
            self.n64,
            self.ps1_triggers+self.n64_buttons+["dpad"]+handles
        )

        for i in self.n64_body: i.z_index=-1
        for i in n64_handles: i.z_index = -2
        for i in ps2_handles: i.z_index = -2



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
        for i in self.ps2_body:
            i.z_index = -1

        rest, self.xbox_body = get_objs_by_ids_rest(
            self.xbox,
            self.xbox_button+self.analogs+self.xbox_letters+self.ps1_dpad
        )
        for i in self.xbox_body:
            i.z_index = -1

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
        self.xbox360 = SVGMobject(ASSETS_PATH + "xbox360.svg")
        for i in self.xbox360.submobjects: i.set_stroke(color=BLACK, width=.1)
        self.play(
            FadeTransformPieces(self.wii, self.xbox360)
        )
        self.wait(.3)

    def xbox360_ps3(self):
        self.ps3 = SVGMobject(ASSETS_PATH + "ps3.svg")
        for i in self.xbox360.submobjects: i.set_stroke(color=BLACK, width=.1)
        for i in self.ps3.submobjects: i.set_stroke(color=BLACK, width=.1)

        #directions for the animation
        directions = [UP, UP, UP+.2*RIGHT, RIGHT, DOWN, UL, UR, UL, DL]

        #objects to retreive from the xbox controller
        triggers = get_objs_by_ids(self.xbox360, self.ps1_triggers)
        buttons = [[f"{i}_button", i] for i in "ybax"]
        buttons_obj = []
        for i in buttons:
            button = get_objs_by_ids(self.xbox360, i)
            buttons_obj.append(button)
        start_back = [[f"{i}_rect", i] for i in ["start", "back"]]
        start_back_obj = []
        for i in start_back:
            s = get_objs_by_ids(self.xbox360, i)
            start_back_obj.append(s)

        dpad =  ["dpad", "dpad_inner"]
        dpad_obj = get_objs_by_ids(self.xbox360, dpad)

        xbox_objs = [*triggers, *buttons_obj, *start_back_obj, dpad_obj]

        sb = [*start_back[0], *start_back[1]] #flattened version of start_back
        rest, xbox_body = get_objs_by_ids_rest(
            self.xbox360,
            self.ps1_triggers+buttons+sb+dpad
        )

        #ps3 objects
        buttons_ps3 = [[f"{i}_button", i] for i in ["triangle", "circle", "cross", "square"]]
        buttons_ps3_obj = []
        for i in buttons_ps3:
            button = get_objs_by_ids(self.ps3, i)
            buttons_ps3_obj.append(button)

        triggers_ps3 = get_objs_by_ids(self.ps3, self.ps1_triggers)
        ss_ps3 = ["start", "select"]
        ss_ps3_obj = [*get_objs_by_ids(self.ps3, ss_ps3)]
        dpad_ps3 = ["up", "right", "down", "left"]
        dpad_ps3_obj = get_objs_by_ids(self.ps3, dpad_ps3)

        ps3_objs = [*triggers_ps3, *buttons_ps3_obj, *ss_ps3_obj, dpad_ps3_obj]
        #flatten the buttons_ps3
        bps3 = []
        for i in buttons_ps3:
            bps3.append(i[0])
            bps3.append(i[1])

        rest, ps3_body = get_objs_by_ids_rest(
            self.ps3,
            self.ps1_triggers+bps3+ss_ps3+dpad_ps3
        )
        for i in triggers_ps3: i.z_index = -2
        for i in triggers: i.z_index = -2
        for i in ps3_body: i.z_index = 0






        def updater_handles(direction):
            def updater(obj, dt):
                value = dt
                speed = 4
                rot_speed = 3
                obj.shift(value * speed * direction)
                obj.rotate(value * rot_speed * PI)
            return updater

        for index, obj in enumerate(xbox_objs):
            obj.clear_updaters()
            obj.add_updater(updater_handles(directions[index]))

        self.play(
            *[
                i.animate.update()
                for i in xbox_objs
            ]
        )
        for i in xbox_objs: i.clear_updaters()
        self.play(
            FadeTransformPieces(xbox_body, ps3_body)
        )
        self.play(
            LaggedStart(*[
                Transform(i, j)
                for i,j in zip(xbox_objs, ps3_objs)
            ]),
            rate_func=rush_into
        )
        self.pss = ps3_objs

        self.wait(.3)

    def ps3_ps4(self):
        self.ps3_2 = SVGMobject(ASSETS_PATH + "ps3.svg")
        for i in self.ps3_2.submobjects: i.set_stroke(color=BLACK, width=.1)
        self.ps4 = SVGMobject(ASSETS_PATH + "ps4.svg")
        t1 = 1
        self.current = 0
        self.direction = DOWN

        def updater(obj, dt):
            self.current += dt

            if self.current >= t1:
                self.direction = UP
                self.current = 0
            alpha = easeInOutCubic(self.current) * .2
            obj.shift(alpha * self.direction)

        self.ps3_2.add_updater(updater)
        self.add(self.ps3_2)
        self.remove(self.ps3, *self.pss, self.xbox360)
        self.wait(1.3)
        self.play(
            FadeTransformPieces(self.ps3_2, self.ps4)
        )


class Test(Scene):

    def construct(self):
        #diff between buttons coors (ps4 & ps3)
        self.x_bias = 0.11373310005032339
        self.y_bias = 0.23616817231530646
        self.ps3 = SVGMobject(ASSETS_PATH + "ps3.svg")
        self.ps4 = SVGMobject(ASSETS_PATH + "ps4.svg")
        for i in self.ps3.submobjects: i.set_stroke(color=BLACK, width=.1)

        body_ps4 = get_obj_by_id(self.ps4, "body")
        #body_ps4.z_index = -1
        body_ps3 = get_objs_by_ids(
            self.ps3,
            [
                "body_center", "body_center_inner", "dpad_holder",
                "right_trigger_holder", "left_trigger_holder",
                "right_handle", "left_handle", "buttons_holder",
                "dpad_cross", "buttons_cross"
            ]
        )
        #for i in body_ps3: i.z_index = -1

        self.ps4.set_y(-self.y_bias)
        self.ps4.set_x(-self.x_bias)

        #self.play(FadeIn(self.ps4))
        self.ps3.animate.match_width(self.ps4)
        #self.ps3.scale(4)
        #self.ps4.scale(4)
        self.play(FadeIn(self.ps3))
        animations = []
        transforms = []
        for i in ("cross", "triangle", "square", "circle"):
            #button: the cirle
            #shape: cross, triangle, etc...
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

        buttons_cross = get_obj_by_id(self.ps3, "buttons_cross")
        dpad_cross = get_obj_by_id(self.ps3, "dpad_cross")
        dpad = get_obj_by_id(self.ps4, "arrows")
        dpad_ps3 = get_objs_by_ids(self.ps3, ["up", "down", "left", "right"])
        print(dpad.get_x()-dpad_cross.get_x())
        holders_ps3 = get_objs_by_ids(self.ps3, ["buttons_holder", "dpad_holder"])
        holders_ps4 = get_objs_by_ids(self.ps4, ["left_circle", "right_circle"])
        self.play(
            ShrinkToCenter(buttons_cross),
            ShrinkToCenter(dpad_cross),
        )
        self.play(*[
            i.animate.match_style(j)
            for i,j in zip(holders_ps3, holders_ps4)
        ])
        self.play(
            LaggedStart(*animations),
            LaggedStart(*transforms),
            rate_fun=rush_into
        )
        self.play(FadeTransformPieces(dpad_ps3, dpad))




    def show_diff(self):
        x_sum = 0
        y_sum = 0
        for i in ("cross", "triangle", "square", "circle"):
            cross_ps3 = get_obj_by_id(self.ps3, f"{i}_button")
            cross_ps4 = get_obj_by_id(self.ps4, f"{i}_button")

            x_diff = cross_ps4.get_x()-cross_ps3.get_x()
            y_diff = cross_ps4.get_y()-cross_ps3.get_y()
            x_sum += x_diff
            y_sum += y_diff
            #print("Y Diff", y_diff)
            #print("X Diff", x_diff)

        print("Average x diff", x_sum/4)
        print("Average y diff", y_sum/4)

        self.wait(.3)


class ControllerPS3ToPS4(Scene):
    # TODO:
    # Add Triggers

    def construct(self):
        self.ps3 = SVGMobject(ASSETS_PATH + "ps3.svg")
        for i in self.ps3.submobjects:
            i.set_stroke(width=.5)
        self.ps4 = SVGMobject(ASSETS_PATH + "ps4_2.svg")
        self.add(self.ps3)
        l = Line(
            UP,
            DOWN,
            color=BLACK,
            stroke_width=.8,
        )
        l.z_index = -9
        lines_coors = [
            (-2, 1), (-1.5, 3.5),
            (2.7, 1),(3, .5),
            (1,4), (-2, -1) 
        ]
        arrays = [
            np.array([x, y, 0])
            for x, y in lines_coors
        ]
        lines = VGroup(*[
            l.copy().shift(i)
            for i in arrays
        ])
        for i in lines:
            i.z_index = -9


        """getting the buttons"""
        buttons_ps3 = VGroup()
        shapes_ps3 = VGroup()
        buttons_ps4 = VGroup()
        shapes_ps4 = VGroup()
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

            buttons_ps3.add(button_ps3)
            buttons_ps4.add(button_ps4)
            shapes_ps3.add(shape_ps3)
            shapes_ps4.add(shape_ps4)
        dpad_ps3 = get_objs_by_ids(self.ps3, ["up", "down", "left", "right"])
        analogs = ["_analog_base", "_analog", "_analog_inner"]
        left_analog = ["left"+i for i in analogs]
        right_analog = ["right"+i for i in analogs]


        analogs_ps3 = get_objs_by_ids(self.ps3,
                                      left_analog+right_analog)
        analogs_ps4 = get_objs_by_ids(self.ps4,
                                      left_analog+right_analog)
        # Bodies
        left_handle = get_obj_by_id(self.ps3, "left_handle")
        right_handle = get_obj_by_id(self.ps3, "right_handle")
        left_handle_4 = get_obj_by_id(self.ps4, "left_handle")
        right_handle_4 = get_obj_by_id(self.ps4, "right_handle")

        body_ps4 = get_obj_by_id(self.ps4, "body_center")
        body_ps3 = get_objs_by_ids(self.ps3, [
            "body_center",
            "body_center_inner",
        ])
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

        dpad_ps4 = get_obj_by_id(self.ps4, "arrows")
        logo = ["ps_logo_bg", "ps_logo"]
        logo_ps3 = get_objs_by_ids(self.ps3, logo)
        logo_ps3.z_index = 4
        logo_ps4 = get_objs_by_ids(self.ps4, logo)
        lights = [f"light_{i}" for i in range(1, 5)]
        lights_ps3 = get_objs_by_ids(self.ps3, lights)
        trackpad = get_obj_by_id(self.ps4, "trackpad")
        trackpad.z_index = 4
        mic = get_obj_by_id(self.ps4, "mic")
        mic.z_index = 4
        right_extreme = get_obj_by_id(self.ps4, "right_extreme")
        left_extreme = get_obj_by_id(self.ps4, "left_extreme")
        right_extreme.z_index = 4
        left_extreme.z_index = 4

        buttons_flight = AnimationGroup(
            LaggedStart(*[
                ShowPassingFlash(i, time_width=.3, rate_func=linear)
                for i in lines
            ],
            lag_ratio=.4
            ),
            # WiggleOutThenIn(img, rotation_angle=0.01*.5*TAU,scale_value=1, n_wiggles=20, rate_func=linear)
            buttons_ps3.animate.shift(1.5*UP),
            shapes_ps3.animate.shift(1.5*UP),
            dpad_ps3.animate.shift(1.5*UP),
            analogs_ps3.animate.shift(1.5*UP),
            ss.animate.shift(1.5*UP),
            logo_ps3.animate.shift(1.5*UP),
            rate_func=linear,
            run_time=1
        )


        text_lights_fading = AnimationGroup(
            LaggedStart(*[
                ShrinkToCenter(i)
                for i in [*lights_ps3, *ss_text]
            ]),
            rate_func=linear,
        )

        self.play(
            LaggedStart(
                buttons_flight,
                text_lights_fading,
                lag_ratio=.5
            )
        )

        transforms_body = AnimationGroup(
            FadeTransform(left_handle, left_handle_4),
            FadeTransform(right_handle, right_handle_4),
            FadeTransform(body_ps3, body_ps4),
            rate_func=linear,
            run_time=.7
 
        )
        transforms_buttons = AnimationGroup(
            LaggedStart(
                LaggedStart(*[
                    Transform(i, j)
                    for i, j in zip(buttons_ps3, buttons_ps4)
                ]),
                LaggedStart(*[
                    Transform(i, j)
                    for i, j in zip(shapes_ps3, shapes_ps4)
                ]),
                lag_ratio=1
            ),
            FadeTransformPieces(dpad_ps3, dpad_ps4),
            FadeTransform(ss[0], sm[1]),
            FadeTransform(ss[1], sm[0]),
            FadeTransform(analogs_ps3, analogs_ps4),
            logo_ps3.animate.move_to(logo_ps4)
        )
        self.play(
            LaggedStart(
                transforms_body,
                transforms_buttons,
                lag_ratio=.5
            )
        )
        for i in lines:
            i.rotate(180 * DEGREES)

        trackpad.shift(5*UP)
        # right and left coefficient
        rl_coeff = 1
        # down coefficient
        d_coeff = 4

        self.play(
            LaggedStart(
                GrowFromCenter(mic),
                FadeInFrom(right_extreme, rl_coeff * RIGHT + d_coeff * DOWN),
                FadeInFrom(left_extreme, rl_coeff * LEFT + d_coeff * DOWN),
            )
        )
        self.play(
            LaggedStart(*[
                ShowPassingFlash(i, time_width=.3, rate_func=linear)
                for i in lines
            ],
            lag_ratio=.3
            ),
            trackpad.animate.shift(5*DOWN),
            rate_func=linear
        )


class ControllerPS4ToXboxOne(Scene):
    """
    Transition PS4 -> Xbox One
    """
    
    def construct(self):
        self.prepare()
        self.start_animation()

    def prepare(self):
        self.ps4 = SVGMobject(ASSETS_PATH + "ps4_2.svg")
        self.xbox1 = SVGMobject(ASSETS_PATH + "xbox_one.svg")
        self.ps4_body, self.ps4_rest = get_objs_by_ids_rest(
            self.ps4,[
                "body_center",
                "left_handle",
                "right_handle",
                "right_trigger",
                "left_trigger",
                "trackpad",
                "left_analog_base",
                "right_analog_base"
            ]
        )

        self.ps4_color = "#222629"

        # Xbox One defs
        self.xbox1_body = get_obj_by_id(self.xbox1, "body")
        self.xbox1_upper = get_obj_by_id(self.xbox1, "upper_side")
        self.xbox1_logo = get_obj_by_id(self.xbox1, "logo")
        self.xbox1_triggers = get_obj_by_id(self.xbox1, "triggers")
        self.xbox1_buttons = VGroup()
        self.xbox1_letters = VGroup()
        for i in list("xyba"):
            button = get_obj_by_id(self.xbox1, f"{i}_button")
            letter = get_obj_by_id(self.xbox1, i)
            self.xbox1_buttons.add(button)
            self.xbox1_letters.add(letter)

        self.xbox1_view = get_objs_by_ids(self.xbox1, ["view", "view_icon"])
        self.xbox1_menu = get_objs_by_ids(self.xbox1, ["menu", "menu_icon"])
        self.xbox1_dpad = get_objs_by_ids(self.xbox1, ["dpad", "dpad_holder"])
        analog = ["analog_base", "analog_outter", "analog", "analog_inner"]
        left_analogs = ["left_"+i for i in analog]
        right_analogs = ["right_"+i for i in analog]
        self.xbox1_left_analog = get_objs_by_ids(self.xbox1, left_analogs)
        self.xbox1_right_analog = get_objs_by_ids(self.xbox1, right_analogs)

    def start_animation(self):
        self.add(self.ps4)
        self.play(
            self.ps4.animate.set_color(self.ps4_color),
            run_time=.5
        )
        self.remove(*self.ps4_rest)
        self.wait(.1)
        self.play(
            ClockwiseTransform(self.ps4_body, self.xbox1_body),
            rate_func=ease_in_circ,
            run_time=.7
        )
        self.play(
            LaggedStart(
                DrawBorderThenFill(self.xbox1_upper), #run_time=.8),
                FadeInFrom(self.xbox1_triggers, UP),
                GrowFromCenter(self.xbox1_logo),
                lag_ratio=.25
            )
        )
        self.play(
            LaggedStart(
                LaggedStart(*[
                    GrowFromCenter(i)
                    for i in self.xbox1_buttons
                ]),
                LaggedStart(*[
                    DrawBorderThenFill(i, run_time=.7)
                    for i in self.xbox1_letters
                ]),
                LaggedStart(
                    GrowFromCenter(self.xbox1_menu[0]),
                    FadeIn(self.xbox1_menu[1]),
                    GrowFromCenter(self.xbox1_view[0]),
                    FadeIn(self.xbox1_view[1]),
                    lag_ratio=.2
                ),
                LaggedStart(
                    LaggedStart(*[
                        GrowFromCenter(i)
                        for i in self.xbox1_right_analog
                    ]),
                    LaggedStart(*[
                        GrowFromCenter(i)
                        for i in self.xbox1_left_analog
                    ]),
                    LaggedStart(
                        GrowFromCenter(self.xbox1_dpad[1]),
                        DrawBorderThenFill(self.xbox1_dpad[0], run_time=.6),
                    ),
                    lag_ratio=.4
                ), 
                lag_ratio=.4
            )
        )
        self.wait(.1)


class ControllerXboxOneSwitch(Scene):

    def construct(self):
        self.prepare()
        self.start_animations()

    def prepare(self):
        self.xbox1 = SVGMobject(ASSETS_PATH + "xbox_one.svg")
        self.switch = SVGMobject(ASSETS_PATH + "switch.svg")
        self.right_con = get_obj_by_id(self.switch, "right_con")
        self.left_con = get_obj_by_id(self.switch, "left_con")
        self.body = get_objs_by_ids(self.switch, [
            "screen_border",
            "bezels",
            "screen"
        ])

        left_x = self.left_con.get_edge_center(RIGHT)[0] * RIGHT
        right_x = self.right_con.get_edge_center(LEFT)[0] * RIGHT

        self.left_rect = Polygon(
            left_x + 4 * UP,
            left_x + 4 * DOWN,
            (left_x + 4 * DOWN) + 6 * LEFT,
            (left_x + 4 * UP) + 6 * LEFT,
            fill_color="#01bbe2",
            fill_opacity=1,
            stroke_width=0
        )

        self.right_rect = Polygon(
            right_x + 4 * UP,
            right_x + 4 * DOWN,
            (right_x + 4 * DOWN) - 6 * LEFT,
            (right_x + 4 * UP) - 6 * LEFT,
            fill_color="#fe5d53",
            fill_opacity=1,
            stroke_width=0
        )

        self.center_rect = Polygon(
            right_x + 4 * UP,
            right_x + 4 * DOWN,
            left_x + 4 * DOWN,
            left_x + 4 * UP,
            fill_color="#606062",
            fill_opacity=1,
            stroke_width=0
        )



    def start_animations(self):
        self.add(self.xbox1)
        self.play(
            FadeInFrom(self.left_rect, 7 * UP),
            FadeInFrom(self.right_rect, 7 * DOWN),
            FadeIn(self.center_rect)
        )
        self.remove(self.xbox1)
        self.wait(.1)
        self.play(
            Transform(self.left_rect, self.left_con),
            Transform(self.right_rect, self.right_con),
            Transform(self.center_rect, self.body),
        )

        self.wait(.2)