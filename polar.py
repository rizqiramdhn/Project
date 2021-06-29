from manimlib.imports import *
import numpy as np

class SeeIfFormulaMakesSense(Scene):
    def construct(self):
        grid = NumberPlane()
        axis = Axes()
        self.add(grid, axis)


        self.wait()


        self.wait(3)
        garis= Arrow([0, 0, 0], [3, 3, 0], color=BLUE)
        garis.scale(1.15)
        dot1 = Dot(np.array([0,0,0]), radius=0.08, color=YELLOW)
        dot2 = Dot(np.array([3,3,0]), radius=0.08, color=YELLOW)
        grid.faded_lines[4:9].fade(1)
        teks = TextMobject("$$(a^{i})^{2}=a^{i} X a^{i}$$")
        matrix1 = TexMobject(r"\overrightarrow{PQ}=\vec{x}=\begin{bmatrix}x^{1}\\ x^{2}\\ x^{3}\\ \vdots  \\x^{n}\end{bmatrix}")
        teks1 = TextMobject("$$A:(a^{1},a^{2},a^{3},\cdots ,a^{n})$$")
        teks2 =TextMobject("Definisi : suatu sistem koordinat","$ x^{i}pada R^{n}$","disebut rectangular")
        teks3 =TextMobject("jika jarak antara 2 titik a(x1,x2,. . ., xn) dan b(y1,y2,. . . .,yn) dapat dicari dengan")
        teks4 =TextMobject("$\\sqrt{(x^{1}-x^{1})^{2}+(x^{2}-x^{2})^{2}+\cdots }=\\sqrt{\\delta _{ij}\\Delta x^{i}\\Delta x^{j}}$")
        teks5=TextMobject("dimana : ","$\\Delta x^{i}=x^{i}-y^{i}$")
        teks2.shift(1.5*UP)
        ppp = TextMobject("P")
        qqq = TextMobject("Q")
        ppp.shift(0.25*UP+0.25*LEFT)
        qqq.shift(3.35*UP+3.35*RIGHT)
        teks3.next_to(teks2,DOWN)
        teks4.next_to(teks3,DOWN)
        teks5.next_to(teks4,DOWN)
        teksteh = (VGroup(teks2,teks4,teks3,teks5))
        teksteh.scale(0.75)
        teksteh.set_color_by_gradient(PURPLE,RED)
        matrix1.shift(2*UP+4*LEFT)
        self.play(FadeOut(grid))
        self.play(FadeIn(dot1))
        self.wait()
        self.play(FadeIn(ppp))
        self.wait()
        self.play(FadeIn(dot2))
        self.wait()
        self.play(FadeIn(qqq))
        self.play(Write(garis))
        self.wait()
        self.play(ShowCreation(matrix1))
        teks1.shift(2*DOWN+4*LEFT)
        teks.shift(2*UP+4*RIGHT)
        self.wait(2)   
        self.play(Write(teks1))        
        self.wait()
        radius=0.08
        self.play(Write(teks))
        teksilang=(VGroup(axis,teks,matrix1,teks1,dot1,dot2,garis,ppp,qqq))
        theta=PI/4
        self.wait(3)
        apatehkotak1 = Rectangle(height =3.2, width = 12.8)
        apatehkotak1.set_fill(YELLOW, opacity= 0.8)
        self.play(Write(apatehkotak1),ReplacementTransform(teksilang,teksteh), run_time= 3)
        self.wait(3)

        