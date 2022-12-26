"""
UNET ANIMATION USING MANIM
The animation is for showing the creation of a standard U-Net network using manim .
The animation was made in ManimCE v0.16.0 (Manim Community Edition).
Not the most efficient code, but gets the work done :) Definitely better and effiend ways to render but I only made it after a week of using Manim so :shrugs:
Help and tips were taken from several places as below:

Manim Community Edition: https://www.manim.community
Manim Community documentation: https://docs.manim.community/en/stable/tutorials/quickstart.html
Theorem of Beethoven: https://www.youtube.com/c/TheoremofBeethoven
"""


from pathlib import Path

from manim import *

# pql for faster 480p 15fps renders
# FLAGS = f"-pqh"
FLAGS = f"--format=gif"
SCENE = "unet"      # <- Name of the class to render


# Scene background colour .. similar to the presentation background to make the animation fit seamlessly on the slide
config.background_color = "#262626"
class unet(Scene):
    def construct(self):

        ## Uncomment and generate for debugging the placement of the layers.
        # ax = NumberPlane(
        #     background_line_style={
        #         "stroke_color": TEAL,
        #         "stroke_width": 0.5,
        #         "stroke_opacity": 0.6
        #     })
        # self.add(ax)

        # creating the network
        input_img = Rectangle(color = WHITE, width=0.5, height=3, grid_xstep=(0.5/4), grid_ystep=0.15)
        d1 = Rectangle(width = 0.15, height = 3.00, stroke_color=GREY_E).set_fill(PURPLE_A, opacity=1.0)
        d2 = Rectangle(width = 0.75, height = 1.50, stroke_color=GREY_E).set_fill(PURPLE_B, opacity=1.0)
        d3 = Rectangle(width = 1.00, height = 0.75, stroke_color=GREY_E).set_fill(PURPLE_C, opacity=1.0)
        d4 = Rectangle(width = 1.00, height = 0.25, stroke_color=GREY_E).set_fill(PURPLE_D, opacity=1.0)
        residual = Rectangle(width = 1.50, height = 0.17, stroke_color=GREY_E).set_fill(ORANGE, opacity=1.0)
        u1 = Rectangle(width = 0.15, height = 3.00, stroke_color=GREY_E).set_fill(GREEN_A, opacity=1.0)
        u2 = Rectangle(width = 0.75, height = 1.50, stroke_color=GREY_E).set_fill(GREEN_B, opacity=1.0)
        u3 = Rectangle(width = 1.00, height = 0.75, stroke_color=GREY_E).set_fill(GREEN_C, opacity=1.0)
        u4 = Rectangle(width = 1.00, height = 0.25, stroke_color=GREY_E).set_fill(GREEN_D, opacity=1.0)
        output_img = Rectangle(color = WHITE, width=0.15, height=3, grid_xstep=0.15, grid_ystep=0.15)

        input_img.move_to( LEFT * 5 ).shift( UP * 2)
        d1.move_to( LEFT * 4).shift(UP * 2 )
        d2.move_to( LEFT * 3).shift(UP * 0 )
        d3.move_to( LEFT * 2).shift(DOWN * 2 )
        d4.move_to( LEFT * 1).shift(DOWN * 3 )
        residual.move_to( LEFT * 0).shift(DOWN * 3.5 )
        u1.move_to( RIGHT * 4).shift(UP * 2 )
        u2.move_to( RIGHT * 3).shift(UP * 0 )
        u3.move_to( RIGHT * 2).shift(DOWN * 2 )
        u4.move_to( RIGHT * 1).shift(DOWN * 3 )
        output_img.move_to( RIGHT * 5 ).shift( UP * 2)

        t1 = Text("Input batch", font_size=12).next_to(input_img, DOWN)
        t2 = Text("Output image", font_size=12).next_to(output_img, DOWN)

        #  lines for encoder
        p1  = [-4, 0.50,0]; p2  = [-4, 0.0,0]; p3    = [-3.5, 0, 0]           # Between d1 and d2
        p4  = [-3,-0.75,0]; p5  = [-3,-2.0,0]; p6    = [-2.5, -2, 0]          # Between d2 and d3
        p7  = [-2,-2.35,0]; p8  = [-2,-3.0,0]; p9    = [-1.5, -3, 0]          # Between d3 and d4
        p10 = [-1,-3.15,0]; p11 = [-1,-3.5,0]; p12 = [-0.75, -3.5, 0]  # Between d4 and d5
        l1_e = Line(p1,p2).append_points(Line(p2,p3).points)
        l2_e = Line(p4,p5).append_points(Line(p5,p6).points)
        l3_e = Line(p7,p8).append_points(Line(p8,p9).points)
        l4_e = Line(p10,p11).append_points(Line(p11,p12).points)

        #  lines for decoder
        p1_d  = [4, 0.50,0]; p2_d  = [4, 0.0,0]; p3_d    = [3.5, 0, 0]           # Between d1 and d2
        p4_d  = [3,-0.75,0]; p5_d  = [3,-2.0,0]; p6_d    = [2.5, -2, 0]          # Between d2 and d3
        p7_d  = [2,-2.35,0]; p8_d  = [2,-3.0,0]; p9_d    = [1.5, -3, 0]          # Between d3 and d4
        p10_d = [1,-3.15,0]; p11_d = [1,-3.5,0]; p12_d = [0.75, -3.5, 0]  # Between d4 and d5
        l1_d = Line(p1_d,p2_d).append_points(Line(p2_d,p3_d).points)
        l2_d = Line(p4_d,p5_d).append_points(Line(p5_d,p6_d).points)
        l3_d = Line(p7_d,p8_d).append_points(Line(p8_d,p9_d).points)
        l4_d = Line(p10_d,p11_d).append_points(Line(p11_d,p12_d).points)

        conna = Arrow(start=input_img.get_edge_center(RIGHT), end=d1.get_edge_center(LEFT), color=GOLD, stroke_width=0.5, max_tip_length_to_length_ratio=0.10)
        connb = Arrow(start=u1.get_edge_center(RIGHT), end=output_img.get_edge_center(LEFT), color=GOLD, stroke_width=0.5, max_tip_length_to_length_ratio=0.10)
        conn1 = Arrow(start=d1.get_edge_center(RIGHT), end=u1.get_edge_center(LEFT), color=GOLD, stroke_width=0.5, max_tip_length_to_length_ratio=0.10)
        conn2 = Arrow(start=d2.get_edge_center(RIGHT), end=u2.get_edge_center(LEFT), color=GOLD, stroke_width=0.5, max_tip_length_to_length_ratio=0.10)
        conn3 = Arrow(start=d3.get_edge_center(RIGHT), end=u3.get_edge_center(LEFT), color=GOLD, stroke_width=0.5, max_tip_length_to_length_ratio=0.10)
        conn4 = Arrow(start=d4.get_edge_center(RIGHT), end=u4.get_edge_center(LEFT), color=GOLD, stroke_width=0.5, max_tip_length_to_length_ratio=0.10)

        maxpool = Text("Maxpool \n Dropout, ReLU", font_size=12)
        maxpool1 = maxpool.copy().scale(0.6).next_to(l1_e, DOWN)
        maxpool2 = maxpool.copy().scale(0.6).next_to(l2_e, DOWN)
        maxpool3 = maxpool.copy().scale(0.6).next_to(l3_e, DOWN)
        maxpool4 = maxpool.copy().scale(0.6).next_to(l4_e, DOWN)

        Conv2DTr = Text("Conv2DTr \n Dropout, ReLU", font_size=12)
        Conv2DTr1 = Conv2DTr.copy().scale(0.6).next_to(l1_d, DOWN)
        Conv2DTr2 = Conv2DTr.copy().scale(0.6).next_to(l2_d, DOWN)
        Conv2DTr3 = Conv2DTr.copy().scale(0.6).next_to(l3_d, DOWN)
        Conv2DTr4 = Conv2DTr.copy().scale(0.6).next_to(l4_d, DOWN)

        concat = Text("concatenate", font_size=12)
        concat1 = concat.copy().scale(0.6).next_to(conn1, UP)
        concat2 = concat.copy().scale(0.6).next_to(conn2, UP)
        concat3 = concat.copy().scale(0.6).next_to(conn3, UP)
        concat4 = concat.copy().scale(0.6).next_to(conn4, UP)

        #  RENDER
        self.add(input_img, t1, output_img, t2) # add both objects to the VGroup

        unet_complete = VGroup(d1, d2, d3, d4, residual, u4, u3, u2, u1, l1_e, l2_e, l3_e, l4_e, l1_d, l2_d, l3_d, l4_d, conn1, conn2, conn3, conn4, conna, connb, input_img, output_img, t1, t2, maxpool1, maxpool2, maxpool3, maxpool4, Conv2DTr1, Conv2DTr2, Conv2DTr3, Conv2DTr4, concat1, concat2, concat3, concat4 )

        self.play(Create(unet_complete), run_time = 5)
        self.wait()


if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")