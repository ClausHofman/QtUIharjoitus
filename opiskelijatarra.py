# APPLICATION FOR PRINTING STUDENT STICKERS

# Libraries and modules
# ---------------------

from PyQt5 import QtWidgets, uic, QtPrintSupport # UI elements and ui builder
from PyQt5.QtGui import QPainter, QTransform, QPixmap
import sys # For accessing system parameters
import code128Bcode

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
        self.nameOutput = self.sticketFirstNameLabel
        self.nameOutput.setText('') # Clear it before use
        self.studentNumberOutput = self.stickerstudentNumbeLabel
        self.studentNumberOutput.setText('')

        # SIGNALS

        # Print the sticker
        self.printPushButton.clicked.connect(self.printSticker)

        # Signals for updating the student name
        self.firstNameInput.textChanged.connect(self.createFullName)
        self.lastNameInput.textChanged.connect(self.createFullName)

        # Signal when student number has been changed
        self.numberInput.textChanged.connect(self.updateBarcode)

        # SHOW THE UI
        self.show()

    # SLOTS (Methods)

    # Print the sticker
    def printSticker(self):

        # Create a printer object
        #  printer = QtPrintSupport.QPrinter() # Screen Hard Copy

        printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)

        # Create print dialog window object
        printDialog = QtPrintSupport.QPrintDialog(printer, self) 



        # Check if  user has not cancelled the dialog, Accepted with capital A
        if printDialog.exec_() == QtPrintSupport.QPrintDialog.Accepted:

            # Create a painter object to create printable area
            painter = QPainter()

            # Start printing process
            painter.begin(printer)

            # Define the area to be printed
            sticker = self.stickerFrame.grab()

            # Transform to high quality (300 dpi)
            transformation = QTransform() # Create transformation object
            transformation.scale(5, 5) # Set the scale 5 x
            sticker = sticker.transformed(transformation) # Apply the transformation to the sticker

            # Print the area
            painter.drawPixmap(30, 30, sticker)

            # Close printer
            painter.end()


    # Concatenates first and last name and updates the sticker
    def createFullName(self):
        self.fullName = self.firstNameInput.text() + ' ' + self.lastNameInput.text()
        self.nameOutput.setText(self.fullName)
    
    # Creates a barcode from the student number
    def updateBarcode(self):
        bcode = code128Bcode.string2barcode(self.numberInput.text())
        self.studentNumberOutput.setText(bcode)


if __name__ == '__main__':

    # Create the app
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = Ui()

    # Run the app
    app.exec_()