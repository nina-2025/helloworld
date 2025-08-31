import pandas

class readcsv:
    def __init__(self,filename):
    """
    Initialize the readcsv instance with a filename and read the CSV file.

    Args:
        filename (str): The path to the CSV file to be read.

    Attributes:
        filename (str): Stores the path to the CSV file.
        df (pandas.DataFrame): DataFrame containing the data from the CSV file.
    """

        self.filename=filename
        self.df=pandas.read_csv(filename)
    def get_csv(self):
        return self.df