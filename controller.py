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
    objs = []
    rest = VGroup()
    for i in obj.submobjects:
        if i.id not in ids:
            rest.add(i)

    for i in ids:
        found = False
        for subm in obj.submobjects:
            if subm.id == i:
                print("found", i)
                objs.append(subm)
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
        snes = SVGMobject(ASSETS_PATH + "xbox-one.svg")
        ps4 = SVGMobject(ASSETS_PATH + "ps2.svg")
        self.play(ShowCreation(snes))
        self.play(Transform(snes, ps4))
        self.wait()