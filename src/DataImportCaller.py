from importdata import importdata
from logger import ProjectLogger
class main:
    def __init__(self, filename):
        """Initialize the main class that calls the importdata class using filename as a
        parameter"""
        self.log= ProjectLogger()
        self.filename = filename
        self.data_importer = importdata(filename)
        self.data_importer.load_data()
        self.log.info("Filename is passed successfully")

if __name__ == "__main__":
    app = main('../data/transactions.csv')
    app.log.info("Main class is called successfully")
