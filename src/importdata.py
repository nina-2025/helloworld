#importdata.py
import pandas as pd
import traceback
import os
from logger import ProjectLogger
from db_config import sql_engine
class importdata:
    """Class for importing data from a CSV file."""
    def __init__(self, filename):
        self.filename = filename
        self.log=ProjectLogger()
        self.log.info(f"importdata initialized with file: {self.filename}")
    
    def load_data(self):  # ✅ renamed and added self
        try:
            print(self.filename)
            self.log.info("Data import started successfully.")
            base_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(base_dir, self.filename)  # use self.filename
            self.log.info("file path : {file_path}")
            df = pd.read_csv(file_path)
            """connecting to the database"""

#            engine = create_engine("mysql+mysqlconnector://neda:neda%40123@localhost/testdb")
# Upload the data
            engine = db_config.sql_engine()
            table_name=self.filename[:-4  ]
            """uploading data to the database"""
            df.to_sql(table_name, con=engine, if_exists='append', index=False)

        except Exception as e:
        #creating exception message
            """In case of exception, print the 
            traceback and log the error message"""
            traceback.print_exc()
            self.log.info(f"Data import failed: {e}")
               