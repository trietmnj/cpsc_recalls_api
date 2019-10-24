import pandas as pd
import json
import os
import errno


class DataProcessor:
    """Clean raw data"""
    __raw_content = None
    __data_table = None

    def set_raw_content(self, raw_content: bytes):
        """Set and parse downloaded json"""
        self.__raw_content = raw_content.decode("UTF-8")
        return self

    @staticmethod
    def __cell_list_to_columns(df: pd.DataFrame, column: str):
        """Construct multiple columns based on lists within specified column cells"""
        tags = df[column].apply(pd.Series)
        tags = tags.rename(columns=lambda x: column + "_" + str(x))
        df = pd.concat([df[:], tags[:]], axis=1)
        return df

    def __construct_table(self):
        """Creates a pandas dataframe"""
        self.__data_table = pd.read_json(self.__raw_content)
        return self

    def __melt_cell_lists(self):
        """Call __cell_list_to_columns on all columns containing collections"""
        columns = ["Products", "Inconjunctions", "Images", "Injuries",
                   "Manufacturers", "Retailers", "Importers", "Distributors",
                   "ManufacturerCountries", "ProductUPCs", "Hazards",
                   "Remedies", "RemedyOptions"]
        for column in columns:
            self.__data_table = self.__cell_list_to_columns(
                self.__data_table, column)
        return self

    def process(self):
        """Automate dataframe cleanup"""
        self.__construct_table()
        self.__melt_cell_lists()
        return self

    def get_dataframe(self):
        """Returns a dataframe"""
        return self.__data_table

    def get_json(self):
        """Returns a json list"""
        return json.loads(self.__raw_content)

    def save_json(self, filename: str):
        """Save json data to file"""
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        with open(filename, "w") as file:
            json.dump(json.loads(self.__raw_content),
                      file, indent=2, sort_keys=True)
