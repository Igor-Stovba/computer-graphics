from PyQt5.QtWidgets import (
    QFrame,
    QWidget,
)


class ObstaclesPanel(QWidget):
    def __init__(self):
        super().__init__()

        # Initially, no cats widget is created
        self.obstacles_drawer = None

        # Create a frame for the cats widget
        self.obst_frame = QFrame(self)
        self.obst_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.obst_frame.setFrameShadow(QFrame.Shadow.Raised)

        # Create a layout for the cats frame
        self.obst_layout = None