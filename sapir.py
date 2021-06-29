from manimlib.imports import *

class ThreeDObjects(SpecialThreeDScene):
    def construct(self):
        sphere = self.get_sphere()
        cube = Cube()
        prism = Prism()
        prisma = Prisma()

        self.set_camera_orientation(0.8, -0.7853981, 106.6)
        self.play(ShowCreation(sphere))
        self.play(ReplacementTransform(sphere, cube))
        self.play(ReplacementTransform(cube, prism))
        self.wait()

       

        self.wait()
        self.move_camera(0.8*np.pi/2, -0.60*np.pi)
        self.play(ApplyMethod(prism.move_to,5*LEFT))
        vek= Arrow([-2, 0, 0], [0, 0, 0])
        vek.scale(1.5)
        prisma.shift(4*RIGHT)
        self.play(Write(prisma))
        self.play(Write(vek))
        self.begin_ambient_camera_rotation()
        self.wait(9)
        