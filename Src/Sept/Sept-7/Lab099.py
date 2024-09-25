# Static - example

class ExcelReader:

    @staticmethod
    def readExcelFile():
        print("Reading from Excel")


class MyDBConnection():
    def runTC(self):
        ExcelReader().readExcelFile()


a = MyDBConnection()
a.runTC()
