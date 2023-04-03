# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\audio_channel.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AudioChannel(object):
    def setupUi(self, AudioChannel):
        AudioChannel.setObjectName("AudioChannel")
        AudioChannel.resize(810, 100)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AudioChannel.sizePolicy().hasHeightForWidth())
        AudioChannel.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(AudioChannel)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelGroupChannel = QtWidgets.QGroupBox(AudioChannel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelGroupChannel.sizePolicy().hasHeightForWidth())
        self.labelGroupChannel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelGroupChannel.setFont(font)
        self.labelGroupChannel.setObjectName("labelGroupChannel")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.labelGroupChannel)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.widget_5 = QtWidgets.QWidget(self.labelGroupChannel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.widget_5.setFont(font)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 6)
        self.gridLayout_3.setSpacing(9)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.audioFile = QtWidgets.QLineEdit(self.widget_5)
        self.audioFile.setMinimumSize(QtCore.QSize(160, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.audioFile.setFont(font)
        self.audioFile.setReadOnly(True)
        self.audioFile.setObjectName("audioFile")
        self.gridLayout_3.addWidget(self.audioFile, 0, 1, 1, 4)
        self.audioOpen = QtWidgets.QPushButton(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.audioOpen.setFont(font)
        self.audioOpen.setObjectName("audioOpen")
        self.gridLayout_3.addWidget(self.audioOpen, 0, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 1, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 0, 6, 1, 1)
        self.timeEnd = QtWidgets.QLineEdit(self.widget_5)
        self.timeEnd.setMinimumSize(QtCore.QSize(80, 0))
        self.timeEnd.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.timeEnd.setFont(font)
        self.timeEnd.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEnd.setObjectName("timeEnd")
        self.gridLayout_3.addWidget(self.timeEnd, 1, 4, 1, 1)
        self.timeStart = QtWidgets.QLineEdit(self.widget_5)
        self.timeStart.setMinimumSize(QtCore.QSize(80, 0))
        self.timeStart.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.timeStart.setFont(font)
        self.timeStart.setAlignment(QtCore.Qt.AlignCenter)
        self.timeStart.setObjectName("timeStart")
        self.gridLayout_3.addWidget(self.timeStart, 1, 1, 1, 1)
        self.audioDuration = QtWidgets.QSlider(self.widget_5)
        self.audioDuration.setMouseTracking(False)
        self.audioDuration.setTabletTracking(False)
        self.audioDuration.setTracking(True)
        self.audioDuration.setOrientation(QtCore.Qt.Horizontal)
        self.audioDuration.setInvertedAppearance(False)
        self.audioDuration.setInvertedControls(False)
        self.audioDuration.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.audioDuration.setObjectName("audioDuration")
        self.gridLayout_3.addWidget(self.audioDuration, 1, 2, 1, 1)
        self.audioLoop = QtWidgets.QCheckBox(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.audioLoop.sizePolicy().hasHeightForWidth())
        self.audioLoop.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.audioLoop.setFont(font)
        self.audioLoop.setObjectName("audioLoop")
        self.gridLayout_3.addWidget(self.audioLoop, 1, 5, 1, 1)
        self.btnDelete = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDelete.sizePolicy().hasHeightForWidth())
        self.btnDelete.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.btnDelete.setFont(font)
        self.btnDelete.setObjectName("btnDelete")
        self.gridLayout_3.addWidget(self.btnDelete, 0, 8, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 1, 3, 1, 1)
        self.audioOutput = QtWidgets.QComboBox(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.audioOutput.sizePolicy().hasHeightForWidth())
        self.audioOutput.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.audioOutput.setFont(font)
        self.audioOutput.setObjectName("audioOutput")
        self.gridLayout_3.addWidget(self.audioOutput, 0, 7, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 1, 6, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnPlay = QtWidgets.QPushButton(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.btnPlay.setFont(font)
        self.btnPlay.setObjectName("btnPlay")
        self.horizontalLayout_4.addWidget(self.btnPlay)
        self.btnPause = QtWidgets.QPushButton(self.widget_5)
        self.btnPause.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.btnPause.setFont(font)
        self.btnPause.setObjectName("btnPause")
        self.horizontalLayout_4.addWidget(self.btnPause)
        self.btnStop = QtWidgets.QPushButton(self.widget_5)
        self.btnStop.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.btnStop.setFont(font)
        self.btnStop.setObjectName("btnStop")
        self.horizontalLayout_4.addWidget(self.btnStop)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_15 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout.addWidget(self.label_15)
        self.sliderVolume = QtWidgets.QSlider(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sliderVolume.sizePolicy().hasHeightForWidth())
        self.sliderVolume.setSizePolicy(sizePolicy)
        self.sliderVolume.setMinimumSize(QtCore.QSize(0, 0))
        self.sliderVolume.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.sliderVolume.setMaximum(100)
        self.sliderVolume.setProperty("value", 100)
        self.sliderVolume.setOrientation(QtCore.Qt.Horizontal)
        self.sliderVolume.setObjectName("sliderVolume")
        self.horizontalLayout.addWidget(self.sliderVolume)
        self.labelVolume = QtWidgets.QLabel(self.widget_5)
        self.labelVolume.setMinimumSize(QtCore.QSize(30, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.labelVolume.setFont(font)
        self.labelVolume.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelVolume.setObjectName("labelVolume")
        self.horizontalLayout.addWidget(self.labelVolume)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 1, 7, 1, 2)
        self.horizontalLayout_11.addWidget(self.widget_5)
        self.gridLayout.addWidget(self.labelGroupChannel, 0, 0, 1, 1)

        self.retranslateUi(AudioChannel)
        QtCore.QMetaObject.connectSlotsByName(AudioChannel)

    def retranslateUi(self, AudioChannel):
        _translate = QtCore.QCoreApplication.translate
        AudioChannel.setWindowTitle(_translate("AudioChannel", "Audio Channel"))
        self.labelGroupChannel.setTitle(_translate("AudioChannel", "Channel 1"))
        self.audioFile.setPlaceholderText(_translate("AudioChannel", "Audio File"))
        self.audioOpen.setText(_translate("AudioChannel", "Open"))
        self.label.setText(_translate("AudioChannel", "Audio"))
        self.label_24.setText(_translate("AudioChannel", "Start"))
        self.label_17.setText(_translate("AudioChannel", "Output"))
        self.timeEnd.setInputMask(_translate("AudioChannel", "HH:HH:HH"))
        self.timeEnd.setText(_translate("AudioChannel", "00:00:00"))
        self.timeEnd.setPlaceholderText(_translate("AudioChannel", "00:00:00"))
        self.timeStart.setInputMask(_translate("AudioChannel", "HH:HH:HH"))
        self.timeStart.setText(_translate("AudioChannel", "00:00:00"))
        self.timeStart.setPlaceholderText(_translate("AudioChannel", "00:00:00"))
        self.audioLoop.setText(_translate("AudioChannel", "Loop"))
        self.btnDelete.setText(_translate("AudioChannel", "Delete"))
        self.label_23.setText(_translate("AudioChannel", "End"))
        self.label_16.setText(_translate("AudioChannel", "Audio Control"))
        self.btnPlay.setText(_translate("AudioChannel", "Play"))
        self.btnPause.setText(_translate("AudioChannel", "Pause"))
        self.btnStop.setText(_translate("AudioChannel", "Stop"))
        self.label_15.setText(_translate("AudioChannel", "Volume"))
        self.labelVolume.setText(_translate("AudioChannel", "100%"))
