from Project.Model.InputHandler.ParseWav import parseWavFiles
import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc


def uponActionPerformed(mainWindow, qtw):
    openRecentAction(mainWindow, qtw)

# TODO: should be another drop down menu where the user
#  can select recently worked on files (maybe also the untitled autosave)
def openRecentAction(mainWindow, qtw):
    print("something")