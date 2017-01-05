#!/usr/bin/python3
import sys
import math
from PyQt5.QtWidgets import  QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
import numpy as np



class MandelbrotWidget(QWidget):
    def __init__(self, iteration, sizex= 1200, sizey = 800):
        super().__init__()

        self.iteration = iteration
        self.x1 = -2.1
        self.x2 = 0.6
        self.y1 = -1.2
        self.y2 = 1.2

        self.sizex = sizex
        self.sizey = sizey

        self.initUI()
        self.update()

    def initUI(self):

        self.setGeometry(300, 300, self.sizex, self.sizey)
        self.setWindowTitle("Mandelbrot")
        self.show()

    def paintEvent(self, qp):

        qp = QPainter()
        qp.begin(self)
        self.drawFractal(qp)
        qp.end()

    def drawFractal(self, qp):

        stepX =  (self.x2 - self.x1) / self.sizex
        stepY =  (self.y2 - self.y1) / self.sizey

        centerx = self.sizex * ( 1 - self.x2 / (self.x2 - self.x1) )
        centery = self.sizey * ( 1 - self.y2 / (self.y2 - self.y1) )


        for x in np.linspace(self.x1, self.x2, num = self.sizex):          
            for y in np.linspace(self.y1, self.y2, num = self.sizey):

                c = complex(x, y)
                z = complex(0)

                for itera in range(self.iteration):
                    z = z*z + c

                
                try:
                    if math.sqrt(z.real ** 2 + z.imag ** 2) < 4 :
                        xx = x * self.sizex / (self.x2 - self.x1)  + centerx
                        yy = y * self.sizey / (self.y2 - self.y1)  + centery
                        qp.drawPoint(xx, yy)

                except:
                    pass



if __name__ == "__main__":

    print("Mandelbrot")
    app = QApplication(sys.argv)
    mandel = MandelbrotWidget(1000)
    sys.exit(app.exec_())





