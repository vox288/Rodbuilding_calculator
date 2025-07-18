
# This module is used to generate a simple
# graphic, based on the calculations of its
# sub - module.
#
# The class itself is the GraphicScene
#
# By passing a rodlenght, number of rings and
# an optional modifier it can:
#   - create a simple "blank" graphic
#   - create graphic for every ring
#   - combine and render all graphics
#     on the GraphicScene
#   - return itself to display a simple
#     fishingrod graphic
#
# The modifier will change the relation of gaps
# between the rings. A higher modifier (up to 0.16)
# will shift the rings more to the tip. 
# A lower modifier (down to 0.5) will spread the
# ring gaps more even around the blank


from PySide6.QtWidgets import QGraphicsScene
from PySide6.QtGui import QPen, QBrush, QColor, QPolygonF
from PySide6.QtCore import QPointF, QRectF

from utils.blank_separator import BlankSeparator


class RodGraphic(QGraphicsScene):
    """
    Renders a QGraphicScene that display a fishing rod.
    
    Based on the calculations of its sub-module this class
    renders a blank and the rings of the rod.
    
    Args are rodlenght, number of rings and optional modifier
        lenght (int)     -- the lenght of the blank in cm
        rings (int)      -- number of rings, at least 2
        modifier (float) -- default 0.1, changes gap relations
    """
    def __init__(self, lenght, rings, modifier=0.1):
        super().__init__()

        self.rings = rings
        self.modifier = modifier
        self.lenght = lenght

        self.black_pen = QPen(QColor(0, 0, 0))
        self.black_pen.setWidth(1)
        self.grey_pan = QPen(QColor(96, 96, 96))
        self.grey_pan.setWidth(5)

        self.grey_brush = QBrush(QColor(96, 96, 96))
        self.white_brush = QBrush(QColor(255, 255, 255))
        self.black_brush = QBrush(QColor(0, 0, 0))

        if self.lenght < 0 or self.rings <= 0:
            raise ValueError("Length and rings must be non-negative")
        

    def render_blank(self):
        """
        Renders a rod graphic based on rodlenght.
            Returns -> QGraphicItem
        """
        points = QPolygonF([
                QPointF(0, 13),
                QPointF(0, 17),
                QPointF(self.lenght, 15)])
        blank = self.addPolygon(
            points, pen=self.black_pen, brush=self.black_brush)
        return blank


    def render_rings(self):
        """
        Renders the rings and adjusts their size & position.
            Returns -> QGraphicItem
        """
        ring_gaps = BlankSeparator(
            self.lenght, self.rings, self.modifier
        ).scale_ring_positions().values()
        ring_size = 4
        ring_height = 14
        lenght_minus_gap = self.lenght
        for gap in ring_gaps:
            lenght_minus_gap -= gap
            measure = QRectF(
                lenght_minus_gap,
                ring_height,
                ring_size,
                ring_size,
            )
            ring = self.addEllipse(
                measure, pen=self.black_pen, brush=self.white_brush
            )
            ring_size *= 1.02
            ring_height += 0.1
            yield ring


    def render_graphic(self):
        """
        Combines rendered blank & rings QGraphicItems into
        a QGraphicScene resembling a fishinrod.

            Returns -> QGraphicScene
        """
        self.render_blank()
        self.gen = self.render_rings()
        for i in range(self.rings):
            next(self.gen)
            i += 1
        return self



##For testing purpose
#
#if __name__ == "__main__":
#    import sys
#    from PySide6.QtWidgets import QApplication, QGraphicsView
#
#
#    app = QApplication(sys.argv)
#    scene = RodGraphic(210, 7).render_graphic()
#    graphic_view = QGraphicsView(scene)
#    graphic_view.show()
#    sys.exit(app.exec())