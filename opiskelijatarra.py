# APPLICATION FOR PRINTING STUDENT STICKERS

# Libraries and modules
# ---------------------

from PyQt5 import QtWidgets, uic # UI elements and ui builder
import sys # For accessing system parameters

# Class definitions
# -----------------

class Ui(QtWidgets.QMainWindow):

    # CONSTRUCTOR
    def __init__(self):
        super().__init__()

        # Load the UI definition file
        uic.loadUi('opiskelijatarra.ui', self)

        # CONTROLS
        # 2 eri tapaa
        self.firstNameInput = self.studentFirstNameLineEdit # Direct assign
        self.lastNameInput = self.findChild(QtWidgets.QLineEdit, 'studentLastNameLineEdit') # Pointer assign
        self.numberInput = self.studentNumbeLineEdit

        # INDICATORS
        self.firstNameOutput = self.sticketFirstNameLabel
        self.studentNumberOutput = self.stickerstudentNumbeLabel

        # SIGNALS

        # Print the sticker
        self.printPushButton.clicked.connect(self.printSticker)

        # TODO: Create signals for updating the student name

        # SHOW THE UI
        self.show()

    # SLOTS (Methods)

    # Print the sticker
    def printSticker(self):
        pass

    # TODO: Create function that concatenates first and last name on the sticker

if __name__ == '__main__':

    # Create the app
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = Ui()

    # Run the app
    app.exec_()