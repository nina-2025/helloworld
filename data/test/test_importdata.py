import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import sys
import os

# Add src to path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.abspath(os.path.join(current_dir, '..','..', 'src'))
print("this is the src path    "+src_path)
sys.path.insert(0, src_path)

from importdata import ImportData


class TestImportData(unittest.TestCase):

    @patch("importdata.sql_engine")
    @patch("importdata.pd.read_csv")
    @patch("importdata.ProjectLogger")
    def test_load_data_success(self, MockLogger, mock_read_csv, mock_sql_engine):
        # Arrange
        mock_logger = MagicMock()
        MockLogger.return_value = mock_logger

        mock_df = pd.DataFrame({"col1": [1, 2], "col2": ["a", "b"]})
        mock_df.to_sql = MagicMock()
        mock_read_csv.return_value = mock_df

        mock_engine = MagicMock()
        mock_sql_engine.return_value = mock_engine

        importer = ImportData("testfile.csv")

        # Act
        importer.load_data()

        # Assert
        mock_read_csv.assert_called_once()
        mock_df.to_sql.assert_called_once_with(
            "testfile", con=mock_engine, if_exists="append", index=False
        )
        mock_logger.info.assert_any_call("Data import started successfully.")

    @patch("importdata.sql_engine")
    @patch("importdata.pd.read_csv", side_effect=Exception("Read failed"))
    @patch("importdata.ProjectLogger")
    def test_load_data_failure_logs_error(self, MockLogger, mock_read_csv, mock_sql_engine):
        mock_logger = MagicMock()
        MockLogger.return_value = mock_logger
        importer = ImportData("badfile.csv")
        importer.load_data()
        mock_logger.info.assert_any_call("Data import failed: Read failed")
