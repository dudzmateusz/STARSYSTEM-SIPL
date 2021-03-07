from PyQt5 import QtCore, QtGui, QtWidgets
from http.server import BaseHTTPRequestHandler, HTTPServer
import sys
import urllib
import base64
import json
import ctypes
import urllib.request
import requests
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.Qt import *
from PyQt5.uic import loadUi
from PyQt5 import *
from logowanie import *
from json import dumps
from xlwt import *
import datetime
from datetime import date
import signal
from PyQt5 import QtCore, QtGui, QtWidgets
import cx_Oracle
import importlib
import subprocess
import os
import time
import re
import pandas as pd
from itertools import *
import xlsxwriter
import xlwt
import csv
from PIL import Image
from time import sleep
from tqdm import tqdm

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 972)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 720))
        MainWindow.setWindowIcon(QIcon("zdjecia/logoprogramu.ico"))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 73, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 61, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 32, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 73, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 61, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 32, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 73, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 61, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 32, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"    color: #ffffff;\n"
"    background-color: rgba(27, 29, 35, 160);\n"
"    border: 1px solid rgb(40, 40, 40);\n"
"    border-radius: 2px;\n"
"}")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setStyleSheet("/* LINE EDIT */\n"
"QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"    border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {    \n"
"    background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"    border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"    border: 3px solid rgb(52, 59, 72);    \n"
"    background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"    border: 3px solid rgb(52, 59, 72);    \n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px; \n"
"    border-left-width: 3px;\n"
"    border-left-color: rgba(39, 44, 54, 150);\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;    \n"
"    background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(85, 170, 255);    \n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 10px;\n"
"    selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"    margin: 0px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"    background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"    border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"    background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"    border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_main)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_top = QtWidgets.QFrame(self.frame_main)
        self.frame_top.setMinimumSize(QtCore.QSize(0, 65))
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 65))
        self.frame_top.setStyleSheet("background-color: transparent;")
        self.frame_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_toggle = QtWidgets.QFrame(self.frame_top)
        self.frame_toggle.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_toggle.setStyleSheet("background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3.addWidget(self.frame_toggle)
        self.frame_top_right = QtWidgets.QFrame(self.frame_top)
        self.frame_top_right.setStyleSheet("background: transparent;")
        self.frame_top_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_right.setObjectName("frame_top_right")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_top_btns = QtWidgets.QFrame(self.frame_top_right)
        self.frame_top_btns.setMaximumSize(QtCore.QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet("background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_btns.setObjectName("frame_top_btns")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_label_top_btns = QtWidgets.QFrame(self.frame_top_btns)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy)
        self.frame_label_top_btns.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_top_btns.setObjectName("frame_label_top_btns")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_title_bar_top = QtWidgets.QLabel(self.frame_label_top_btns)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_title_bar_top.setFont(font)
        self.label_title_bar_top.setStyleSheet("background: transparent;\n"
"")
        self.label_title_bar_top.setObjectName("label_title_bar_top")
        self.horizontalLayout_10.addWidget(self.label_title_bar_top)
        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)
        self.frame_btns_right = QtWidgets.QFrame(self.frame_top_btns)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy)
        self.frame_btns_right.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns_right.setObjectName("frame_btns_right")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addWidget(self.frame_top_btns)
        self.frame_top_info = QtWidgets.QFrame(self.frame_top_right)
        self.frame_top_info.setMaximumSize(QtCore.QSize(16777215, 65))
        self.frame_top_info.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_info.setObjectName("frame_top_info")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_2.addWidget(self.frame_top_info)
        self.horizontalLayout_3.addWidget(self.frame_top_right)
        self.verticalLayout.addWidget(self.frame_top)
        self.frame_center = QtWidgets.QFrame(self.frame_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet("background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_center.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_center.setObjectName("frame_center")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_content_right = QtWidgets.QFrame(self.frame_center)
        self.frame_content_right.setStyleSheet("background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content_right.setObjectName("frame_content_right")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_content = QtWidgets.QFrame(self.frame_content_right)
        self.frame_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_content)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tabWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tabWidget.setFont(font)
        self.tabWidget.setMouseTracking(True)
        self.tabWidget.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"    border-color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.tabWidget.setIconSize(QtCore.QSize(50, 50))
        self.tabWidget.setObjectName("tabWidget")
        self.HOME = QtWidgets.QWidget()
        self.HOME.setObjectName("HOME")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.HOME)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_6 = QtWidgets.QLabel(self.HOME)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("")
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_10.addWidget(self.label_6)
        self.label_3 = QtWidgets.QLabel(self.HOME)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("zdjecia/logoprogramu.ico"))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_10.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(self.HOME)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_10.addWidget(self.label)
        self.label_7 = QtWidgets.QLabel(self.HOME)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_10.addWidget(self.label_7)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("zdjecia/png-clipart-home-apartment-ico-flat-design-icon-christmas-home-free-holidays-text.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.HOME, icon, "")
        self.tabWidgetPage2 = QtWidgets.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tabWidgetPage2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame = QtWidgets.QFrame(self.tabWidgetPage2)
        self.frame.setStyleSheet("border-radius: 5px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_6.addWidget(self.frame)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tabWidgetPage2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setClearButtonEnabled(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_6.addWidget(self.lineEdit_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.pushButton_3.setText("")
        self.pushButton_3.clicked.connect(self.Ui_szukaj_listu)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("zdjecia/Jommans-Briefness-Search.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_6.addWidget(self.pushButton_3)
        self.frame_3 = QtWidgets.QFrame(self.tabWidgetPage2)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 150))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.tableWidget_66 = QtWidgets.QTableWidget(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_66.sizePolicy().hasHeightForWidth())
        self.tableWidget_66.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tableWidget_66.setPalette(palette)
        self.tableWidget_66.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget_66.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_66.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_66.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_66.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_66.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_66.setAlternatingRowColors(False)
        self.tableWidget_66.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_66.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_66.setShowGrid(True)
        self.tableWidget_66.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_66.setObjectName("tableWidget_66")
        self.tableWidget_66.setColumnCount(16)
        self.tableWidget_66.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_66.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_66.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_66.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_66.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_66.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_66.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_66.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_66.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_66.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_66.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_66.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_66.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_66.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_66.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_66.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_66.setHorizontalHeaderItem(15, item)
        self.tableWidget_66.horizontalHeader().setVisible(False)
        self.tableWidget_66.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_66.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_66.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_66.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_66.verticalHeader().setVisible(False)
        self.tableWidget_66.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_66.verticalHeader().setHighlightSections(False)
        self.tableWidget_66.verticalHeader().setStretchLastSection(True)
        self.horizontalLayout_12.addWidget(self.tableWidget_66)
        self.verticalLayout_6.addWidget(self.frame_3)
        self.tableWidget_38 = QtWidgets.QTableWidget(self.tabWidgetPage2)
        self.tableWidget_38.setMinimumSize(QtCore.QSize(0, 200))
        self.tableWidget_38.setMaximumSize(QtCore.QSize(16777215, 250))
        self.tableWidget_38.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget_38.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_38.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_38.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_38.setObjectName("tableWidget_38")
        self.tableWidget_38.setColumnCount(8)
        self.tableWidget_38.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_38.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_38.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_38.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_38.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_38.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_38.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_38.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_38.setHorizontalHeaderItem(7, item)
        self.verticalLayout_6.addWidget(self.tableWidget_38)
        self.tableWidget_37 = QtWidgets.QTableWidget(self.tabWidgetPage2)
        self.tableWidget_37.setMaximumSize(QtCore.QSize(16777215, 100))
        self.tableWidget_37.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget_37.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_37.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_37.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_37.setObjectName("tableWidget_37")
        self.tableWidget_37.setColumnCount(7)
        self.tableWidget_37.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_37.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_37.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_37.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_37.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_37.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_37.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_37.setHorizontalHeaderItem(6, item)
        self.verticalLayout_6.addWidget(self.tableWidget_37)
        self.tableWidget_40 = QtWidgets.QTableWidget(self.tabWidgetPage2)
        self.tableWidget_40.setMaximumSize(QtCore.QSize(16777215, 100))
        self.tableWidget_40.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget_40.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_40.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_40.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_40.setObjectName("tableWidget_40")
        self.tableWidget_40.setColumnCount(5)
        self.tableWidget_40.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_40.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_40.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_40.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_40.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_40.setHorizontalHeaderItem(4, item)
        self.verticalLayout_6.addWidget(self.tableWidget_40)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("zdjecia/list.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabWidgetPage2, icon2, "")
        self.tabWidgetPage3 = QtWidgets.QWidget()
        self.tabWidgetPage3.setObjectName("tabWidgetPage3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabWidgetPage3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.tabWidgetPage3)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("zdjecia/obrazekpaju.png"))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tabWidgetPage3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setClearButtonEnabled(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.verticalLayout_5.addWidget(self.lineEdit_13)
        self.pushButton_29 = QtWidgets.QPushButton(self.tabWidgetPage3)
        self.pushButton_29.setText("")
        self.pushButton_29.clicked.connect(self.Ui_szukaj_nickuPAYU)
        self.pushButton_29.setIcon(icon1)
        self.pushButton_29.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_29.setObjectName("pushButton_29")
        self.verticalLayout_5.addWidget(self.pushButton_29)
        self.pushButton_6 = QtWidgets.QPushButton(self.tabWidgetPage3)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("zdjecia/excel-icon1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon3)
        self.pushButton_6.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.Ui_ZapiszPayu)
        self.verticalLayout_5.addWidget(self.pushButton_6)
        self.tableWidget_7 = QtWidgets.QTableWidget(self.tabWidgetPage3)
        self.tableWidget_7.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_7.sizePolicy().hasHeightForWidth())
        self.tableWidget_7.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tableWidget_7.setPalette(palette)
        self.tableWidget_7.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget_7.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_7.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_7.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget_7.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_7.setAlternatingRowColors(False)
        self.tableWidget_7.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_7.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_7.setShowGrid(True)
        self.tableWidget_7.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_7.setObjectName("tableWidget_7")
        self.tableWidget_7.setColumnCount(6)
        self.tableWidget_7.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(5, item)
        self.tableWidget_7.horizontalHeader().setVisible(False)
        self.tableWidget_7.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_7.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_7.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_7.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_7.verticalHeader().setVisible(False)
        self.tableWidget_7.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_7.verticalHeader().setHighlightSections(False)
        self.tableWidget_7.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_5.addWidget(self.tableWidget_7)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("zdjecia/payment-payu-money-card-51321.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabWidgetPage3, icon4, "")
        self.tabWidgetPage4 = QtWidgets.QWidget()
        self.tabWidgetPage4.setObjectName("tabWidgetPage4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tabWidgetPage4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.tabWidgetPage4)
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("zdjecia/p24324.png"))
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tabWidgetPage4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setClearButtonEnabled(True)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout_7.addWidget(self.lineEdit_12)
        self.pushButton_28 = QtWidgets.QPushButton(self.tabWidgetPage4)
        self.pushButton_28.setText("")
        self.pushButton_28.setIcon(icon1)
        self.pushButton_28.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_28.clicked.connect(self.Ui_szukaj_nickuP24)
        self.verticalLayout_7.addWidget(self.pushButton_28)
        self.pushButton_7 = QtWidgets.QPushButton(self.tabWidgetPage4)
        self.pushButton_7.setIcon(icon3)
        self.pushButton_7.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.Ui_ZapiszP24)
        self.verticalLayout_7.addWidget(self.pushButton_7)
        self.tableWidget_8 = QtWidgets.QTableWidget(self.tabWidgetPage4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_8.sizePolicy().hasHeightForWidth())
        self.tableWidget_8.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tableWidget_8.setPalette(palette)
        self.tableWidget_8.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_8.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_8.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_8.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_8.setAlternatingRowColors(False)
        self.tableWidget_8.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_8.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_8.setShowGrid(True)
        self.tableWidget_8.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_8.setObjectName("tableWidget_8")
        self.tableWidget_8.setColumnCount(6)
        self.tableWidget_8.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(5, item)
        self.tableWidget_8.horizontalHeader().setVisible(False)
        self.tableWidget_8.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_8.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_8.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_8.verticalHeader().setVisible(False)
        self.tableWidget_8.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_8.verticalHeader().setHighlightSections(False)
        self.tableWidget_8.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_7.addWidget(self.tableWidget_8)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("zdjecia/p24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabWidgetPage4, icon5, "")
        self.tabWidgetPage5 = QtWidgets.QWidget()
        self.tabWidgetPage5.setObjectName("tabWidgetPage5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tabWidgetPage5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.tabWidgetPage5)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("zdjecia/getbeck.png"))
        self.label_9.setObjectName("label_9")
        self.verticalLayout_8.addWidget(self.label_9, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.tabWidgetPage5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setClearButtonEnabled(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.verticalLayout_8.addWidget(self.lineEdit_14)
        self.pushButton_30 = QtWidgets.QPushButton(self.tabWidgetPage5)
        self.pushButton_30.setText("")
        self.pushButton_30.setIcon(icon1)
        self.pushButton_30.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_30.clicked.connect(self.Ui_szukaj_nickuZWROTY)
        self.verticalLayout_8.addWidget(self.pushButton_30)
        self.pushButton_19 = QtWidgets.QPushButton(self.tabWidgetPage5)
        self.pushButton_19.setIcon(icon3)
        self.pushButton_19.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_19.clicked.connect(self.Ui_ZapiszZwroty)
        self.verticalLayout_8.addWidget(self.pushButton_19)
        self.tableWidget_9 = QtWidgets.QTableWidget(self.tabWidgetPage5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_9.sizePolicy().hasHeightForWidth())
        self.tableWidget_9.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tableWidget_9.setPalette(palette)
        self.tableWidget_9.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_9.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_9.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_9.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_9.setAlternatingRowColors(False)
        self.tableWidget_9.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_9.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_9.setShowGrid(True)
        self.tableWidget_9.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_9.setObjectName("tableWidget_9")
        self.tableWidget_9.setColumnCount(6)
        self.tableWidget_9.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(5, item)
        self.tableWidget_9.horizontalHeader().setVisible(False)
        self.tableWidget_9.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_9.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_9.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_9.verticalHeader().setVisible(False)
        self.tableWidget_9.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_9.verticalHeader().setHighlightSections(False)
        self.tableWidget_9.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_8.addWidget(self.tableWidget_9)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("zdjecia/getbeck.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabWidgetPage5, icon6, "")
        self.tabWidgetPage6 = QtWidgets.QWidget()
        self.tabWidgetPage6.setObjectName("tabWidgetPage6")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tabWidgetPage6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.tabWidgetPage6)
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("zdjecia/fedex.png"))
        self.label_11.setObjectName("label_11")
        self.verticalLayout_11.addWidget(self.label_11, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tabWidgetPage6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setClearButtonEnabled(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_11.addWidget(self.lineEdit_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.tabWidgetPage6)
        self.pushButton_10.setText("")
        self.pushButton_10.setIcon(icon1)
        self.pushButton_10.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.Ui_szukaj_nickuF)
        self.verticalLayout_11.addWidget(self.pushButton_10)
        self.pushButton_4 = QtWidgets.QPushButton(self.tabWidgetPage6)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("zdjecia/import-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon7)
        self.pushButton_4.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.Ui_otworzFCod)
        self.verticalLayout_11.addWidget(self.pushButton_4)
        self.pushButton_9 = QtWidgets.QPushButton(self.tabWidgetPage6)
        self.pushButton_9.setIcon(icon3)
        self.pushButton_9.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.Ui_ZapiszFedexCOD)
        self.verticalLayout_11.addWidget(self.pushButton_9)
        self.tableWidget_32 = QtWidgets.QTableWidget(self.tabWidgetPage6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_32.sizePolicy().hasHeightForWidth())
        self.tableWidget_32.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tableWidget_32.setPalette(palette)
        self.tableWidget_32.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget_32.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_32.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_32.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_32.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_32.setAlternatingRowColors(False)
        self.tableWidget_32.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_32.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_32.setShowGrid(True)
        self.tableWidget_32.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_32.setObjectName("tableWidget_32")
        self.tableWidget_32.setColumnCount(10)
        self.tableWidget_32.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_32.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_32.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_32.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_32.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_32.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_32.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_32.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_32.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_32.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_32.setHorizontalHeaderItem(9, item)
        self.tableWidget_32.horizontalHeader().setVisible(False)
        self.tableWidget_32.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_32.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_32.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_32.verticalHeader().setVisible(False)
        self.tableWidget_32.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_32.verticalHeader().setHighlightSections(False)
        self.tableWidget_32.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_11.addWidget(self.tableWidget_32)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("zdjecia/fedex.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabWidgetPage6, icon8, "")
        self.tabWidgetPage7 = QtWidgets.QWidget()
        self.tabWidgetPage7.setObjectName("tabWidgetPage7")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tabWidgetPage7)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_12 = QtWidgets.QLabel(self.tabWidgetPage7)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 333))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("zdjecia/dpd.png"))
        self.label_12.setObjectName("label_12")
        self.verticalLayout_12.addWidget(self.label_12, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tabWidgetPage7)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setClearButtonEnabled(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_12.addWidget(self.lineEdit_10)
        self.pushButton_13 = QtWidgets.QPushButton(self.tabWidgetPage7)
        self.pushButton_13.setText("")
        self.pushButton_13.setIcon(icon1)
        self.pushButton_13.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_12.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.tabWidgetPage7)
        self.pushButton_14.setIcon(icon7)
        self.pushButton_14.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.clicked.connect(self.Ui_otworzDPDCod)
        self.verticalLayout_12.addWidget(self.pushButton_14)
        self.pushButton_20 = QtWidgets.QPushButton(self.tabWidgetPage7)
        self.pushButton_20.setIcon(icon3)
        self.pushButton_20.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_20.clicked.connect(self.Ui_ZapiszDPDCOD)
        self.verticalLayout_12.addWidget(self.pushButton_20)
        self.tableWidget_34 = QtWidgets.QTableWidget(self.tabWidgetPage7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_34.sizePolicy().hasHeightForWidth())
        self.tableWidget_34.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tableWidget_34.setPalette(palette)
        self.tableWidget_34.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget_34.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_34.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_34.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_34.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_34.setAlternatingRowColors(False)
        self.tableWidget_34.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_34.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_34.setShowGrid(True)
        self.tableWidget_34.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_34.setObjectName("tableWidget_34")
        self.tableWidget_34.setColumnCount(10)
        self.tableWidget_34.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_34.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_34.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_34.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_34.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_34.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_34.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_34.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_34.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_34.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_34.setHorizontalHeaderItem(9, item)
        self.tableWidget_34.horizontalHeader().setVisible(False)
        self.tableWidget_34.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_34.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_34.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_34.verticalHeader().setVisible(False)
        self.tableWidget_34.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_34.verticalHeader().setHighlightSections(False)
        self.tableWidget_34.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_12.addWidget(self.tableWidget_34)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("zdjecia/DPD.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabWidgetPage7, icon9, "")
        self.tabWidgetPage8 = QtWidgets.QWidget()
        self.tabWidgetPage8.setObjectName("tabWidgetPage8")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.tabWidgetPage8)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_13 = QtWidgets.QLabel(self.tabWidgetPage8)
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("zdjecia/inps.png"))
        self.label_13.setObjectName("label_13")
        self.verticalLayout_13.addWidget(self.label_13, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.lineEdit = QtWidgets.QLineEdit(self.tabWidgetPage8)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_13.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tabWidgetPage8)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_13.addWidget(self.lineEdit_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.tabWidgetPage8)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("zdjecia/infoooo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon10)
        self.pushButton_5.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.Ui_dzisioj)
        self.verticalLayout_13.addWidget(self.pushButton_5)
        self.pushButton_17 = QtWidgets.QPushButton(self.tabWidgetPage8)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("zdjecia/generate2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_17.setIcon(icon11)
        self.pushButton_17.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_17.clicked.connect(self.Ui_otworzCod)
        self.verticalLayout_13.addWidget(self.pushButton_17)
        self.pushButton_15 = QtWidgets.QPushButton(self.tabWidgetPage8)
        self.pushButton_15.setIcon(icon3)
        self.pushButton_15.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.clicked.connect(self.Ui_ZapiszCOD)
        self.verticalLayout_13.addWidget(self.pushButton_15)
        self.tableWidget_25 = QtWidgets.QTableWidget(self.tabWidgetPage8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_25.sizePolicy().hasHeightForWidth())
        self.tableWidget_25.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tableWidget_25.setPalette(palette)
        self.tableWidget_25.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget_25.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_25.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_25.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_25.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_25.setAlternatingRowColors(False)
        self.tableWidget_25.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_25.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_25.setShowGrid(True)
        self.tableWidget_25.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_25.setObjectName("tableWidget_25")
        self.tableWidget_25.setColumnCount(16)
        self.tableWidget_25.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_25.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_25.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_25.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_25.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_25.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_25.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_25.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_25.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_25.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_25.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_25.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_25.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_25.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_25.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_25.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_25.setHorizontalHeaderItem(15, item)
        self.tableWidget_25.horizontalHeader().setVisible(False)
        self.tableWidget_25.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_25.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_25.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_25.verticalHeader().setVisible(False)
        self.tableWidget_25.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_25.verticalHeader().setHighlightSections(False)
        self.tableWidget_25.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_13.addWidget(self.tableWidget_25)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("zdjecia/inpost.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabWidgetPage8, icon12, "")
        self.tabWidgetPage9 = QtWidgets.QWidget()
        self.tabWidgetPage9.setObjectName("tabWidgetPage9")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.tabWidgetPage9)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_14 = QtWidgets.QLabel(self.tabWidgetPage9)
        self.label_14.setTextFormat(QtCore.Qt.RichText)
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_14.addWidget(self.label_14, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_15 = QtWidgets.QLabel(self.tabWidgetPage9)
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("zdjecia/Suder.ico"))
        self.label_15.setObjectName("label_15")
        self.verticalLayout_14.addWidget(self.label_15, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tabWidgetPage9)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setClearButtonEnabled(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_14.addWidget(self.lineEdit_11)
        self.pushButton_18 = QtWidgets.QPushButton(self.tabWidgetPage9)
        self.pushButton_18.setText("")
        self.pushButton_18.setIcon(icon1)
        self.pushButton_18.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_18.clicked.connect(self.Ui_szukaj_DE)
        self.verticalLayout_14.addWidget(self.pushButton_18)
        self.pushButton_2 = QtWidgets.QPushButton(self.tabWidgetPage9)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.Ui_zapiszDE)
        self.verticalLayout_14.addWidget(self.pushButton_2)
        self.pushButton_8 = QtWidgets.QPushButton(self.tabWidgetPage9)
        self.pushButton_8.setIcon(icon11)
        self.pushButton_8.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.Ui_zaladujStanDE)
        self.verticalLayout_14.addWidget(self.pushButton_8)
        self.tableWidget = QtWidgets.QTableWidget(self.tabWidgetPage9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tableWidget.setPalette(palette)
        self.tableWidget.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_14.addWidget(self.tableWidget)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("zdjecia/Suder.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabWidgetPage9, icon13, "")
        self.tabWidgetPage10 = QtWidgets.QWidget()
        self.tabWidgetPage10.setObjectName("tabWidgetPage10")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.tabWidgetPage10)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_16 = QtWidgets.QLabel(self.tabWidgetPage10)
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("zdjecia/order-shipped.png"))
        self.label_16.setObjectName("label_16")
        self.verticalLayout_16.addWidget(self.label_16, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tabWidgetPage10)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setClearButtonEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_16.addWidget(self.lineEdit_3)
        self.pushButton = QtWidgets.QPushButton(self.tabWidgetPage10)
        self.pushButton.setText("")
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Ui_szukaj_listu_tracking)
        self.verticalLayout_16.addWidget(self.pushButton)
        self.pushButton_11 = QtWidgets.QPushButton(self.tabWidgetPage10)
        self.pushButton_11.setIcon(icon11)
        self.pushButton_11.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(self.zaladujTracking)
        self.verticalLayout_16.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.tabWidgetPage10)
        self.pushButton_12.setIcon(icon3)
        self.pushButton_12.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(self.Ui_zapiszTracking)
        self.verticalLayout_16.addWidget(self.pushButton_12)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tabWidgetPage10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tableWidget_2.setPalette(palette)
        self.tableWidget_2.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setAlternatingRowColors(False)
        self.tableWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.verticalHeader().setHighlightSections(False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_16.addWidget(self.tableWidget_2)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("zdjecia/courier.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabWidgetPage10, icon14, "")
        self.verticalLayout_9.addWidget(self.tabWidget)
        self.label_10 = QtWidgets.QLabel(self.frame_content)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_9.addWidget(self.label_10)
        self.verticalLayout_4.addWidget(self.frame_content)
        self.frame_grip = QtWidgets.QFrame(self.frame_content_right)
        self.frame_grip.setMinimumSize(QtCore.QSize(0, 25))
        self.frame_grip.setMaximumSize(QtCore.QSize(16777215, 25))
        self.frame_grip.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grip.setObjectName("frame_grip")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_label_bottom = QtWidgets.QFrame(self.frame_grip)
        self.frame_label_bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_bottom.setObjectName("frame_label_bottom")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_credits = QtWidgets.QLabel(self.frame_label_bottom)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_credits.setObjectName("label_credits")
        self.horizontalLayout_7.addWidget(self.label_credits)
        self.label_version = QtWidgets.QLabel(self.frame_label_bottom)
        self.label_version.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_version.setFont(font)
        self.label_version.setStyleSheet("color: rgb(98, 103, 111);")
        self.label_version.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_version.setObjectName("label_version")
        self.horizontalLayout_7.addWidget(self.label_version)
        self.horizontalLayout_6.addWidget(self.frame_label_bottom)
        self.frame_size_grip = QtWidgets.QFrame(self.frame_grip)
        self.frame_size_grip.setMaximumSize(QtCore.QSize(20, 20))
        self.frame_size_grip.setStyleSheet("QSizeGrip {\n"
"    background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_size_grip.setObjectName("frame_size_grip")
        self.horizontalLayout_6.addWidget(self.frame_size_grip)
        self.verticalLayout_4.addWidget(self.frame_grip)
        self.horizontalLayout_2.addWidget(self.frame_content_right)
        self.verticalLayout.addWidget(self.frame_center)
        self.horizontalLayout.addWidget(self.frame_main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "STARSYSTEM POLAND"))
        self.label_title_bar_top.setText(_translate("MainWindow", "<html><head/><body><p>STARSYSTEM POLAND INTEGRATED SYSTEM</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "STAR SYSTEM"))
        self.label.setText(_translate("MainWindow", "Obsługa zewnętrznych platform E-Commerce"))
        self.label_7.setText(_translate("MainWindow", "V.12-2020"))
        self.tableWidget_66.setSortingEnabled(False)
        item = self.tableWidget_66.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableWidget_66.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Sposób płatności"))
        item = self.tableWidget_66.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Czy pobranie?"))
        item = self.tableWidget_66.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status zam."))
        item = self.tableWidget_66.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Dostawa"))
        item = self.tableWidget_66.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Cena dos."))
        item = self.tableWidget_66.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Data złoż. zam."))
        item = self.tableWidget_66.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Więcej informacji"))
        item = self.tableWidget_66.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Rodzaj faktury"))
        item = self.tableWidget_66.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Nick"))
        item = self.tableWidget_66.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Numer fv."))
        item = self.tableWidget_66.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "List przew."))
        item = self.tableWidget_66.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Całkowita kwot. za zam."))
        item = self.tableWidget_66.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "SMS od klienta."))
        item = self.tableWidget_66.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Numer płatności"))
        item = self.tableWidget_38.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Zdjęcie"))
        item = self.tableWidget_38.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableWidget_38.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nazwa"))
        item = self.tableWidget_38.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "SKU"))
        item = self.tableWidget_38.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Ilość"))
        item = self.tableWidget_38.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Cena"))
        item = self.tableWidget_38.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Dostawa"))
        item = self.tableWidget_38.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Całkowita kwota za zam."))
        item = self.tableWidget_37.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Imię"))
        item = self.tableWidget_37.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nazwisko"))
        item = self.tableWidget_37.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Miasto"))
        item = self.tableWidget_37.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Ul"))
        item = self.tableWidget_37.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Kod"))
        item = self.tableWidget_37.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Telefon"))
        item = self.tableWidget_37.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget_40.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Miasto"))
        item = self.tableWidget_40.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ul"))
        item = self.tableWidget_40.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Kod"))
        item = self.tableWidget_40.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Firma"))
        item = self.tableWidget_40.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Nip"))
        self.pushButton_6.setText(_translate("MainWindow", "Zapisz do pliku"))
        self.tableWidget_7.setSortingEnabled(False)
        item = self.tableWidget_7.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Data wpływu na konto"))
        item = self.tableWidget_7.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Kwota całościowa"))
        item = self.tableWidget_7.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "FV"))
        item = self.tableWidget_7.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Kwota wpływu"))
        item = self.tableWidget_7.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Nick"))
        item = self.tableWidget_7.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "List przewozowy"))
        self.pushButton_7.setText(_translate("MainWindow", "Zapisz do pliku"))
        self.tableWidget_8.setSortingEnabled(False)
        item = self.tableWidget_8.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Data wpływu na konto"))
        item = self.tableWidget_8.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Kwota całościowa"))
        item = self.tableWidget_8.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "FV"))
        item = self.tableWidget_8.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Kwota wpływu"))
        item = self.tableWidget_8.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Nick"))
        item = self.tableWidget_8.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "List przewozowy"))
        self.pushButton_19.setText(_translate("MainWindow", "Zapisz do pliku"))
        self.tableWidget_9.setSortingEnabled(False)
        item = self.tableWidget_9.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Data wpływu na konto"))
        item = self.tableWidget_9.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Kwota zwrotu"))
        item = self.tableWidget_9.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "FV"))
        item = self.tableWidget_9.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Saldo po operacji"))
        item = self.tableWidget_9.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Nick"))
        item = self.tableWidget_9.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "List przewozowy"))
        self.pushButton_4.setText(_translate("MainWindow", "Wczytaj dane z pliku"))
        self.pushButton_9.setText(_translate("MainWindow", "Zapisz do pliku"))
        self.tableWidget_32.setSortingEnabled(False)
        item = self.tableWidget_32.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "0"))
        item = self.tableWidget_32.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_32.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_32.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget_32.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget_32.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget_32.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget_32.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget_32.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget_32.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "9"))
        self.pushButton_14.setText(_translate("MainWindow", "Wczytaj dane z pliku"))
        self.pushButton_20.setText(_translate("MainWindow", "Zapisz dane do pliku"))
        self.tableWidget_34.setSortingEnabled(False)
        item = self.tableWidget_34.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "0"))
        item = self.tableWidget_34.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_34.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_34.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget_34.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget_34.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget_34.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget_34.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget_34.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget_34.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "9"))
        self.pushButton_5.setText(_translate("MainWindow", "Dzisiejsza data"))
        self.pushButton_17.setText(_translate("MainWindow", "Generuj dane"))
        self.pushButton_15.setText(_translate("MainWindow", "Zapisz dane do pliku"))
        self.tableWidget_25.setSortingEnabled(False)
        item = self.tableWidget_25.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Data"))
        item = self.tableWidget_25.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nr klienta"))
        item = self.tableWidget_25.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nadawca"))
        item = self.tableWidget_25.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Odbiorca"))
        item = self.tableWidget_25.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Kod"))
        item = self.tableWidget_25.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "List przewozowy"))
        item = self.tableWidget_25.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Data nadania"))
        item = self.tableWidget_25.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Data doręczenia"))
        item = self.tableWidget_25.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Kwota"))
        item = self.tableWidget_25.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Nick"))
        item = self.tableWidget_25.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Ref"))
        item = self.tableWidget_25.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "MPK"))
        item = self.tableWidget_25.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Kwota"))
        item = self.tableWidget_25.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Nick"))
        item = self.tableWidget_25.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "FV"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">Płatności Digitland Enterprise</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Zapisz dane do pliku"))
        self.pushButton_8.setText(_translate("MainWindow", "Generuj dane"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Data FV"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Termin"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Do wpłaty"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Data"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Wpłata kwota"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "FV"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Pozostało do spłaty"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Przewoźnik"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Status"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Nick"))
        self.pushButton_11.setText(_translate("MainWindow", "Generuj dane"))
        self.pushButton_12.setText(_translate("MainWindow", "Zapisz dane do pliku"))
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Typ kuriera"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "List przewozowy"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Id zam."))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Uwagi"))
        self.label_credits.setText(_translate("MainWindow", "Informacje dotyczące funkcjonowania aplikacji proszę kierować na e-mail: m.dudziak@suder.eu lub telefonicznie: 12 291 2376"))
        self.label_version.setText(_translate("MainWindow", "v12-2020"))
        print("Czas włączania programu to ok. 3 minuty, proszę o cierpliwość. Na poniższym pasku widnieję stan ładowania programu, załadowany program to 6/6it")
        curdate = str(date.today().strftime('%d-%m-%Y'))
        curmonth = str(date.today().strftime('%m'))
        path_to_json = 'jsons/'
        json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
        for index, js in tqdm(enumerate(json_files),desc="6/", colour="green"):       
                        with open(os.path.join(path_to_json,js)) as json_file:
                            datas = json.load(json_file)
                            try:
                                for p in datas['checkoutForms']:
                                                row_numer6= self.tableWidget_66.rowCount()
                                                self.tableWidget_66.insertRow(row_numer6)
                                                try:
                                                    d = datetime.datetime.strptime(p['lineItems'][0]['boughtAt'], '%Y-%m-%dT%H:%M:%S.%fZ')
                                                    x = datetime.date.strftime(d , "%d-%m-%Y")
                                                    x2 = datetime.date.strftime(d , "%m")
                                                except:
                                                    pass
                                                                                                
                                                try:        
                                                    #ARCHIWUM---------------------------------------------------------------------------------------------------------------------------------------
                                                        d = datetime.datetime.strptime(p['lineItems'][0]['boughtAt'], '%Y-%m-%dT%H:%M:%S.%fZ')
                                                        x = datetime.date.strftime(d , "%d-%m-%Y")
                                                        
                                                        self.tableWidget_66.setItem(row_numer6,0,QTableWidgetItem(p['id']))
                                                        self.tableWidget_66.setItem(row_numer6,14,QTableWidgetItem(p['payment']['id']))
                                                                                                 
                                                        if p['payment']['type']=='CASH_ON_DELIVERY':
                                                                self.tableWidget_66.setItem(row_numer6,2,QTableWidgetItem('TAK'))
                                                        elif p['payment']['type']=='ONLINE':
                                                                self.tableWidget_66.setItem(row_numer6,2,QTableWidgetItem('NIE'))
                                                        else:
                                                                self.tableWidget_66.setItem(row_numer6,2,QTableWidgetItem('NIEZNANE'))
                                                                
                                                        if p['payment']['provider'] is not None:  
                                                            self.tableWidget_66.setItem(row_numer6,1,QTableWidgetItem(p['payment']['provider']))
                                                        else:
                                                            self.tableWidget_66.setItem(row_numer6,1,QTableWidgetItem('POBRANIE'))
                                                            self.tableWidget_66.item(row_numer6,1).setBackground(QColor('orange'))
                                                        if p['status']=='READY_FOR_PROCESSING':                      
                                                                self.tableWidget_66.setItem(row_numer6,3,QTableWidgetItem('Zatwierdzone'))
                                                                self.tableWidget_66.item(row_numer6,3).setBackground(QColor('green'))
                                                        else:
                                                                self.tableWidget_66.setItem(row_numer6,3,QTableWidgetItem('Nieznany'))
                                                                self.tableWidget_66.item(row_numer6,3).setBackground(QColor('red'))
                                                            
                                                        self.tableWidget_66.setItem(row_numer6,4,QTableWidgetItem(p['delivery']['method']['name']))
                                                        self.tableWidget_66.setItem(row_numer6,5,QTableWidgetItem(p['delivery']['cost']['amount']))
                                                        d = datetime.datetime.strptime(p['lineItems'][0]['boughtAt'], '%Y-%m-%dT%H:%M:%S.%fZ')
                                                        s = datetime.date.strftime(d , "%d-%m-%Y | %H:%M:%S")
                                                        dm = datetime.date.strftime(d, "%d-%m-%Y")
                                                        self.tableWidget_66.setItem(row_numer6,6,QTableWidgetItem(s))
                                                        if curdate == dm:
                                                            self.tableWidget_66.item(row_numer6,6).setBackground(QColor(234, 255, 0))
                                                        self.tableWidget_66.setItem(row_numer6,12,QTableWidgetItem(p['summary']['totalToPay']['amount']))
                                                        self.tableWidget_66.setCellWidget(row_numer6,7,NewWindowTest(p['id'],self.tableWidget_37,self.tableWidget_38,self.tableWidget_40))
                                                        
                                                        if(p['invoice']['required'] != True):
                                                                try:
                                                                    self.tableWidget_66.setItem(row_numer6,8,QTableWidgetItem('Paragon'))
                                                                    self.tableWidget_66.item(row_numer6,8).setBackground(QColor('lightgray'))
                                                                except Exception:
                                                                    pass
                                                        else:
                                                                self.tableWidget_66.setItem(row_numer6,8,QTableWidgetItem('FV - FIRMA'))
                                                                self.tableWidget_66.item(row_numer6,8).setBackground(QColor('pink'))
                                                                
                                                        self.tableWidget_66.setItem(row_numer6,9,QTableWidgetItem(p['buyer']['login']))
                                                        self.tableWidget_66.resizeColumnsToContents()
                                                        self.tableWidget_66.resizeRowsToContents()

                                                        con = cx_Oracle.connect('integracja_allegro/CzterejPancerni@192.168.1.4/orcl')
                                                        cur = con.cursor()
                                                        val = p['id']
                                                        cur = con.cursor()
                                                        sql="select ztr.ALLEGRO_INTEGRACJA_PROC.GetNrFaktury(:a) from dual"
                                                        cur.execute(sql,{'a' : val})
                                                        headers = {}
                                                        headers['charset'] = 'UTF-8'
                                                        headers['Accept-Language'] = 'pl-PL'
                                                        headers['Content-Type'] = 'application/vnd.allegro.public.v1+json'
                                                        headers['Api-Key'] = API_KEY
                                                        headers['Accept'] = 'application/vnd.allegro.public.v1+json'
                                                        headers['Authorization'] = "Bearer {}".format(sign2['access_token'])
                                                        tekst = str(p['id'])
                                                        try:
                                                            with requests.Session() as sesja:
                                                                         sesja.headers.update(headers)
                                                                         response = sesja.get('https://api.allegro.pl/order/checkout-forms/'+tekst+'/shipments')
                                                                         show = response.json()
                                                                         bilet = show['shipments'][0]['waybill']
                                                                         if bilet:
                                                                             self.tableWidget_66.setItem(row_numer6,11,QTableWidgetItem(bilet))
                                                                         else:
                                                                             self.tableWidget_66.setItem(row_numer6,11,QTableWidgetItem('nie wprowadzono listu'))
                                                        except:
                                                            pass
                                                            
                                                        for result in cur:
                                                            self.tableWidget_66.setItem(row_numer6,10,QTableWidgetItem(result[0]))
                                                        cur.close()
                                                        con.close()
                                                        
                                                except:      
                                                  pass

                            except:
                                pass


        


    
        curdate = str(date.today().strftime('%d-%m-%Y'))
        curmonth = str(date.today().strftime('%m'))
        path_to_json = 'jsons_platnosci/'
        json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
        for index, js in tqdm(enumerate(json_files),desc="4/", colour="green"):        
                        with open(os.path.join(path_to_json,js)) as json_file:
                            datas = json.load(json_file)
                            try:
                                for p in datas['paymentOperations']:
                                         row_numer = self.tableWidget_7.rowCount()
                                         self.tableWidget_7.insertRow(row_numer)
                                         row_numer2= self.tableWidget_8.rowCount()
                                         self.tableWidget_8.insertRow(row_numer2)
                                         row_numer3= self.tableWidget_9.rowCount()
                                         self.tableWidget_9.insertRow(row_numer3)

                                         try:
                                             if p['wallet']['paymentOperator']=='PAYU':
                                                 if p['group']=='OUTCOME':
                                                     self.tableWidget_7.setItem(row_numer,1,QTableWidgetItem(p['value']['amount'].replace('.',',')))
                                                     self.tableWidget_7.item(row_numer,1).setBackground(QColor('yellow'))
                                                     self.tableWidget_7.setItem(row_numer+1,2,QTableWidgetItem('========================'))
                                                     self.tableWidget_7.setItem(row_numer+1,3,QTableWidgetItem('========================'))
                                                     self.tableWidget_7.setItem(row_numer+1,4,QTableWidgetItem('========================'))
                                                     self.tableWidget_7.setItem(row_numer+1,5,QTableWidgetItem('========================'))
                                                                                     
                                                 d = datetime.datetime.strptime(p['occurredAt'], '%Y-%m-%dT%H:%M:%S.%fZ')
                                                 x = datetime.date.strftime(d , "%d-%m-%Y")
                                                 self.tableWidget_7.setItem(row_numer,0,QTableWidgetItem(x))
                                                 if p['group']=='INCOME' or p['group']=='REFUND':
                                                     self.tableWidget_7.setItem(row_numer,3,QTableWidgetItem(p['value']['amount'].replace('.',',')))
                                                     if p['participant']['login']:
                                                         self.tableWidget_7.setItem(row_numer,4,QTableWidgetItem(p['participant']['login']))
                                                     nickk = str(p['payment']['id'])
                                                     for i in range(self.tableWidget_66.rowCount()):
                                                             user = self.tableWidget_66.item(i,14)
                                                             if user is not None:
                                                                 userr = str(self.tableWidget_66.item(i,14).text())
                                                             
                                                                 if (nickk == userr):
                                                                     try:
                                                                        fv = self.tableWidget_66.item(i,10).text()
                                                                        self.tableWidget_7.setItem(row_numer,2,QTableWidgetItem(fv))
                                                                     except:
                                                                         pass
                                                         
                                                     nick = str(p['payment']['id'])
                                                     for i in range(self.tableWidget_66.rowCount()):
                                                             z = self.tableWidget_66.item(i,0)
                                                             zz = self.tableWidget_66.item(i,14)
                                                             if z is not None and zz is not None:
                                                                 text = str(z.text())
                                                                 user = str(zz.text())
                                                                 if (nick == user):
                                                                     try: 
                                                                         with requests.Session() as sesja:
                                                                              sesja.headers.update(headers)
                                                                              response = sesja.get('https://api.allegro.pl/order/checkout-forms/'+text+'/shipments')
                                                                              show = response.json()
                                                                              bilet = show['shipments'][0]['waybill']        
                                                                              self.tableWidget_7.setItem(row_numer,5,QTableWidgetItem(bilet))
                                                                     except:
                                                                              pass
                                                 self.tableWidget_7.resizeColumnsToContents()
                                                 self.tableWidget_7.resizeRowsToContents()
                                             else:
                                                 self.tableWidget_7.removeRow(row_numer)

                            
                                         except:
                                             pass
                                        
                                         #P24---------------------------------------------------------------------------------------------------------------------------------------
                                         try:
                                             if p['wallet']['paymentOperator']=='P24':
                                                 if p['group']=='OUTCOME':
                                                     self.tableWidget_8.setItem(row_numer2,1,QTableWidgetItem(p['value']['amount'].replace('.',',')))
                                                     self.tableWidget_8.item(row_numer2,1).setBackground(QColor('yellow'))
                                                     self.tableWidget_8.setItem(row_numer2+1,0,QTableWidgetItem('========================'))
                                                     self.tableWidget_8.setItem(row_numer2+1,1,QTableWidgetItem('========================'))
                                                     self.tableWidget_8.setItem(row_numer2+1,2,QTableWidgetItem('========================'))
                                                     self.tableWidget_8.setItem(row_numer2+1,3,QTableWidgetItem('========================'))
                                                     self.tableWidget_8.setItem(row_numer2+1,4,QTableWidgetItem('========================'))
                                                     self.tableWidget_8.setItem(row_numer2+1,5,QTableWidgetItem('========================'))


                                                 d = datetime.datetime.strptime(p['occurredAt'], '%Y-%m-%dT%H:%M:%S.%fZ')
                                                 x = datetime.date.strftime(d , "%d-%m-%Y")
                                                 self.tableWidget_8.setItem(row_numer2,0,QTableWidgetItem(x))
                                                 if p['group']=='INCOME' or p['group']=='REFUND':
                                                     self.tableWidget_8.setItem(row_numer2,3,QTableWidgetItem(p['value']['amount'].replace('.',',')))
                                                     nickk = str(p['payment']['id'])
                                                     for i in range(self.tableWidget_66.rowCount()):
                                                             user = self.tableWidget_66.item(i,14)
                                                             if user is not None:
                                                                 userr = str(self.tableWidget_66.item(i,14).text())
                                                             
                                                                 if (nickk == userr):
                                                                     try:
                                                                        fv = self.tableWidget_66.item(i,10).text()
                                                                        self.tableWidget_8.setItem(row_numer2,2,QTableWidgetItem(fv))
                                                                     except:
                                                                         pass
                                                 
                                                 if p['participant']['login']:
                                                     self.tableWidget_8.setItem(row_numer2,4,QTableWidgetItem(p['participant']['login']))
                                                 self.tableWidget_8.resizeColumnsToContents()
                                                 self.tableWidget_8.resizeRowsToContents()

                                                 nick = str(p['participant']['login'])
                                                 for i in range(self.tableWidget_66.rowCount()):
                                                     z = self.tableWidget_66.item(i,0)
                                                     zz = self.tableWidget_66.item(i,14)
                                                     if z is not None and zz is not None:
                                                                text = str(z.text())
                                                                user = str(zz.text())
                                                                if (nick == user):
                                                                 try:
                                                                     headers = {}
                                                                     headers['charset'] = 'UTF-8'
                                                                     headers['Accept-Language'] = 'pl-PL'
                                                                     headers['Content-Type'] = 'application/vnd.allegro.public.v1+json'
                                                                     headers['Api-Key'] = API_KEY
                                                                     headers['Accept'] = 'application/vnd.allegro.public.v1+json'
                                                                     headers['Authorization'] = "Bearer {}".format(sign2['access_token'])
  
                                                                     with requests.Session() as sesja:
                                                                          sesja.headers.update(headers)
                                                                          response = sesja.get('https://api.allegro.pl/order/checkout-forms/'+text+'/shipments')
                                                                          show = response.json()
                                                                          bilet = show['shipments'][0]['waybill']  
                                                                          self.tableWidget_8.setItem(row_numer2,5,QTableWidgetItem(bilet))
                                                                 except:
                                                                          pass
                                             else:
                                                 self.tableWidget_8.removeRow(row_numer2)

                                                 

                                         except:
                                             pass



                                         #Zwroty---------------------------------------------------------------------------------------------------------------------------------------
                                         try:
                                             if p['type']=='REFUND_CHARGE':
                                                 if p['group']=='REFUND':
                                                     d = datetime.datetime.strptime(p['occurredAt'], '%Y-%m-%dT%H:%M:%S.%fZ')
                                                     x = datetime.date.strftime(d , "%d-%m-%Y")
                                                     self.tableWidget_9.setItem(row_numer3,0,QTableWidgetItem(x))
                                                 
                                                     self.tableWidget_9.setItem(row_numer3,1,QTableWidgetItem(p['value']['amount'].replace('.',',')))
                                                     self.tableWidget_9.setItem(row_numer3,3,QTableWidgetItem(p['wallet']['balance']['amount']))
                                                     nickk = str(p['payment']['id'])
                                                     for i in range(self.tableWidget_66.rowCount()):
                                                        

                                                             user = self.tableWidget_66.item(i,14)
                                                             if user is not None:
                                                                 userr = str(self.tableWidget_66.item(i,14).text())
                                                             
                                                                 if (nickk == userr):
                                                                     try:
                                                                        fv = self.tableWidget_66.item(i,10).text()
                                                                        self.tableWidget_9.setItem(row_numer3,2,QTableWidgetItem(fv))
                                                                     except:
                                                                         pass
                                                     if p['participant']['login']:
                                                         self.tableWidget_9.setItem(row_numer3,4,QTableWidgetItem(p['participant']['login']))

                                                     nick = str(p['payment']['id'])
                                                     for i in range(self.tableWidget_66.rowCount()):
                                                             z = self.tableWidget_66.item(i,0)
                                                             zz = self.tableWidget_66.item(i,14)
                                                             if z is not None and zz is not None:
                                                                 text = str(z.text())
                                                                 user = str(zz.text())
                                                                 if (nick == user):
                                                                     try: 
                                                                         with requests.Session() as sesja:
                                                                              sesja.headers.update(headers)
                                                                              response = sesja.get('https://api.allegro.pl/order/checkout-forms/'+text+'/shipments')
                                                                              show = response.json()
                                                                              bilet = show['shipments'][0]['waybill']  
                                                                              self.tableWidget_9.setItem(row_numer3,5,QTableWidgetItem(bilet))
                                                                     except:
                                                                              pd
                                                 else:
                                                     self.tableWidget_9.removeRow(row_numer3)

                                                 self.tableWidget_9.resizeColumnsToContents()
                                                 self.tableWidget_9.resizeRowsToContents()
                                             else:
                                                 self.tableWidget_9.removeRow(row_numer3)

                                         except:
                                             pass
                            except:
                                pass

        
    def Ui_zaladujStanDE(self):
        for i in range(self.tableWidget_66.rowCount()):
            try:
                    fv = self.tableWidget_66.item(i,10)
                    if fv is not None:
                        con = cx_Oracle.connect('integracja_allegro/CzterejPancerni@192.168.1.4/orcl')
                        cur = con.cursor()
                        cur_var = cur.var(cx_Oracle.CURSOR)
                        val = str(fv.text())
                        val2 = val.split(' -')[0]
                        cur.callproc("ztr.ALLEGRO_INTEGRACJA_PROC.GetStanPlatnosciFaktury", [val2,cur_var])
                        data = cur_var.getvalue()
                        for result in data:
                                try:
                                    row_numer = self.tableWidget.rowCount()
                                    self.tableWidget.insertRow(row_numer)
                                    self.tableWidget.setItem(row_numer,5,QTableWidgetItem((str(result[0]))))
                                    self.tableWidget.setItem(row_numer,0,QTableWidgetItem((str(result[1]))))
                                    self.tableWidget.setItem(row_numer,2,QTableWidgetItem((str(result[2]))))
                                    self.tableWidget.setItem(row_numer,6,QTableWidgetItem((str(result[2]))))
                                    self.tableWidget.setItem(row_numer,4,QTableWidgetItem((str(result[5]))))                      
                                    self.tableWidget.setItem(row_numer,3,QTableWidgetItem((str(result[10]))))
                                    

                                except:
                                    pass
                        cur.close()
                        con.close()
            except:
                pass

        z = self.tableWidget_66.rowCount()
        for i in range(z):
            try:
                        
                        faktura = self.tableWidget_66.item(i,10)
                        zz = self.tableWidget.rowCount()
                        for v in range(zz):
                                fv = self.tableWidget.item(v,5)
                                if faktura is not None and fv is not None:
                                    fakt = str(faktura.text())
                                    fvv = str(fv.text())
                                    if fvv in fakt:
                                                listy= self.tableWidget_66.item(i,11)
                                                nick = self.tableWidget_66.item(i,9)
                                                self.tableWidget.setItem(v,7,QTableWidgetItem(str(listy.text())))
                                                self.tableWidget.setItem(v,8,QTableWidgetItem(str(nick.text())))
                                    else:
                                        pass
            except:
                pass

    def zaladujTracking(self):
    
        token = '1001278-1006030-UOAO7B9BMMHVUIMXZDOII1SIQOFACPYZD9FOU0WKLG3LOLC5X2GNHQXA9ZER1TY1'
        token_url = 'https://api.baselinker.com/connector.php'
        idd = str('bl_1')
        parametry = {
                    "date_confirmed_from":"",
                    }
        data = json.dumps(parametry)

        headers = {}
        headers['Host'] = 'https://api.baselinker.com/connector.php'
        headers['Content-Type'] = 'application/json'
        headers['token'] = token
        headers['method'] = 'getOrders'
        headers['parameters'] = data


        response = requests.post(token_url,headers)
        t= response.json()
        with open('jsons_bl/data.json','w') as outfile:
                json.dump(t, outfile)

        for p in t['orders']:
            
            order = str(p['order_id'])
            row_numer = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row_numer)
            self.tableWidget_2.setItem(row_numer,3,QTableWidgetItem(order))
            parametr = { "order_id" : order}
            datas = json.dumps(parametr)
            headers = {}
            headers['Host'] = 'https://api.baselinker.com/connector.php'
            headers['Content-Type'] = 'application/json'
            headers['token'] = token
            headers['method'] = 'getOrderPackages'
            headers['parameters'] = datas


            response = requests.post(token_url,headers)
            t= response.json()
            with open('jsons_bl/data2.json','w') as outfile:
                    json.dump(t, outfile)
            for p in t['packages']:
                
                order = str(p['courier_package_nr'])
                orderstatus = str(p['tracking_status'])
                statuskuriera = str(p['courier_code'])
                self.tableWidget_2.setItem(row_numer,1,QTableWidgetItem(order))
                if orderstatus==str("0"):
                    self.tableWidget_2.setItem(row_numer,2,QTableWidgetItem("Nieznany"))
                elif orderstatus==str("1"):
                    self.tableWidget_2.setItem(row_numer,2,QTableWidgetItem("Zarejestrowana u kuriera"))
                elif orderstatus==str("2"):
                    self.tableWidget_2.setItem(row_numer,2,QTableWidgetItem("Przekazane kurierowi"))
                elif orderstatus==str("3"):
                    self.tableWidget_2.setItem(row_numer,2,QTableWidgetItem("Nie dostarczono"))
                elif orderstatus==str("4"):
                    self.tableWidget_2.setItem(row_numer,2,QTableWidgetItem("Wydano do doręczenia"))
                elif orderstatus==str("5"):
                    self.tableWidget_2.setItem(row_numer,2,QTableWidgetItem("Dostarczono"))
                elif orderstatus==str("6"):
                    self.tableWidget_2.setItem(row_numer,2,QTableWidgetItem("Zwrot"))
                elif orderstatus==str("7"):
                    self.tableWidget_2.setItem(row_numer,2,QTableWidgetItem("Awizo"))
                elif orderstatus==str("8"):
                    self.tableWidget_2.setItem(row_numer,2,QTableWidgetItem("Oczekuje w punkcie"))
                elif orderstatus==str("9"):
                    self.tableWidget_2.setItem(row_numer,2,QTableWidgetItem("Zagubiona"))
                elif orderstatus==str("10"):
                    self.tableWidget_2.setItem(row_numer,2,QTableWidgetItem("Anulowana"))
                elif orderstatus==str("11"):
                    self.tableWidget_2.setItem(row_numer,2,QTableWidgetItem("W drodze"))
                self.tableWidget_2.setItem(row_numer,0,QTableWidgetItem(statuskuriera))

    def Ui_zaladujZakladkaInpost(self):
        curdate = str(date.today().strftime('%d-%m-%Y'))
        curmonth = str(date.today().strftime('%m'))
        path_to_json = 'jsons/'
        json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
        for index, js in enumerate(json_files):       
                        with open(os.path.join(path_to_json,js)) as json_file:
                            datas = json.load(json_file)
                            try:
                                for p in datas['checkoutForms']:
                                            row_numer5 = self.tableWidget_6.rowCount()
                                            self.tableWidget_6.insertRow(row_numer5)
                                            try:
                                                d = datetime.datetime.strptime(p['lineItems'][0]['boughtAt'], '%Y-%m-%dT%H:%M:%S.%fZ')
                                                x = datetime.date.strftime(d , "%d-%m-%Y")
                                                x2 = datetime.date.strftime(d , "%m")
                                            except:
                                                pass
                                                                    
                                            #INPOST---------------------------------------------------------------------------------------------------------------------------------------
                                            try:
                                                    if (p['delivery']['method']['name']=='Allegro Paczkomaty 24/7 InPost'
                                                    or p['delivery']['method']['name']=='Allegro miniKurier24 InPost'
                                                    or p['delivery']['method']['name']=='Allegro miniKurier24 InPost pobranie'
                                                    or p['delivery']['method']['name']=='Allegro Paczkomaty 24/7 InPost pobranie'):
                                                                                        
                                                        self.tableWidget_6.setItem(row_numer5,0,QTableWidgetItem(p['buyer']['login']))
                                                                                              
                                                        self.tableWidget_6.setItem(row_numer5,1,QTableWidgetItem(p['delivery']['address']['firstName']))
                                                                                                
                                                        self.tableWidget_6.setItem(row_numer5,2,QTableWidgetItem(p['delivery']['address']['lastName']))
                                                                                                
                                                        self.tableWidget_6.setItem(row_numer5,3,QTableWidgetItem(p['delivery']['method']['name']))
                                                                                           
                                                        self.tableWidget_6.setItem(row_numer5,4,QTableWidgetItem(p['delivery']['cost']['amount'].replace('.',',')))
                                                                                            
                                                        d = datetime.datetime.strptime(p['lineItems'][0]['boughtAt'], '%Y-%m-%dT%H:%M:%S.%fZ')
                                                        x = datetime.date.strftime(d , "%d-%m-%Y")

                                                        self.tableWidget_6.setItem(row_numer5,5,QTableWidgetItem(x))
                                                        self.tableWidget_6.resizeColumnsToContents()
                                                        self.tableWidget_6.resizeRowsToContents()
                                                    else:
                                                        self.tableWidget_6.removeRow(row_numer5)

                                            except:
                                                pass
                            except:
                                    pass

    def Ui_zaladujZakladkaPobranie(self):
        curdate = str(date.today().strftime('%d-%m-%Y'))
        curmonth = str(date.today().strftime('%m'))
        path_to_json = 'jsons/'
        json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
        for index, js in enumerate(json_files):       
                        with open(os.path.join(path_to_json,js)) as json_file:
                            datas = json.load(json_file)
                            try:
                                for p in datas['checkoutForms']:
                                            row_numer33 = self.tableWidget_4.rowCount()
                                            self.tableWidget_4.insertRow(row_numer33)
                                            try:
                                                d = datetime.datetime.strptime(p['lineItems'][0]['boughtAt'], '%Y-%m-%dT%H:%M:%S.%fZ')
                                                x = datetime.date.strftime(d , "%d-%m-%Y")
                                                x2 = datetime.date.strftime(d , "%m")
                                            except:
                                                pass

                                         #ZA POBRANIEM / ZESTAWIENIE --------------------------------------------------------------------------------------------
                                            try:
                                                if p['delivery']['method']['name']=='Kurier DPD pobranie' or p['delivery']['method']['name']=='Kurier FedEx pobraniowy' or p['delivery']['method']['name']=='Kurier FedEx pobranie' or p['delivery']['method']['name']=='Allegro Paczkomaty 24/7 InPost pobranie' or p['delivery']['method']['name']=='Allegro miniKurier24 InPost pobranie' or p['delivery']['method']['name']=='Allegro Kurier24 InPost pobranie':
                                                        x2 = datetime.date.strftime(d , "%m")
                                                        self.tableWidget_4.setItem(row_numer33,0,QTableWidgetItem(p['id']))
    
                                                        con = cx_Oracle.connect('integracja_allegro/CzterejPancerni@192.168.1.4/orcl')
                                                        cur = con.cursor()
                                                        val = p['id']
                                                        cur = con.cursor()
                                                        sql="select ztr.ALLEGRO_INTEGRACJA_PROC.GetNrFaktury(:a) from dual"
                                                        cur.execute(sql,{'a' : val})
                                                        tekst = str(p['id'])
                                                        headers = {}
                                                        headers['charset'] = 'UTF-8'
                                                        headers['Accept-Language'] = 'pl-PL'
                                                        headers['Content-Type'] = 'application/vnd.allegro.public.v1+json'
                                                        headers['Api-Key'] = API_KEY
                                                        headers['Accept'] = 'application/vnd.allegro.public.v1+json'
                                                        headers['Authorization'] = "Bearer {}".format(sign2['access_token'])
                                                        tekst = str(p['id'])
                                                        with requests.Session() as sesja:
                                                                 sesja.headers.update(headers)
                                                                 response = sesja.get('https://api.allegro.pl/order/checkout-forms/'+tekst+'/shipments')
                                                                 show = response.json()
                                                                 bilet = show['shipments'][0]['waybill']       
                                                                 self.tableWidget_4.setItem(row_numer33,9,QTableWidgetItem(bilet))

                                                        for result in cur:
                                                            if p['id']:
                                                                self.tableWidget_4.setItem(row_numer33,8,QTableWidgetItem(result[0]))

                                                        cur.close()
                                                        con.close()
                                                                
                                                        if p['payment']['type']=='CASH_ON_DELIVERY':
                                                            self.tableWidget_4.setItem(row_numer33,1,QTableWidgetItem('Płatność przy odbiorze'))
                                                            
                                                        if p['status']=='READY_FOR_PROCESSING':                                 
                                                            self.tableWidget_4.setItem(row_numer33,2,QTableWidgetItem('Zapłacono'))
                                                            self.tableWidget_4.setItem(row_numer33,3,QTableWidgetItem(p['delivery']['method']['name']))
                                                            self.tableWidget_4.setItem(row_numer33,4,QTableWidgetItem(p['delivery']['cost']['amount']))
                                                            d = datetime.datetime.strptime(p['lineItems'][0]['boughtAt'], '%Y-%m-%dT%H:%M:%S.%fZ')
                                                            x = datetime.date.strftime(d , "%d-%m-%Y")
                                                            self.tableWidget_4.setItem(row_numer33,5,QTableWidgetItem(x))   
                                                            if(p['invoice']['required'] != True):
                                                                try:
                                                                    self.tableWidget_4.setItem(row_numer33,6,QTableWidgetItem('PARAGON'))
                                                                    self.tableWidget_4.item(row_numer33,6).setBackground(QColor('lightgrey'))
                                                                except Exception:
                                                                    pass
                                                
                                                            else:
                                                                self.tableWidget_4.setItem(row_numer33,6,QTableWidgetItem('FAKTURA'))
                                                                self.tableWidget_4.item(row_numer33,6).setBackground(QColor('lightgreen'))
                                                            
                                                            self.tableWidget_4.setItem(row_numer33,7,QTableWidgetItem(p['buyer']['login']))
                                                            self.tableWidget_4.resizeColumnsToContents()
                                                            self.tableWidget_4.resizeRowsToContents()
                                                        else:
                                                                pass
                                 
                                                        self.tableWidget_4.resizeColumnsToContents()
                                                        self.tableWidget_4.resizeRowsToContents()
                                                        self.tableWidget_4.resizeColumnsToContents()
                                                        self.tableWidget_4.resizeRowsToContents()
                                                        self.pushButton_9.clicked.connect(self.Ui_OnFilter3)

                                                        self.pushButton_16.clicked.connect(self.Ui_ZapiszZaPobraniem)
                                                        self.pushButton_31.clicked.connect(self.Ui_OnFilterPobranie)

                                                        
                                                    

                                                else:
                                                    self.tableWidget_4.removeRow(row_numer33)

                                            except:
                                                pass
                            except:
                                    pass
    def Ui_zaladujTowary(self):
        con = cx_Oracle.connect('integracja_allegro/CzterejPancerni@192.168.1.4/orcl')
        cur = con.cursor()
        sql='select t.indeks,t.skrot,t.nazwa_pl,t.KOD_WG_DOST,t.pozostale_kody,t.cena_detal_netto,t.zdjecie_link,t.producer_name from ztr.allegro_api_v_rejestr_towarow t'
        cur.execute(sql)
        for result in cur:
            row_numer23 = self.tableWidget_5.rowCount()
            self.tableWidget_5.insertRow(row_numer23)
            self.tableWidget_5.setItem(row_numer23,0,QTableWidgetItem(str(result[0])))
            self.tableWidget_5.setItem(row_numer23,1,QTableWidgetItem(str(result[1])))
            self.tableWidget_5.setItem(row_numer23,2,QTableWidgetItem(str(result[2])+''+str(result[7])))
            self.tableWidget_5.setItem(row_numer23,3,QTableWidgetItem(str(result[3])))
            self.tableWidget_5.setItem(row_numer23,4,QTableWidgetItem(str(result[4])))
            self.tableWidget_5.setItem(row_numer23,5,QTableWidgetItem(str(result[5])))
            self.tableWidget_5.setItem(row_numer23,6,QTableWidgetItem(str(result[6])))
            self.tableWidget_5.setItem(row_numer23,11,QTableWidgetItem(str(result[7])))
            cena_str = str(result[5])
            cena = float(cena_str)
            mnoznik = cena*1.23
            cena_final = round(mnoznik,2)
            self.tableWidget_5.setItem(row_numer23,5,QTableWidgetItem(str(cena_final)))
            cur = con.cursor()
            cur_var = cur.var(cx_Oracle.CURSOR)
            lac = self.tableWidget_5.item(row_numer23,0)
            txt = lac.text()
            cur.callproc("ztr.allegro_integracja_proc.GetParametryTowaru", [txt, cur_var])
            data = cur_var.getvalue()
            entries = []
            for result in data:
                try:
                    if(str(result[1])==str('121')):
                        self.tableWidget_5.setItem(row_numer23,7,QTableWidgetItem(str(result[3])))
                    elif(str(result[1])==str('62')):
                        self.tableWidget_5.setItem(row_numer23,8,QTableWidgetItem(str(result[3])))
                    elif(str(result[1])==str('61')):
                        self.tableWidget_5.setItem(row_numer23,9,QTableWidgetItem(str(result[3])))
                    elif(str(result[1])==str('21')):
                        self.tableWidget_5.setItem(row_numer23,10,QTableWidgetItem(str(result[3])))
                except:
                     pass
            cur = con.cursor()
            cur_cursor = cur.var(cx_Oracle.CURSOR)
            p_indeks = self.tableWidget_5.item(row_numer23,0)
            text_indeks = p_indeks.text()
            test = cur.callproc("ztr.ALLEGRO_INTEGRACJA_PROC.GetKodEAN",[text_indeks,cur_cursor])
            data123 = cur_cursor.getvalue()
            for ready2 in data123:
                try:
                    x = str(ready2)
                    tx = x.replace('(','')
                    txx = tx.replace(')','')
                    tx3 = txx.replace(',','')
                    self.tableWidget_5.setItem(row_numer23,12,QTableWidgetItem(str(tx3)))
                except:
                    pass
                    
            cur = con.cursor()
            cur_cursor = cur.var(cx_Oracle.CURSOR)
            p_indeks = self.tableWidget_5.item(row_numer23,0)
            text_indeks = p_indeks.text()
            test = cur.callproc("ztr.ALLEGRO_INTEGRACJA_PROC.GetPojazdyDlaTowaru",[text_indeks,cur_cursor])
            data = cur_cursor.getvalue()
            for ready in data:
                try:
                    row_numer233 = self.tableWidget_10.rowCount()
                    self.tableWidget_10.insertRow(row_numer233)
                    self.tableWidget_10.setItem(row_numer233,0,QTableWidgetItem(str(ready[3:8])))
                    test = self.tableWidget_10.item(row_numer233,0)
                    testtxt = test.text()
                    self.tableWidget_10.setItem(row_numer233,1,QTableWidgetItem(str(ready[0])))
                except:
                    pass

    def Ui_otworzFCodSEND(self):
        try:
            for i in range(self.tableWidget_32.rowCount()):
                data = self.tableWidget_32.item(i,2)
                wplata = self.tableWidget_32.item(i,7)
                fv = self.tableWidget_32.item(i,8)
                ps = self.tableWidget_32.item(i,7)
                nick = self.tableWidget_32.item(i,9)
                row_numer = self.tableWidget_33.rowCount()
                self.tableWidget_33.insertRow(row_numer)
                if data is not None:
                    self.tableWidget_33.setItem(row_numer,0,QTableWidgetItem(str(data.text())))
                if wplata is not None:
                    self.tableWidget_33.setItem(row_numer,1,QTableWidgetItem(str(wplata.text())))
                if fv is not None:
                    self.tableWidget_33.setItem(row_numer,2,QTableWidgetItem(str(fv.text())))
                if ps is not None:
                    self.tableWidget_33.setItem(row_numer,3,QTableWidgetItem(str(ps.text())))
                if nick is not None:
                    self.tableWidget_33.setItem(row_numer,4,QTableWidgetItem(str(nick.text())))
        except:
            self.tableWidget_33.removeRow()
    def Ui_otworzFCod(self):
        try:
            Tk().withdraw() 
            filename = askopenfilename()
            print(filename)
            df = pd.read_excel(filename)
            self.tableWidget_32.setRowCount(len(df.index))
            for m in range(len(df.index)):
                    for j in range (len(df.columns)):
                        try:
                             if str(df.iat[m,j]) == 'nan':
                                 self.tableWidget_32.setItem(m,j,QTableWidgetItem(str('')))
                             else:
                                 self.tableWidget_32.setItem(m,j,QTableWidgetItem(str(df.iat[m,j])))
                        except:
                            pass

       
            i = self.tableWidget_32.rowCount()
            z = self.tableWidget_66.rowCount()
            for x in range(z):
                listy = self.tableWidget_66.item(x,11)
                for v in range(i):
                    listy2 = self.tableWidget_32.item(v,1)

                    if listy is not None and listy2 is not None:
                        if str(listy.text()) in str(listy2.text()):
                            fv = self.tableWidget_66.item(x,10)
                            nick = self.tableWidget_66.item(x,9)
                            self.tableWidget_32.setItem(v,8,QTableWidgetItem(str(fv.text())))
                            self.tableWidget_32.setItem(v,9,QTableWidgetItem(str(nick.text())))
                        else:
                            pass
        
        except:
            self.tableWidget_32.removeRow()

    def Ui_otworzDPDCod(self):
        try:
            Tk().withdraw() 
            filename = askopenfilename()
            print(filename)
            df = pd.read_excel(str(filename))
            self.tableWidget_34.setRowCount(len(df.index))
            for m in range(len(df.index)):
                    for j in range (len(df.columns)):
                        try:
                             if str(df.iat[m,j]) == 'nan':
                                 self.tableWidget_34.setItem(m,j,QTableWidgetItem(str('')))
                             else:
                                 self.tableWidget_34.setItem(m,j,QTableWidgetItem(str(df.iat[m,j])))
                        except:
                            pass

       
            i = self.tableWidget_34.rowCount()
            z = self.tableWidget_66.rowCount()
            for x in range(z):
                listy = self.tableWidget_66.item(x,11)
                for v in range(i):
                    listy2 = self.tableWidget_34.item(v,2)

                    if listy is not None and listy2 is not None:
                        if str(listy.text()) in str(listy2.text()):
                            fv = self.tableWidget_66.item(x,9)
                            nick = self.tableWidget_66.item(x,10)
                            self.tableWidget_34.setItem(v,8,QTableWidgetItem(str(fv.text())))
                            self.tableWidget_34.setItem(v,9,QTableWidgetItem(str(nick.text())))
                        else:
                            pass
        
        except:
            self.tableWidget_34.removeRow()


    def Ui_otworzDPDCodSEND(self):
        try:
            for i in range(self.tableWidget_34.rowCount()):
                data = self.tableWidget_34.item(i,3)
                wplata = self.tableWidget_34.item(i,4)
                fv = self.tableWidget_34.item(i,8)
                ps = self.tableWidget_34.item(i,4)
                nick = self.tableWidget_34.item(i,9)
                row_numer = self.tableWidget_35.rowCount()
                self.tableWidget_35.insertRow(row_numer)
                if data is not None:
                    self.tableWidget_35.setItem(row_numer,0,QTableWidgetItem(str(data.text())))
                if wplata is not None:
                    self.tableWidget_35.setItem(row_numer,1,QTableWidgetItem(str(wplata.text())))
                if fv is not None:
                    self.tableWidget_35.setItem(row_numer,2,QTableWidgetItem(str(fv.text())))
                if ps is not None:
                    self.tableWidget_35.setItem(row_numer,3,QTableWidgetItem(str(ps.text())))
                if nick is not None:
                    self.tableWidget_35.setItem(row_numer,4,QTableWidgetItem(str(nick.text())))
        except:
            self.tableWidget_34.removeRow()

    def Ui_otworzCod(self):
        try:
            self.tableWidget_25.setRowCount(0)
            token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJhcGktc2hpcHgtcGwuZWFzeXBhY2syNC5uZXQiLCJzdWIiOiJhcGktc2hpcHgtcGwuZWFzeXBhY2syNC5uZXQiLCJleHAiOjE1ODA5ODMyMzksImlhdCI6MTU4MDk4MzIzOSwianRpIjoiNDg5NWRjZDAtNzVmZC00NTY1LThiZDUtNjNmOWIwZDY5MGE4In0.xYzsOGhWZyD_hQI1OAFAdn89CR63LRFqNwhCLHeuQf6CAUffhqb1BqO_vHBKutB_fb-wHWe_j1skq-j_JHysRA'
            token_url = 'http://api-shipx-pl.easypack24.net'


            headers = {}
            headers['Host'] = 'api-shipx-pl.easypack24.net'
            headers['Content-Type'] = 'application/json'
            headers['Authorization'] = "Bearer {}".format(token)

            response = requests.post(token_url,headers)
            l1 = self.lineEdit.text()
            l2 = self.lineEdit_2.text()
            with requests.Session() as session:
                session.headers.update(headers)
                response = session.get('https://api-shipx-pl.easypack24.net/v1/organizations/14292/reports/cod?format=csv&start_date={}&end_date={}'.format(l1,l2))
                decoded_content = response.content.decode('utf-8')
                try:
                    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
                    my_list = list(cr)
                    with open('raportyCODINPOST.csv' ,'w' , newline='') as f:
                        csv_writer = csv.writer(f)
                        csv_writer.writerows(my_list)

                        for row_num, data in enumerate(my_list):
                            worksheet.write_row(row_num, 0, data)
                except:
                    pass
                        

            df = pd.read_csv('raportyCODINPOST.csv',encoding= 'unicode_escape')
        
            compareVal = df.data[0]
            total=round(0,2)

            for x, datez in enumerate(df.data):
                if compareVal==datez:
                    total += df.kwota[x]

                else:
                    df.at[x-1,'total'] = total
                    total = df.kwota[x]
                    compareVal = df.data[x]

                if x == len(df)-1:
                    df.at[x,'total'] = total

            self.tableWidget_25.setRowCount(len(df.index))
            for i in range(len(df.index)):
                for j in range(len(df.columns)):
                    self.tableWidget_25.setItem(i,0,QTableWidgetItem(str(df.iat[i,0])))
                    self.tableWidget_25.setItem(i,1,QTableWidgetItem(str('-')))
                    self.tableWidget_25.setItem(i,2,QTableWidgetItem(str('-')))
                    self.tableWidget_25.setItem(i,3,QTableWidgetItem(str('-')))
                    self.tableWidget_25.setItem(i,4,QTableWidgetItem(str('-')))
                    self.tableWidget_25.setItem(i,5,QTableWidgetItem(str('-')))
                    self.tableWidget_25.setItem(i,6,QTableWidgetItem(str(df.iat[i,6])))
                    self.tableWidget_25.setItem(i,7,QTableWidgetItem(str('-')))
                    self.tableWidget_25.setItem(i,8,QTableWidgetItem(str('-')))
                    self.tableWidget_25.setItem(i,9,QTableWidgetItem(str(df.iat[i,9])))
                    self.tableWidget_25.setItem(i,10,QTableWidgetItem(str(df.iat[i,10])))
                    self.tableWidget_25.setItem(i,11,QTableWidgetItem(str('-')))
                    self.tableWidget_25.setItem(i,12,QTableWidgetItem(str('-')))
                    self.tableWidget_25.setItem(i,13,QTableWidgetItem(str(df.iat[i,13])))

            n = self.tableWidget_25.rowCount()
            for i in range(n):
                try:
                    z = self.tableWidget_25.item(i,13).text()
                    f = float(z)
                    x= round(f,2)
                    s = str(x)
                    self.tableWidget_25.setItem(i,13,QTableWidgetItem(s))
                    if z!='nan':
                        self.tableWidget_25.item(i,13).setBackground(QColor('yellow'))
                    else:
                        self.tableWidget_25.setItem(i,13,QTableWidgetItem('-'))
                        self.tableWidget_25.item(i,13).setBackground(QColor('grey'))
                        
                    nick = self.tableWidget_25.item(i,10).text()
                    #res = re.findall(r'\w+', str(nick))
                    if "cy:" in str(nick):
                        b= nick.split("cy:",1)[1]
                        self.tableWidget_25.setItem(i,14,QTableWidgetItem(str(b)))
                    else:
                        pass
                        
                    if "CY:" in str(nick):
                        b= nick.split("CY:",1)[1]
                        self.tableWidget_25.setItem(i,14,QTableWidgetItem(str(b)))
                    else:
                        pass
                    if "(" not in str(nick):
                        b = self.tableWidget_25.item(i,10).text()
                        self.tableWidget_25.setItem(i,14,QTableWidgetItem(str(b)))
                    else:
                        pass

                    tn = self.tableWidget_25.item(i,14).text()
                    path_to_json = 'jsons/'
                    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
                    for index, js in enumerate(json_files):
                    #with open('data.json') as json_file , open('data2.json') as json_file2:         
                        with open(os.path.join(path_to_json,js)) as json_file:
                            datas = json.load(json_file)
                        
                            for p in datas['checkoutForms']:
                                if str(tn.lower()) in str(p['buyer']['login'].lower()):
                                    con = cx_Oracle.connect('integracja_allegro/CzterejPancerni@192.168.1.4/orcl')
                                    cur = con.cursor()
                                    val = p['id']
                                    cur = con.cursor()
                                    sql="select ztr.ALLEGRO_INTEGRACJA_PROC.GetNrFaktury(:a) from dual"
                                    cur.execute(sql,{'a' : val})
                                    for result in cur:
                                            if p['id']:
                                                self.tableWidget_25.setItem(i,15,QTableWidgetItem(result[0]))
                                    cur.close()
                                    con.close()
                                else:
                                    pass
                                

                except:
                    print('error')

        except:
                print('INPOST COD ERROR')


    def Ui_dzisioj(self):
        try:
            datadzisioj = str(date.today().strftime('%Y-%m-%d'))
            self.lineEdit_2.setText(str(datadzisioj))
        except:
            pass
            
    def Ui_szukaj_listu(self):
        try:
            
            z = self.tableWidget_66.rowCount()
            word = self.lineEdit_4.text()
            w = str(word)
            self.lineEdit.setText(w)
            word = self.lineEdit_4.text()
            if word:
                
                for i in range(self.tableWidget_66.rowCount()):
                    match = False
                    for j in range(self.tableWidget_66.columnCount()):
                        item = self.tableWidget_66.item(i,j)
                        if item is not None and re.match(w,item.text()):
                            match = True
                            break
                    self.tableWidget_66.setRowHidden(i, not match)
            else:
                for i in range(self.tableWidget_66.rowCount()):
                    self.tableWidget_66.setRowHidden(i, False)
        except:
            pass

    def Ui_szukaj_listu_tracking(self):
        try:
            
            z = self.tableWidget_2.rowCount()
            word = self.lineEdit_3.text()
            w = str(word)
            self.lineEdit_3.setText(w)
            word = self.lineEdit_3.text()
            if word:
                
                for i in range(self.tableWidget_2.rowCount()):
                    match = False
                    for j in range(self.tableWidget_2.columnCount()):
                        item = self.tableWidget_2.item(i,j)
                        if item is not None and re.match(w,item.text()):
                            match = True
                            break
                    self.tableWidget_2.setRowHidden(i, not match)
            else:
                for i in range(self.tableWidget_2.rowCount()):
                    self.tableWidget_2.setRowHidden(i, False)
        except:
            pass
    def Ui_szukaj_nickuP24(self):
        try:
            
            z = self.tableWidget_8.rowCount()
            word = self.lineEdit_12.text()
            if word:
                
                for i in range(self.tableWidget_8.rowCount()):
                    match = False
                    for j in range(self.tableWidget_8.columnCount()):
                        item = self.tableWidget_8.item(i,j)
                        if item is not None and re.match(word,item.text()):
                            match = True
                            break
                    self.tableWidget_8.setRowHidden(i, not match)
            else:
                for i in range(self.tableWidget_8.rowCount()):
                    self.tableWidget_8.setRowHidden(i, False)
        except:
            pass

    def Ui_szukaj_nickuPAYU(self):
        try:
      
            z = self.tableWidget_7.rowCount()
            word = self.lineEdit_13.text()
            if word:
                
                for i in range(self.tableWidget_7.rowCount()):
                    match = False
                    for j in range(self.tableWidget_7.columnCount()):
                        item = self.tableWidget_7.item(i,j)
                        if item is not None and re.match(word,item.text()):
                            match = True
                            break
                    self.tableWidget_7.setRowHidden(i, not match)
            else:
                for i in range(self.tableWidget_7.rowCount()):
                    self.tableWidget_7.setRowHidden(i, False)
        except:
            pass

    def Ui_szukaj_nickuZP(self):
        try:

            z = self.tableWidget_4.rowCount()
            word = self.lineEdit_15.text()
            if word:
                
                for i in range(self.tableWidget_4.rowCount()):
                    match = False
                    for j in range(self.tableWidget_4.columnCount()):
                        item = self.tableWidget_4.item(i,j)
                        if item is not None and re.match(word,item.text()):
                            match = True
                            break
                    self.tableWidget_4.setRowHidden(i, not match)
            else:
                for i in range(self.tableWidget_4.rowCount()):
                    self.tableWidget_4.setRowHidden(i, False)
        except:
            pass

    def Ui_szukaj_nickuINPOST(self):
        try:
 
            z = self.tableWidget_6.rowCount()
            word = self.lineEdit_16.text()
            if word:
                
                for i in range(self.tableWidget_6.rowCount()):
                    match = False
                    for j in range(self.tableWidget_6.columnCount()):
                        item = self.tableWidget_6.item(i,j)
                        if item is not None and re.match(word,item.text()):
                            match = True
                            break
                    self.tableWidget_6.setRowHidden(i, not match)
            else:
                for i in range(self.tableWidget_6.rowCount()):
                    self.tableWidget_6.setRowHidden(i, False)
        except:
            pass


    def Ui_szukaj_nickuF(self):
        try:
            z = self.tableWidget_32.rowCount()
            word = self.lineEdit_9.text()
            w = str(word)
            self.lineEdit_9.setText(w)
            word = self.lineEdit_9.text()
            if word:
                
                for i in range(self.tableWidget_32.rowCount()):
                    match = False
                    for j in range(self.tableWidget_32.columnCount()):
                        item = self.tableWidget_32.item(i,j)
                        if item is not None and re.match(w,item.text()):
                            match = True
                            break
                    self.tableWidget_32.setRowHidden(i, not match)
            else:
                for i in range(self.tableWidget_32.rowCount()):
                    self.tableWidget_32.setRowHidden(i, False)
        except:
            pass


    def Ui_szukaj_nickuZWROTY(self):
        try:

            z = self.tableWidget_9.rowCount()
            word = self.lineEdit_14.text()
            if word:
                
                for i in range(self.tableWidget_9.rowCount()):
                    match = False
                    for j in range(self.tableWidget_9.columnCount()):
                        item = self.tableWidget_9.item(i,j)
                        if item is not None and re.match(word,item.text()):
                            match = True
                            break
                    self.tableWidget_9.setRowHidden(i, not match)
            else:
                for i in range(self.tableWidget_9.rowCount()):
                    self.tableWidget_9.setRowHidden(i, False)
        except:
            pass

    def Ui_szukaj_nickuCOD(self):
        try:

            z = self.tableWidget_25.rowCount()
            word = self.lineEdit_21.text()
            if word:
                
                for i in range(self.tableWidget_25.rowCount()):
                    match = False
                    for j in range(self.tableWidget_25.columnCount()):
                        item = self.tableWidget_25.item(i,j)
                        if item is not None and re.match(word,item.text()):
                            match = True
                            break
                    self.tableWidget_25.setRowHidden(i, not match)
            else:
                for i in range(self.tableWidget_25.rowCount()):
                    self.tableWidget_25.setRowHidden(i, False)
        except:
            pass

    def Ui_szukaj_DE(self):
        try:

            z = self.tableWidget.rowCount()
            word = self.lineEdit_11.text()
            if word:
                
                for i in range(self.tableWidget.rowCount()):
                    match = False
                    for j in range(self.tableWidget.columnCount()):
                        item = self.tableWidget.item(i,j)
                        if item is not None and re.match(word,item.text()):
                            match = True
                            break
                    self.tableWidget.setRowHidden(i, not match)
            else:
                for i in range(self.tableWidget.rowCount()):
                    self.tableWidget.setRowHidden(i, False)
        except:
            pass


    def Ui_zapiszDE(self):
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
        sheet.write(0,0,"Data fv")
        for currentColumn in range(self.tableWidget.columnCount()):
            for currentRow in range(self.tableWidget.rowCount()):
                try:
                    style = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
                    sheet.write(0,0,"Data fv",style)
                    sheet.write(0,1,"Termin")
                    sheet.write(0,2,"Do wpĹ‚aty kwota")
                    sheet.write(0,3,"Data")
                    sheet.write(0,4,"WpĹ‚ata kwota")
                    sheet.write(0,5,"FV")
                    sheet.write(0,6,"PozostaĹ‚o do spĹ‚aty")
                    sheet.write(0,7,"List przewozowy")
                    sheet.write(0,8,"Nick")
                    sheet.write(0,9,"Uwagi")
                    teext = str(self.tableWidget.item(currentRow, currentColumn).text())
                    sheet.write(currentRow+1, currentColumn, teext)
                except AttributeError:
                    pass
        wbk.save("raporty/Zestawienie_rozliczenDE.xls")
        ctypes.windll.user32.MessageBoxW(0, "Zapisano raport! Znajdziesz go w folderze: raporty.", "Zapisano", 64)


    def Ui_zapiszTracking(self):
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
        sheet.write(0,0,"Data fv")
        for currentColumn in range(self.tableWidget_2.columnCount()):
            for currentRow in range(self.tableWidget_2.rowCount()):
                try:
                    style = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
                    sheet.write(0,0,"Typ kuriera",style)
                    sheet.write(0,1,"List przewozowy")
                    sheet.write(0,2,"Status")
                    sheet.write(0,3,"Id zamówienia")
                    sheet.write(0,4,"Uwagi")
                    teext = str(self.tableWidget_2.item(currentRow, currentColumn).text())
                    sheet.write(currentRow+1, currentColumn, teext)
                except AttributeError:
                    pass
        wbk.save("raporty/Zestawienie_Tracking.xls")
        ctypes.windll.user32.MessageBoxW(0, "Zapisano raport! Znajdziesz go w folderze: raporty.", "Zapisano", 64)
        
    def Ui_ZapiszInpost(self):
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
        sheet.write(0,0,"Login")
        for currentColumn in range(self.tableWidget_6.columnCount()):
            for currentRow in range(self.tableWidget_6.rowCount()):
                try:
                    style = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
                    sheet.write(0,0,"Login",style)
                    sheet.write(0,1,"Imię˘")
                    sheet.write(0,2,"Nazwisko")
                    sheet.write(0,3,"Metoda dostawy Inpost")
                    sheet.write(0,4,"Koszt dostawy")
                    sheet.write(0,5,"Data zakupu")
                    teext = str(self.tableWidget_6.item(currentRow, currentColumn).text())
                    sheet.write(currentRow+1, currentColumn, teext)
                except AttributeError:
                    pass
        wbk.save("raporty/Zestawienie_INPOST_Allegro.xls")
        ctypes.windll.user32.MessageBoxW(0, "Zapisano raport! Znajdziesz go w folderze: raporty.", "Zapisano", 64)


    def Ui_ZapiszFedexCOD(self):
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
        sheet.write(0,0,"Data bank")
        for currentColumn in range(self.tableWidget_32.columnCount()):
            for currentRow in range(self.tableWidget_32.rowCount()):
                try:
                    style = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
                    sheet.write(0,0,"Data bank",style)
                    sheet.write(0,1,"List")
                    sheet.write(0,2,"Data nadania")
                    sheet.write(0,3,"Opis")
                    sheet.write(0,4,"Uwagi")
                    sheet.write(0,5,"Nr. zew")
                    sheet.write(0,6,"Odbiorca")
                    sheet.write(0,7,"Kwota")
                    sheet.write(0,8,"Nr.FV")
                    sheet.write(0,9,"Nick allegro")
                    teext = str(self.tableWidget_32.item(currentRow, currentColumn).text())
                    sheet.write(currentRow+1, currentColumn, teext)
                except AttributeError:
                    pass
        wbk.save("raporty/Zestawienie_Fedex_COD.xls")
        ctypes.windll.user32.MessageBoxW(0, "Zapisano raport! Znajdziesz go w folderze: raporty.", "Zapisano", 64)


    def Ui_ZapiszFedexCODDFK(self):
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
        sheet.write(0,0,"Data bank")
        for currentColumn in range(self.tableWidget_33.columnCount()):
            for currentRow in range(self.tableWidget_33.rowCount()):
                try:
                    style = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
                    sheet.write(0,0,"Data",style)
                    sheet.write(0,1,"WpĹ‚ata")
                    sheet.write(0,2,"Faktura")
                    sheet.write(0,3,"PozostaĹ‚o do spĹ‚aty")
                    sheet.write(0,4,"Nick/Klient")
                    teext = str(self.tableWidget_33.item(currentRow, currentColumn).text())
                    sheet.write(currentRow+1, currentColumn, teext)
                except AttributeError:
                    pass
        wbk.save("raporty/Zestawienie_Fedex_CODDFK.xls")
        ctypes.windll.user32.MessageBoxW(0, "Zapisano raport! Znajdziesz go w folderze: raporty.", "Zapisano", 64)

    def Ui_ZapiszDPDCOD(self):
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
        sheet.write(0,0,"Data bank")
        for currentColumn in range(self.tableWidget_34.columnCount()):
            for currentRow in range(self.tableWidget_34.rowCount()):
                try:
                    style = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
                    sheet.write(0,0,"Data bank",style)
                    sheet.write(0,1,"List")
                    sheet.write(0,2,"Data nadania")
                    sheet.write(0,3,"Opis")
                    sheet.write(0,4,"Uwagi")
                    sheet.write(0,5,"Nr. zew")
                    sheet.write(0,6,"Odbiorca")
                    sheet.write(0,7,"Kwota")
                    sheet.write(0,8,"Nick")
                    sheet.write(0,9,"FV")
                    teext = str(self.tableWidget_34.item(currentRow, currentColumn).text())
                    sheet.write(currentRow+1, currentColumn, teext)
                except AttributeError:
                    pass
        wbk.save("raporty/Zestawienie_DPD.xls")
        ctypes.windll.user32.MessageBoxW(0, "Zapisano raport! Znajdziesz go w folderze: raporty.", "Zapisano", 64)
        
    def Ui_ZapiszCOD(self):
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
        sheet.write(0,0,"Data")
        for currentColumn in range(self.tableWidget_25.columnCount()):
            for currentRow in range(self.tableWidget_25.rowCount()):
                try:
                    style = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
                    sheet.write(0,0,"Data",style)
                    sheet.write(0,1,"Numer Klienta")
                    sheet.write(0,2,"Nadawca")
                    sheet.write(0,3,"Odbiorca")
                    sheet.write(0,4,"Kod pocztowy odbiorcy")
                    sheet.write(0,5,"Miasto odbiorcy")
                    sheet.write(0,6,"Numer listu przewozowego")
                    sheet.write(0,7,"Data nadania")
                    sheet.write(0,8,"Data otrzymania")
                    sheet.write(0,9,"Kwota")
                    sheet.write(0,10,"Uwagi")
                    sheet.write(0,11,"Referencja")
                    sheet.write(0,12,"Mpk")
                    sheet.write(0,13,"Suma")
                    sheet.write(0,14,"Nick Allegro")
                    sheet.write(0,15,"Numer FV")
                    teext = str(self.tableWidget_25.item(currentRow, currentColumn).text())
                    sheet.write(currentRow+1, currentColumn, teext)
                except AttributeError:
                    pass
        wbk.save("raporty/Zestawienie_WEBTRUCK-COD.xls")
        ctypes.windll.user32.MessageBoxW(0, "Zapisano raport! Znajdziesz go w folderze: raporty.", "Zapisano", 64)


    def Ui_danezewzapisz(self):
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
        for currentColumn in range(self.tableWidget_5.columnCount()):
            for currentRow in range(self.tableWidget_5.rowCount()):
                try:
                    teext = str(self.tableWidget_5.item(currentRow, currentColumn).text())
                    sheet.write(currentRow+1, currentColumn, teext)
                except AttributeError:
                    pass
        wbk.save("raporty/danezew.xls")
        ctypes.windll.user32.MessageBoxW(0, "Zapisano raport! Znajdziesz go w folderze: raporty.", "Zapisano", 64)

    def Ui_danezewzapisz2(self):
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
        for currentColumn in range(self.tableWidget_10.columnCount()):
            for currentRow in range(self.tableWidget_10.rowCount()):
                try:
                    teext = str(self.tableWidget_5.item(currentRow, currentColumn).text())
                    sheet.write(currentRow+1, currentColumn, teext)
                except AttributeError:
                    pass
        wbk.save("raporty/danezew_przynaleznosc_pojazdowa.xls")
        ctypes.windll.user32.MessageBoxW(0, "Zapisano raport! Znajdziesz go w folderze: raporty.", "Zapisano", 64)
        
    def Ui_ZapiszZwroty(self):
    
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
        sheet.write(0,0,"Data wpÄąâ€šywu na konto")
        for currentColumn in range(self.tableWidget_9.columnCount()):
            for currentRow in range(self.tableWidget_9.rowCount()):
                try:
                    style = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
                    sheet.write(0,0,"Data wpÄąâ€šywu na konto")
                    sheet.write(0,1,"Kwota zwrotu")
                    sheet.write(0,2,"FV")
                    sheet.write(0,3,"Saldo po operacji")
                    sheet.write(0,4,"Nick allegro")
                    sheet.write(0,5,"Uwagi")
                    teext = str(self.tableWidget_9.item(currentRow, currentColumn).text())
                    sheet.write(currentRow+1, currentColumn, teext)
                except AttributeError:
                    pass 
        wbk.save("raporty/Zestawienie_zwrotow.xls")
        ctypes.windll.user32.MessageBoxW(0, "Zapisano raport! Znajdziesz go w folderze: raporty.", "Zapisano", 64)


    def Ui_ZapiszFedexDFK(self):
    
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
        for currentColumn in range(self.tableWidget_31.columnCount()):
            for currentRow in range(self.tableWidget_31.rowCount()):
                try:
                    style = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
                    sheet.write(0,0,"KWOTA WPÄąÂYWU")
                    sheet.write(0,1,"DATA")
                    sheet.write(0,2,"DANE KLIENTA",style)
                    sheet.write(0,3,"KWOTA WPÄąÂYWU ÄąÂĂ„â€žCZNIE")
                    sheet.write(0,4,"FAKTURA")
                    sheet.write(0,5,"NICK ALLEGRO")
                    sheet.write(0,6,"LIST PRZEWOZOWY")
                    teext = str(self.tableWidget_31.item(currentRow, currentColumn).text())
                    sheet.write(currentRow+1, currentColumn, teext)
                except AttributeError:
                    pass 
        wbk.save("raporty/Zestawienie_FedexDFK_Automatyzacja.xls")
        ctypes.windll.user32.MessageBoxW(0, "Zapisano raport! Znajdziesz go w folderze: raporty.", "Zapisano", 64)
        
    def Ui_ZapiszZaPobraniem(self):
    
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
        for currentColumn in range(self.tableWidget_4.columnCount()):
            for currentRow in range(self.tableWidget_4.rowCount()):
                try:
                    style = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
                    sheet.write(0,0,"ID")
                    sheet.write(0,1,"SPOSÄ‚â€śB PÄąÂATNOÄąĹˇCI")
                    sheet.write(0,2,"STATUS",style)
                    sheet.write(0,3,"METODA DOSTAWY")
                    sheet.write(0,4,"CENA DOSTAWY")
                    sheet.write(0,5,"DATA ZAKUPU")
                    sheet.write(0,6,"P/FV")
                    sheet.write(0,7,"Nick Allegro")
                    sheet.write(0,8,"Numer Faktury/Paragonu - Data")
                    sheet.write(0,9,"Uwagi")
                    teext = str(self.tableWidget_4.item(currentRow, currentColumn).text())
                    sheet.write(currentRow+1, currentColumn, teext)
                except AttributeError:
                    pass 
        wbk.save("raporty/Zestawienie_ZA_POBRANIEM.xls")
        ctypes.windll.user32.MessageBoxW(0, "Zapisano raport! Znajdziesz go w folderze: raporty.", "Zapisano", 64)
        
    def Ui_ZapiszP24(self):
    
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
        for currentColumn in range(self.tableWidget_8.columnCount()):
            for currentRow in range(self.tableWidget_8.rowCount()):
                try:
                    style = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
                    sheet.write(0,0,"Data wpÄąâ€šywu na konto")
                    sheet.write(0,1,"Kwota wpÄąâ€šywu na konto",style)
                    sheet.write(0,2,"Numer Faktury/Paragonu - Data")
                    sheet.write(0,3,"Kwota poszczegÄ‚Ĺ‚lnych Faktur/ParagonÄ‚Ĺ‚w")
                    sheet.write(0,4,"Nick Allegro")
                    sheet.write(0,5,"Listy Przewozowe")
                    teext = str(self.tableWidget_8.item(currentRow, currentColumn).text())
                    sheet.write(currentRow+1, currentColumn, teext)
               
                except AttributeError:
                    pass 
        wbk.save("raporty/zestawienie_P24_Allegro.xls")
        ctypes.windll.user32.MessageBoxW(0, "Zapisano raport! Znajdziesz go w folderze: raporty.", "Zapisano", 64)
        
    def Ui_ZapiszPayu(self):

        wbk = xlwt.Workbook()
        cols = ['Nick Allegro','ImiĂ„â„˘','Nazwisko','Metoda dostawy','Koszt','Data zakupu']
        sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
        for currentColumn in range(self.tableWidget_7.columnCount()):
            for currentRow in range(self.tableWidget_7.rowCount()):
                try:
                    style = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
                    sheet.write(0,0,"Data wpÄąâ€šywu na konto")
                    sheet.write(0,1,"Kwota wpÄąâ€šywu na konto",style)
                    sheet.write(0,2,"Numer Faktury/Paragonu - Data")
                    sheet.write(0,3,"Kwota poszczegÄ‚Ĺ‚lnych Faktur/ParagonÄ‚Ĺ‚w")
                    sheet.write(0,4,"Nick Allegro")
                    sheet.write(0,5,"List przewozowy")
                    teext = str(self.tableWidget_7.item(currentRow, currentColumn).text())
                    sheet.write(currentRow+1, currentColumn, teext)
                except AttributeError:
                    pass 
        wbk.save("raporty/zestawienie_PAYU_Allegro.xls")
        ctypes.windll.user32.MessageBoxW(0, "Zapisano raport! Znajdziesz go w folderze: raporty.", "Zapisano", 64)
                


        
