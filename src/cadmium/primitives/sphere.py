# 
# Cadmium - Python library for Solid Modelling
# Copyright (C) 2011 Jayesh Salvi [jayesh <at> 3dtin <dot> com]
#

import math
from OCC.BRepPrimAPI import *

from cadmium.polyhedron import Solid

class Sphere(Solid):
  
  def __init__(self, r=None, radius=None, phi=360):
    if radius: r = radius
    self.instance = BRepPrimAPI_MakeSphere(r, phi*math.pi/180)
    Solid.__init__(self, shape=self.instance.Shape())