import numpy as np

try:
    import matplotlib.pyplot as plt
except ImportError:  # pragma: no cover
    plt = None

from .base_edge import BaseEdge

from ..pose.r2 import PoseR2
from ..pose.se2 import PoseSE2
from ..pose.r3 import PoseR3
from ..pose.se3 import PoseSE3

class EdgeBundleAdjustCalib(BaseEdge):
    
    def __init__(self, vertex_ids, vertices=None):
        self.vertex_ids = vertex_ids
        self.vertices = vertices

    def calc_error(self):

        raise NotImplementedError