class NewWindowTest(QMainWindow):
    def __init__(self,object,tableWidget,tableWidget2,tableWidget3):
        super(NewWindowTest, self).__init__()
        pushButton = QPushButton(self)
        pushButton.setIcon(QIcon('zdjecia/pushbutton_icos.png'))
        pushButton.clicked.connect(lambda:self.Ui_zamowienia(object,tableWidget,tableWidget2,tableWidget3))
        pushButton.move(0,0)
        pushButton.setFixedHeight(50)
        self.setCentralWidget(pushButton)

    def openlink(self,item):
        if item.column() == 1:
            t = self.tableWidget_38.item(0,1)
            tt = str(t)
            webbrowser.open(tt)


        
    def Ui_zamowienia(self,object,tableWidget_13,tableWidget_14,tableWidget_15):
            self.object = object
            self.tableWidget_13 = tableWidget_13
            self.tableWidget_14 = tableWidget_14
            self.tableWidget_15 = tableWidget_15
            for i in reversed(range(self.tableWidget_13.rowCount())):
                self.tableWidget_13.removeRow(i)
            for i in reversed(range(self.tableWidget_14.rowCount())):
                self.tableWidget_14.removeRow(i)
            for i in reversed(range(self.tableWidget_15.rowCount())):
                self.tableWidget_15.removeRow(i)
            path_to_json = 'jsons/'
            json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
            for index, js in enumerate(json_files):       
                            with open(os.path.join(path_to_json,js)) as json_file:
                                datas = json.load(json_file)
                                for p in datas['checkoutForms']:
                                        row_numer12 = self.tableWidget_13.rowCount()
                                        self.tableWidget_13.insertRow(row_numer12)
                                        row_numer13 = self.tableWidget_14.rowCount()
                                        self.tableWidget_14.insertRow(row_numer13)
                                        row_numer14 = self.tableWidget_15.rowCount()
                                        self.tableWidget_15.insertRow(row_numer14)

                                        if(p['id']==self.object):
                                           if(p['status']=="READY_FOR_PROCESSING"):
                                               self.tableWidget_13.setItem(row_numer12,0,QTableWidgetItem(p['delivery']['address']['firstName']))
                                               self.tableWidget_13.setItem(row_numer12,1,QTableWidgetItem(p['delivery']['address']['lastName']))
                                               self.tableWidget_13.setItem(row_numer12,2,QTableWidgetItem(p['delivery']['address']['city']))
                                               self.tableWidget_13.setItem(row_numer12,3,QTableWidgetItem(p['delivery']['address']['street']))
                                               self.tableWidget_13.setItem(row_numer12,4,QTableWidgetItem(p['delivery']['address']['zipCode']))
                                               self.tableWidget_13.setItem(row_numer12,5,QTableWidgetItem(p['delivery']['address']['phoneNumber']))
                                               self.tableWidget_13.setItem(row_numer12,6,QTableWidgetItem(p['buyer']['email']))
                                               self.tableWidget_13.resizeColumnsToContents()
                                               self.tableWidget_13.resizeRowsToContents()
                                           elif(p['status']=="FILLED_IN"):
                                               self.tableWidget_13.setItem(row_numer12,0,QTableWidgetItem('-'))
                                               self.tableWidget_13.setItem(row_numer12,1,QTableWidgetItem('-'))
                                               self.tableWidget_13.setItem(row_numer12,2,QTableWidgetItem('-'))
                                               self.tableWidget_13.setItem(row_numer12,3,QTableWidgetItem('-'))
                                               self.tableWidget_13.setItem(row_numer12,4,QTableWidgetItem('-'))
                                               self.tableWidget_13.setItem(row_numer12,5,QTableWidgetItem('-'))
                                               self.tableWidget_13.resizeColumnsToContents()
                                               self.tableWidget_13.resizeRowsToContents()
                                                    
                                        else:
                                               self.tableWidget_13.removeRow(row_numer12)
                                               
                                        if(p['id']==self.object):
                                            for i in range(len(p['lineItems'])):
                                                self.tableWidget_14.insertRow(row_numer13)                                           
                                                try:
                                                
                                                    self.tableWidget_14.setItem(row_numer13,1,QTableWidgetItem(p['lineItems'][i]['id']))
                                                            
                                                    self.tableWidget_14.setItem(row_numer13,2,QTableWidgetItem(p['lineItems'][i]['offer']['name']))
                                                    try:
                                                        self.tableWidget_14.setItem(row_numer13,3,QTableWidgetItem(p['lineItems'][i]['offer']['external']['id']))
                                                    except Exception:
                                                        self.tableWidget_14setItem(row_numer13,3,QTableWidgetItem('Brak'))
                                                    try:
                                                        self.tableWidget_14.setItem(row_numer13,4,QTableWidgetItem(str(int(p['lineItems'][i]['quantity']))))
                                                    except Exception:
                                                        self.tableWidget_14.setItem(row_numer13,4,QTableWidgetItem('-'))
                                                    self.tableWidget_14.setItem(row_numer13,5,QTableWidgetItem(p['lineItems'][i]['originalPrice']['amount']))
                                                    
                                                    id_oferty = p['lineItems'][i]['offer']['id']
                                                    oferta = str(id_oferty)
                                                    headers = {}
                                                    headers['charset'] = 'UTF-8'
                                                    headers['Accept-Language'] = 'pl-PL'
                                                    headers['Content-Type'] = 'application/vnd.allegro.public.v1+json'
                                                    headers['Api-Key'] = API_KEY
                                                    headers['Accept'] = 'application/vnd.allegro.public.v1+json'
                                                    headers['Authorization'] = "Bearer {}".format(sign2['access_token'])
                                                    with requests.Session() as session:
                                                        session.headers.update(headers)
                                                        response = session.get('https://api.allegro.pl/sale/offers?offer.id={}'.format(oferta))
                                                        wyswietl = response.json()
                                                        for i in wyswietl['offers']:
                                                            zdj = i['primaryImage']['url']
                                                            zdi2 = str(zdj+'.jpg')
                                                            r = requests.get(zdi2,stream=True)
                                                            assert r.status_code == 200
                                                            try:
                                                                img = QImage()
                                                                assert img.loadFromData(r.content)
                                                                w = QLabel()
                                                                w.setPixmap(QPixmap.fromImage(img.scaled(100,100)))
                                                                self.tableWidget_14.setCellWidget(row_numer13,0,w)
                                                            except:
                                                                pass

                                       
                                                    self.tableWidget_14.resizeColumnsToContents()
                                                    self.tableWidget_14.resizeRowsToContents()
                                                except Exception:
                                                    pass
                                            self.tableWidget_14.setItem(row_numer13,6,QTableWidgetItem(p['delivery']['cost']['amount']))    
                                        else:
                                            self.tableWidget_14.removeRow(row_numer13)
                                        
                                        if p['summary']['totalToPay']['amount']:
                                            self.tableWidget_14.setItem(row_numer13,7,QTableWidgetItem(p['summary']['totalToPay']['amount']))
                                            self.tableWidget_14.resizeColumnsToContents()
                                            self.tableWidget_14.resizeRowsToContents()
                                        else:
                                            self.tableWidget_14.removeRow(row_numer13)


                                        if(p['id']==self.object):
                                            try:
                                                if(p['invoice']['required'] == True):
                                                    self.tableWidget_15.setItem(row_numer14,0,QTableWidgetItem(p['invoice']['address']['city']))
                                                    self.tableWidget_15.setItem(row_numer14,1,QTableWidgetItem(p['invoice']['address']['street']))
                                                    self.tableWidget_15.setItem(row_numer14,2,QTableWidgetItem(p['invoice']['address']['zipCode']))
                                                    self.tableWidget_15.setItem(row_numer14,3,QTableWidgetItem(p['invoice']['address']['company']['name']))
                                                    self.tableWidget_15.setItem(row_numer14,4,QTableWidgetItem(p['invoice']['address']['company']['taxId']))
                                                    self.tableWidget_15.resizeColumnsToContents()
                                                    self.tableWidget_15.resizeRowsToContents()
                                                    
                                                else:
                                                    self.tableWidget_15.setItem(row_numer14,0,QTableWidgetItem('-'))
                                                    self.tableWidget_15.setItem(row_numer14,1,QTableWidgetItem('-'))
                                                    self.tableWidget_15.setItem(row_numer14,2,QTableWidgetItem('-'))
                                                    self.tableWidget_15.setItem(row_numer14,3,QTableWidgetItem('-'))
                                                    self.tableWidget_15.setItem(row_numer14,4,QTableWidgetItem('-'))
                                            except Exception:
                                                self.tableWidget_15.setItem(row_numer14,0,QTableWidgetItem('-'))
                                                self.tableWidget_15.setItem(row_numer14,1,QTableWidgetItem('-'))
                                                self.tableWidget_15.setItem(row_numer14,2,QTableWidgetItem('-'))
                                                self.tableWidget_15.setItem(row_numer14,3,QTableWidgetItem('-'))
                                                self.tableWidget_15.setItem(row_numer14,4,QTableWidgetItem('-'))
                                        else:
                                            self.tableWidget_15.removeRow(row_numer14)
                                    
      



def main():
    import sys
    import files_rc
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
main()
