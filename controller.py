from manim import *
import os
ASSETS_PATH = os.getcwd() + "/assets/"


def easeInOutCubic(x):
    from math import pow
    if x < .5:
        return 4 * x * x * x
    else:
        return 1 - pow(-2 * x + 2, 3) / 2

def get_obj_by_id(obj, id):
    for i in obj.submobjects:
        if i.id == id:
            print("found", i)
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


class Clipping(Scene):

    def construct(self):
        for i in range(100):
            x = (np.random.rand() -.5) * 14
            y = (np.random.rand() - .5) * 7.6
            scale = np.random.rand() * .7
            obj = Dot(color=WHITE).scale(scale)
            obj.set_x(x)
            obj.set_y(y)
            self.add(obj)

        c = Circle(fill_opacity=1, fill_color=BLACK)
        c.z_index = -1
        self.play(c.animate.shift(3 * RIGHT))
        self.wait()

class Space(Scene):

    def construct(self):
        f = SVGMobject(ASSETS_PATH + "result.svg").scale(4)
        self.play(
            ShowCreation(f)
        )