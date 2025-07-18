# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_Window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDial, QFrame, QGraphicsView,
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QSizePolicy, QSlider, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(689, 786)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ToolsCheckSpelling))
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_top = QLabel(self.centralwidget)
        self.label_top.setObjectName(u"label_top")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_top.sizePolicy().hasHeightForWidth())
        self.label_top.setSizePolicy(sizePolicy)
        self.label_top.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_top.setFrameShape(QFrame.Shape.WinPanel)
        self.label_top.setFrameShadow(QFrame.Shadow.Raised)
        self.label_top.setLineWidth(5)
        self.label_top.setMidLineWidth(5)
        self.label_top.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_top.setMargin(10)
        self.label_top.setIndent(-1)

        self.verticalLayout_2.addWidget(self.label_top)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_rodlenght = QLabel(self.centralwidget)
        self.label_rodlenght.setObjectName(u"label_rodlenght")
        self.label_rodlenght.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_rodlenght)

        self.dial_rodlenght = QDial(self.centralwidget)
        self.dial_rodlenght.setObjectName(u"dial_rodlenght")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dial_rodlenght.sizePolicy().hasHeightForWidth())
        self.dial_rodlenght.setSizePolicy(sizePolicy1)
        self.dial_rodlenght.setMinimumSize(QSize(0, 0))
        self.dial_rodlenght.setBaseSize(QSize(0, 0))
        self.dial_rodlenght.setMinimum(60)
        self.dial_rodlenght.setMaximum(400)

        self.verticalLayout_4.addWidget(self.dial_rodlenght)

        self.label_output_rodlenght = QLabel(self.centralwidget)
        self.label_output_rodlenght.setObjectName(u"label_output_rodlenght")
        self.label_output_rodlenght.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_output_rodlenght)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_ringcount = QLabel(self.centralwidget)
        self.label_ringcount.setObjectName(u"label_ringcount")
        self.label_ringcount.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_ringcount)

        self.dial_ringcount = QDial(self.centralwidget)
        self.dial_ringcount.setObjectName(u"dial_ringcount")
        self.dial_ringcount.setMinimum(3)
        self.dial_ringcount.setMaximum(15)

        self.verticalLayout_3.addWidget(self.dial_ringcount)

        self.label_output_ringcount = QLabel(self.centralwidget)
        self.label_output_ringcount.setObjectName(u"label_output_ringcount")
        self.label_output_ringcount.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_output_ringcount)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_3)

        self.label_modifier = QLabel(self.centralwidget)
        self.label_modifier.setObjectName(u"label_modifier")
        sizePolicy.setHeightForWidth(self.label_modifier.sizePolicy().hasHeightForWidth())
        self.label_modifier.setSizePolicy(sizePolicy)
        self.label_modifier.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_modifier)

        self.slider_modifier = QSlider(self.centralwidget)
        self.slider_modifier.setObjectName(u"slider_modifier")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slider_modifier.sizePolicy().hasHeightForWidth())
        self.slider_modifier.setSizePolicy(sizePolicy2)
        self.slider_modifier.setMinimumSize(QSize(0, 40))
        self.slider_modifier.setMinimum(4)
        self.slider_modifier.setMaximum(16)
        self.slider_modifier.setValue(10)
        self.slider_modifier.setSliderPosition(10)
        self.slider_modifier.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_5.addWidget(self.slider_modifier)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)


        self.verticalLayout.addLayout(self.verticalLayout_5)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.graphic_view_frame = QGraphicsView(self.centralwidget)
        self.graphic_view_frame.setObjectName(u"graphic_view_frame")

        self.verticalLayout.addWidget(self.graphic_view_frame)

        self.label_output_result = QLabel(self.centralwidget)
        self.label_output_result.setObjectName(u"label_output_result")
        sizePolicy.setHeightForWidth(self.label_output_result.sizePolicy().hasHeightForWidth())
        self.label_output_result.setSizePolicy(sizePolicy)
        self.label_output_result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_output_result)


        self.verticalLayout_6.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Rodbuilding Calculator", None))
        self.label_top.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700; text-decoration: underline;\">Welcome to the Rodbuilding-Calculator</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Please enter a rodlenght and number of rings to claculate the positioning</span></p></body></html>", None))
        self.label_rodlenght.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; text-decoration: underline;\">Rodlenght</span></p></body></html>", None))
        self.label_output_rodlenght.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Lenght will be displayed here in centimeters</span></p></body></html>", None))
        self.label_ringcount.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; text-decoration: underline;\">Ringcount</span></p></body></html>", None))
        self.label_output_ringcount.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Number of rings will be displayed here</span></p></body></html>", None))
        self.label_modifier.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\">This slider modifies the gap relation between the rings</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-style:italic;\">A higher value is recommended for long or fast blanks, rings will be more concentrated to the tip</span></p><p align=\"center\"><span style=\" font-size:9pt; font-style:italic;\">A lower value will place the rings more even</span></p></body></html>", None))
        self.label_output_result.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Output will be displayed here</span></p></body></html>", None))
    # retranslateUi

