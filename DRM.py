"""
DICHROMATIC REFLECTION MODEL ANIMATION FOR SPECULAR REFLECTION
The animation is for showing the specularly reflected rays that are reflected from a surface after reflection.
The animation was made in ManimCE v0.16.0 (Manim Community Edition) in one (extended hours) weekend!
Not the most efficient code, but gets the work done :)
Help and tips were taken from several places as below:

Manim Community Edition: https://www.manim.community
Manim Community documentation: https://docs.manim.community/en/stable/tutorials/quickstart.html
Theorem of Beethoven: https://www.youtube.com/c/TheoremofBeethoven
"""

from math import gamma
from pathlib import Path

from manim import *

FLAGS = f"-pqh"
SCENE = "drm"      # <- Name of the class to render

# Scene background colour .. similar to the presentation background to make the animation fit seamlessly on the slide
config.background_color = "#262626"

class drm(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes(
            x_range=[-5, 5, 5],
            y_range=[-5, 5, 5],
            z_range=[-5, 5, 5],
            x_length=7,
            y_length=7,
            z_length=7,
        )
        r = ValueTracker(1)
        h = ValueTracker(1)

        axes = ThreeDAxes()
        self.set_camera_orientation( phi=90*DEGREES, theta=-90*DEGREES, focal_distance=6)

        incoming   = Arrow3D(start=np.array([-2, 0, 2]), end=np.array([0, 0, 0]), resolution=8 )
        outgoing   = Arrow3D(start=np.array([0, 0, 0]), end=np.array([2, 0, 2]), resolution=8 )
        outgoing_a = Arrow3D(start=np.array([0, 0, 0]), end=np.array([1, 0, 0.5]), resolution=8 )
        outgoing_b = Arrow3D(start=np.array([0, 0, 0]), end=np.array([0.5, 0, 1]), resolution=8 )
        outgoing_c = Arrow3D(start=np.array([0, 0, 0]), end=np.array([0.5, 1, 1]), resolution=8 )
        outgoing_d = Arrow3D(start=np.array([0, 0, 0]), end=np.array([0.5, -1, 1]), resolution=8 )
        incoming_txt = Text('incoming ray').scale(0.25).rotate(90*DEGREES, axis=X_AXIS).next_to(incoming.get_start())
        outgoing_txt = Text('Specularly reflected ray').scale(0.25).rotate(90*DEGREES, axis=X_AXIS).next_to(outgoing.get_end())
        reflected_txt = Text('reflected rays').scale(0.25).rotate(90*DEGREES, axis=X_AXIS).next_to(outgoing_a.get_end())
        self.add(incoming.set_color(YELLOW), outgoing.set_color(RED), outgoing_a.set_color(YELLOW_B), outgoing_b.set_color(YELLOW_B), outgoing_c.set_color(YELLOW_B), outgoing_d.set_color(YELLOW_B), incoming_txt, outgoing_txt, reflected_txt)

        self.wait(1)
        self.play(Create(axes))
        self.wait(2)

        resolution_fa = 1
        surface_plane = Surface(
                    lambda u, v: axes.c2p(u, v, self.param_surface(u, v)),
                    resolution=(resolution_fa, resolution_fa),
                    v_range=[-2, 2],
                    u_range=[-2, 2],
                    )
        surface_plane.set_style(fill_opacity=0.35)

        self.add(surface_plane)
        self.wait()

        self.move_camera( phi=80*DEGREES, theta=-40*DEGREES, focal_distance=6 )

        self.begin_ambient_camera_rotation(rate=PI / 9, about="theta")
        # Increase the wait time for a longer animation. Default I used was 35. Shortened for the sample video.
        self.wait(5)

        self.stop_ambient_camera_rotation()
        self.wait()

    def param_surface(self, u, v):
        x = u
        y = v
        z = np.sin(x) * np.cos(y)
        return z

if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")