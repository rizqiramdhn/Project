from manimlib.imports import *
import numpy as np
class Spherical(ThreeDScene,Scene):
    def construct(self):
        judulkalii = TextMobject("Spherical Coordinates")
        judulkalii.scale(1.25)
        judulkalii.set_color_by_gradient(PURPLE,RED)
        self.play(Write(judulkalii))
        self.wait(2)
        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)
        axess = ThreeDAxes()
        self.play(ReplacementTransform(judulkalii,axess),run_time=1.5)
        dott3 = Dot(np.array([4,3,0]), radius=0.08, color=YELLOW)
        garisss= DashedLine([3, 0, 0], color=RED)
        aa = (4,3,0)
        bb = (4,3,3)
        garisss3= DashedLine(aa,bb)
        garisss3.set_color(PURPLE)
        cc = (4,3,3)
        dd = (0,0,3)
        ee = TextMobject("x3")
        ee.shift(5,4,1.5)
        ee = TextMobject("x2")
        ee.shift(1,1,1)
        garisss4=DashedLine(cc,dd)
        garisss.shift(3*UP)
        garisss.scale(2)
        STARTT = (4,0,0)
        ENDD =   (4,1.5,0)
        koordinat = (0,0,2)
        garisss1= DashedLine(STARTT,ENDD)
        garisss1.scale(2)
        garisss1.shift(0.75*UP)
        garisss1.set_color(GREEN)
        kk=(0,0,0)
        ll=(4,3,0)
        garisss2= DashedLine(kk,ll)
        garisss2.set_color_by_gradient(YELLOW,GREEN)
        garisss5= Arrow([0, 0 ,0 ],[4 ,3 ,3 ],color=BLUE)
        garisss2.scale(1)
        angle = math.radians(35)
        arc1 =  Arc(radius=2,angle=angle)
        self.play(FadeIn(dott3), run_time=2)
        self.play(Write(garisss1))
        self.play(Write(garisss))
        self.play(Write(garisss2))
        self.play(Write(garisss3))
        self.play(Write(garisss4))
        self.play(Write(arc1))
        self.wait()
        self.play(Write(garisss5))
        grup =(VGroup(dott3,garisss1,garisss,garisss2,garisss3,garisss4,axess,garisss5,arc1))
        self.play(ApplyMethod(grup.scale,0.4))
        self.play(ApplyMethod(grup.move_to,koordinat))
        self.wait()
        
        #tekss
        judulkaliii = TextMobject("Spherical Coordinates")
        judulkaliii.scale(1.25)
        judulkaliii.set_color_by_gradient(PURPLE,RED)
        self.add_fixed_in_frame_mobjects(judulkaliii)
        self.remove(judulkaliii)
        self.play(Write(judulkaliii))
        self.wait(2)
        self.play(ApplyMethod(judulkaliii.move_to,3.5*UP))
        warnaa = TextMobject("Misal garis yang berwarna merah adalah x1, Garis biru adalah $x^{-1}$ , garis ungu adalah x3, garis hijau adalah x2, theta adalah $x^{-2}$ ")
        namaaaa = TextMobject("P : (X1, X2, X3 adalah rectangular coordinates)")
        namaaaaa = TextMobject("$\\vec{\\vec{\\tau }}$ s adalah sebuah transformasi koordinat curvaliniear")
        namaaa1 = TextMobject("$\\bar{x}^{2}=arctan(\\frac{x^{2}}{x^{1}})$")
        namaaa2 = TextMobject("$\\bar{x}^{-3}=arccos(\\frac{{x}^{3}}{\\sqrt{(x^{1})^{2},(x^{2})^{2},(x^{3})^{2}}})$")
        namaaa3 = TextMobject("$\\bar{x}^{-3}= \sqrt{(x^{1})^{2},(x^{2})^{2},(x^{3})^{2}}$")
        namaaa4 = TextMobject("$x^{1}=\\bar{x}^{1}cos(\\bar{x}^{2})sin(\\bar{x}^{3})$")
        namaaa5 = TextMobject("$x^{2}=\\bar{x}^{1}sin(\\bar{x}^{2})sin(\\bar{x}^{3})$")
        namaaa6 = TextMobject("$x^{3}=\\bar{x}^{1}cos(\\bar{x}^{3})$")
        namaaaa.set_color_by_gradient(RED,GREEN)
        apatehkotakkk2 = Rectangle(height = 1.3, width = 13.5)
        apatehkotakkk2.set_fill(YELLOW, opacity= 1)
        self.add_fixed_in_frame_mobjects(apatehkotakkk2)
        self.remove(apatehkotakkk2)
        apatehkotakkk2.shift(3*DOWN)
        self.play(Write(apatehkotakkk2))
        self.add_fixed_in_frame_mobjects(warnaa)
        self.remove(warnaa)
        warnaa.set_color_by_gradient(RED,BLUE)
        warnaa.scale(0.8)
        self.play(Write(warnaa))
        
        self.play(ApplyMethod(warnaa.move_to, 3*DOWN))
        self.wait()
        self.add_fixed_in_frame_mobjects(namaaaa)
        self.remove(namaaaa)
        self.play(Write(namaaaa))
        self.wait(2)
        namaaaaa.set_color_by_gradient(RED,BLUE)
        self.add_fixed_in_frame_mobjects(namaaaa)
        self.remove(namaaaa)
        self.add_fixed_in_frame_mobjects(namaaaaa)
        self.remove(namaaaaa)
        self.play(ReplacementTransform(namaaaa,namaaaaa),run_time=1)
        self.wait(2)

        namaaa1.shift(1.5*UP)
        namaaa2.next_to(namaaa1,DOWN)
        namaaa3.next_to(namaaa2,DOWN)
        namaaa4.shift(1.5*UP)
        namaaa5.next_to(namaaa4,DOWN)
        namaaa6.next_to(namaaa5,DOWN)
        namaaateh = (VGroup(namaaa1,namaaa2,namaaa3))
        namaaateh1 = (VGroup(namaaa4,namaaa5,namaaa6))
        namaaateh
        b_2 = Brace(namaaateh1, DOWN)
        b_1 = Brace(namaaateh, DOWN)
 
        tensorr = TextMobject("Ts",color=(YELLOW))
        tensorr1 = TextMobject("$Ts^{-1}$",color = (YELLOW))
