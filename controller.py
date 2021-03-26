from manim import *

file = r"C:\Users\jm\Documents/ps2.svg"
path = "C:/Users/jm/Downloads/"
def test_func(x):
    return np.cos(x[0] * x[1])

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
                objs.append(subm)
                break
                
    return (objs, rest)

class Test(Scene):

    def construct(self):
        xbox = SVGMobject(path + "xbox_360.svg")
        xbox_fat = SVGMobject(path + "xbox_fat.svg")
        ps2 = SVGMobject(path + "ps2.svg")
        square_button_ = get_obj_by_id(ps2, "square_button")
        square_button_.set_stroke("#FF01DB", 3)
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
        """
        xbox_ids = ["a_button", "b_button", "x_button", "y_button", "right_analog", "left_analog"]
        ps2_ids = ["x_button", "circle_button", "square_button", "triangle_button", "right_analog", "left_analog"]
        xbox_obj, xbox_rest = get_objs_by_ids_rest(xbox, xbox_ids)
        ps2_obj, ps2_rest = get_objs_by_ids_rest(ps2, ps2_ids)
        self.play(ShowCreation(xbox_fat))
        """
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
        #self.play()
        #self.play(ReplacementTransform(xbox, ps2))
        # self.play(ReplacementTransform(ps2, nes))
        self.wait()


class Test3D(ThreeDScene):

    def construct(self):
        c = Cube()
        self.play(
            ShowCreation(c)
        )
        s = Sphere().set_x(-4)
        self.add(s)
        
        self.move_camera(phi=20*DEGREES)