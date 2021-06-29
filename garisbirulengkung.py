from manimlib.imports import *
import math
import numpy as np
class Matriks10(ZoomedScene):
    CONFIG = {
    "zoom_factor": 0.5,
    "zoomed_display_height": 4,
    "zoomed_display_width": 4,
    "image_frame_stroke_width": 20,
    "zoomed_camera_config": {
    "default_frame_stroke_width": 3,
    },
    }
    def construct(self):

        props = TextMobject("Jacobian Matriks : ").set_color(YELLOW).to_corner(UP + LEFT)
        self.play(ShowCreation(props))

        self.wait()
        grid = NumberPlane()
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_function,
            lambda p: p + 0.5*np.array([
                np.sin(p[1]),
                np.sin(p[0]),
                0,
            ]),
            run_time=2,
        )

        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame
        zoomed_display_frame.set_color(RED)
        zd_rect = BackgroundRectangle(
        zoomed_display,
        fill_opacity=0,
        buff=MED_SMALL_BUFF,
        )
           
        self.add_foreground_mobject(zd_rect)
        unfold_camera = UpdateFromFunc(
        zd_rect,
        lambda rect: rect.replace(zoomed_display)
        )


        self.play(
            ShowCreation(frame))
        self.activate_zooming()
        
        self.play(
            # You have to add this line
            self.get_zoomed_display_pop_out_animation(),
            unfold_camera
        )



        # Scale in     x   y  z
        scale_factor=[0.5,1.5,0]

        self.wait()
        
        teke = TexMobject(r"\begin{bmatrix}\frac{\partial f_{1}}{\partial x} & \frac{\partial f_{1}}{\partial y}\\ \frac{\partial f_{2}}{\partial x}& \frac{\partial f_{2}}{\partial y}\end{bmatrix}")
        teke.set_color_by_gradient(RED,YELLOW)
        teke.shift(1*UP+5*LEFT)
        self.play(Write(teke))  
        



        self.wait(5)