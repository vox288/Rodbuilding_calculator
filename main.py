# This programm is meant to be used for rodbuilding:
#   It calculates measurements for Fishing-Rods
#
# main.py runs a GUI window based on the PySide6 Framework (Copyright © The Qt Company).
#
# Using the:
#   Rodlength-dial  -- for adjusting the rodlength
#   Ringcount-dial  -- for adjusting number of rings
#   Modifier-slider -- for adjusting the gap relation
#   
#   You can tweak around and adjust your measurements.
#   A small graphic will be displayed as soon as you provide
#   a Rodlenght and Rings, via the Modifier you are able to
#   change the relation of the gaps between the rings.
#
#   A higher Modifier will shift the rings more to the tip
#       wich may be better for fast or short blanks 
#   A lower modifier will place the rings much more even 
#       wich may be better for slow or long blanks
# 
# The programm will also calculate the following measurements:
#
#   - position for the center of the reel_seat 
#     - position for the start_ring from bottom up
#       - length of the ringed section
#         - gaps between the rings, from the tip to startring
#           and with it their exact position.
#           You measure from each ring to the next one:
#             {"Ring 1":0:0, "Ring 2: 8.75","Ring 3": 12.50}
#                             **means**
#             | Tip-Ring--> 8.75 -->Ring 2--> 12.50 -->Ring 3
#    
#           ****All measurements are in Centimeters****
#
# The programm will automaticaly create or overwrite an 
# existing Rod_Specs.txt file, with your last setup,
# listing all measurements.
#
# If you don't want to use the GUI you could just use blank_separator.py
# in the utils directory. Just uncomment the bottom lines and adjusting it as needed.
#
# Author: Jens Michalik     E-Mail: vox288@gmail.com
#
# This project is licensed under the MIT License
#
# This application uses PySide6 (Copyright © The Qt Company),
# licensed under the GNU Lesser General Public License (LGPL) version 3.
# The source code of PySide6 is available at www.qt.io.


import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QPainter

from utils.blank_separator import BlankSeparator
from utils.rod_graphic import RodGraphic
from UI.Main_Window_ui import Ui_MainWindow


class Main_Window(QMainWindow, Ui_MainWindow):
    """Starts a GUI program that can be used to calculate,
    display and save the positioning for the components
    of a fishing rod.

    Args are rodlenght, number of rings and optional modifier
        lenght (int)     -- the lenght of the blank in cm
        rings (int)      -- number of rings, at least 2
        modifier (float) -- default 0.1, changes gap relations
    """

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("Rodbuilding Calculator")

        self.dial_rodlenght.valueChanged.connect(self._get_rodlenght)
        self.dial_ringcount.valueChanged.connect(self._get_ringcount)
        self.slider_modifier.valueChanged.connect(self._get_modifier)
        self.lenght_is_set = 1.0
        self.rings_are_set = 1.0
        self.modifier = 0.1
        self.graphic_view_frame.scale(1.7, 1.4)


    def _get_ringcount(self):
        """Inner use, gets called if the value of the dial changes."""
        ring_count = self.dial_ringcount.value()
        self.rings_are_set = ring_count
        if self.lenght_is_set >= 1 and self.rings_are_set >= 2:
            self.save_rod_measures()
        return self.label_output_ringcount.setText(
            str(ring_count) + " " + "Rings"
        )


    def _get_rodlenght(self):
        """Inner use, gets called if the value of the dial changes."""
        rodlenght = self.dial_rodlenght.value()
        self.lenght_is_set = rodlenght
        if self.lenght_is_set >= 1 and self.rings_are_set >= 2:
            self.save_rod_measures()
        return self.label_output_rodlenght.setText(str(rodlenght) + " " + "cm")


    def _get_modifier(self):
        """Inner use, is called if the value of the slider changes."""
        modifier = self.slider_modifier.value()
        self.modifier = modifier / 100
        self.save_rod_measures()
        return self.label_modifier.setText(str(modifier))


    def create_rod_graphic(self):
        """If rodlenght and ringcount are set, renders a graphic.

        The QGraphicView is refreshed every time a value changes.
        """ 
        scene = RodGraphic(
            self.dial_rodlenght.value(),
            self.dial_ringcount.value(),
            self.modifier,
        ).render_graphic()
        self.graphic_view_frame.setRenderHints(QPainter.Antialiasing)
        return self.graphic_view_frame.setScene(scene)


    def save_rod_measures(self):
        """Calculates and saves the rod measurements to Rod_Specs.txt.

        The txt file is refreshed every time a value changes.
        """
        try:
            blank = BlankSeparator(
                self.dial_rodlenght.value(),
                self.dial_ringcount.value(),
                self.modifier,
            )
            blank_specs = {
                "Rodlenght overall": str(self.dial_rodlenght.value())
                + " "
                + "cm",
                "Center of reelseat from bottom up": str(blank.calc_reel_seat())
                + " "
                + "cm",
                "Startring from bottom up": str(
                    blank.calc_start_ring() + blank.calc_reel_seat()
                )
                + " "
                + "cm",
                "Number of Rings": self.dial_ringcount.value(),
                "Ringed section": str(blank.calc_ringed_section())
                + " "
                + "cm",
                "Modifier used": self.modifier * 100,
                "Ring gaps from tip to bottom in cm": blank.scale_ring_positions(),
            }
            with open("Rod_Specs.txt", "w", encoding="utf-8") as file:
                for item in blank_specs.items():
                    file.writelines(str(item) + "\n")

            self.create_rod_graphic()
            return self.label_output_result.setText(
                "Rod-Measurements are saved in Rod_Specs.txt"
            )
        except Exception as err:
            match err:
                case FileNotFoundError():
                    print("Error has occured while saving the Specs")
                    print(err)
                case OSError():
                    print("Error with OS or file occured while saving the Specs")
                    print(err)

def main():
    app = QApplication(sys.argv)
    window = Main_Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