#        namaaaatt.shift(4*RIGHT)
        
        
        namaaateh.set_color_by_gradient(YELLOW,PURPLE)
        namaaateh.set_color_by_gradient(RED,GREEN)
        self.add_fixed_in_frame_mobjects(namaaaaa)
        self.remove(namaaaaa)
        self.add_fixed_in_frame_mobjects(namaaateh)
        self.remove(namaaateh)
        self.add_fixed_in_frame_mobjects(b_1)
        self.remove(b_1)
        self.play(Write(namaaateh))
        self.play(ApplyMethod(namaaateh.move_to,2*UP+3.5 *LEFT))
        self.add_fixed_in_frame_mobjects(tensorr)
        self.remove(tensorr)
        tensorr.shift(0.2*DOWN+3.65*LEFT)
        self.wait(3)
        self.add_fixed_in_frame_mobjects(namaaateh1)
        self.remove(namaaateh1)
        namaaateh1.set_color_by_gradient(RED,GREEN)
        self.add_fixed_in_frame_mobjects(b_1)
        self.remove(b_1)
        self.play(Write(b_1),run_time=2)
        self.play(ApplyMethod(b_1.move_to,0.3*UP+3.55*LEFT))
        self.play(Write(namaaateh1))
        self.play(ApplyMethod(namaaateh1.move_to,2*UP+4.3*RIGHT))
        
        self.play(Write(tensorr)) 
        self.wait(3)
        self.add_fixed_in_frame_mobjects(b_2)
        self.remove(b_2)
        self.play(Write(b_2))
        self.play(ApplyMethod(b_2.move_to,0.4*UP+4.355*RIGHT))
        self.add_fixed_in_frame_mobjects(tensorr1)
        self.remove(tensorr1)
        tensorr1.shift(4.555*RIGHT)
        self.play(Write(tensorr1))
        self.wait(3)
        