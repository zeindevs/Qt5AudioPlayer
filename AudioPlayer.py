import sys
import pyaudio 
import os

from PyQt5.QtCore import pyqtSignal, Qt, QTime
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QSizePolicy, QWidget, QVBoxLayout
from PyQt5.QtMultimedia import QAudioDeviceInfo, QMediaPlayer, QMediaService, QAudioOutputSelectorControl, QMediaContent

from ui.audio_player import Ui_MainWindow
from ui.audio_channel import Ui_AudioChannel

os.environ['QT_MULTIMEDIA_PREFERRED_PLUGINS'] = 'windowsmediafundation'

class AudioPlayer(QWidget, Ui_AudioChannel):
    deleted = pyqtSignal(int)

    def __init__(self, parent=None, id=0, channel='Channel 1'):
        super().__init__()

        self.id = id

        self.setupUi(self)

        self.soundCard = []

        self.audioMedia = None

        p = pyaudio.PyAudio()

        self.player = QMediaPlayer()
        self.player.positionChanged.connect(self.positionChanged)
        self.player.durationChanged.connect(self.durationChanged)

        self.audioDuration.valueChanged.connect(self.handlePosition)

        host_info = p.get_host_api_info_by_index(1)
        device_count = host_info.get("deviceCount")

        # for device in QAudioDeviceInfo.availableDevices(QAudio.Mode.AudioOutput):
            # print(device.deviceName())
            # self.audioOutput.addItem(device.deviceName())

        if device_count:
            for x in range(int(device_count)):
                info = p.get_device_info_by_host_api_device_index(1, x)
                self.soundCard.append(info)
        
            for x in self.soundCard:
                self.audioOutput.addItem(x['name'])
        
        self.labelGroupChannel.setTitle(channel)

        self.audioOpen.clicked.connect(self.handleOpen)

        self.audioOutput.currentTextChanged.connect(self.handleOutput)

        self.sliderVolume.setRange(0,100)
        self.sliderVolume.valueChanged.connect(self.handleVolume)

        self.btnPlay.setDisabled(True)

        self.btnPlay.clicked.connect(self.handlePlay)

        self.btnDelete.clicked.connect(self.handleDelete)
        self.btnPause.clicked.connect(self.handlePause)
        self.btnStop.clicked.connect(self.handleStop)

    def handleOpen(self):
        filename, _ = QFileDialog.getOpenFileUrl(self)
        if filename:
            self.player.setMedia(QMediaContent(filename))
            self.audioFile.setText(filename.toString())
            self.btnPlay.setDisabled(False)
    
    def handleOutput(self):
        pass
        # out = self.player.service().requestControl("org.qt-project.qt.audiooutputselectorcontrol/5.0")
        # self.player.service().releaseControl(out)

    def handleVolume(self, value: int):
        self.labelVolume.setText(f'{value}%')
        self.player.setVolume(value)

    def handlePlay(self):
        self.player.play()
        self.btnPlay.setDisabled(True)
        self.btnPause.setDisabled(False)
        self.btnStop.setDisabled(False)
    
    def handlePause(self):
        self.player.pause()
        self.btnPlay.setDisabled(False)
        self.btnPause.setDisabled(True)

    def handleStop(self):
        self.player.stop()
        self.btnPlay.setDisabled(False)
        self.btnStop.setDisabled(True)
        self.btnPause.setDisabled(True)

    def handleDelete(self):
        self.player.stop()
        self.deleted.emit(self.id)
        self.close()
        self.destroy()

    def positionChanged(self, position):
        mtime = QTime(0, 0, 0, 0)
        mtime = mtime.addMSecs(self.player.position())
        self.timeStart.setText(mtime.toString())
        self.audioDuration.setValue(position)

    def durationChanged(self, duration):
        mtime = QTime(0, 0, 0, 0)
        mtime = mtime.addMSecs(self.player.duration())
        self.timeEnd.setText(mtime.toString())
        self.audioDuration.setRange(0, duration)

    def handlePosition(self, position):
        mtime = QTime(0, 0, 0, 0)
        mtime = mtime.addMSecs(position)
        self.timeStart.setText(mtime.toString())
        self.player.setPosition(position)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        self.audioList = []

        self.lastId = 0
        
        widget = QWidget()

        self.audioLayout = QVBoxLayout()

        widget.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)

        widget.setLayout(self.audioLayout)

        self.scrollArea.setWidget(widget)

        self.btnAddChannel.clicked.connect(self.handleAddChannel)
        self.btnDeleteAllChannel.clicked.connect(self.handleDeleteAllChannel)

    def handleAddChannel(self):
        index = len(self.audioList) + 1
        audio = AudioPlayer(id=index, channel=f'Channel {index}')
        audio.deleted.connect(self.handleDeleteChannel)
        self.lastId = index
        self.audioList.append({ 'id': index, 'audio': audio })
        self.audioLayout.addWidget(audio)
        self.labelTotalChannel.setText(str(len(self.audioList)))
        self.btnDeleteAllChannel.setDisabled(False)

    def handleDeleteChannel(self, widget=None):
        pass
        # del self.audioList[index-1]
        # self.audioLayout.removeWidget(self.audioList[index-1])
        # self.audioLayout.removeWidget(widget)
        
    def handleDeleteAllChannel(self):
        for widget in self.audioList:
            self.audioLayout.removeWidget(widget['audio'])
        self.audioList = []
        self.labelTotalChannel.setText('0')
        self.btnDeleteAllChannel.setDisabled(True)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    app.setStyle('Fusion')
    win.setWindowTitle('Audio Player (Sound Card) Multi Channel')
    win.show()
    sys.exit(app.exec())
