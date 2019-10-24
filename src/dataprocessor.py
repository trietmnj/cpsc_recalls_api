import pandas as pd


class DataProcessor:
    """Clean raw data"""
    __raw_content = None
    __data_table = None

    def set_raw_content(self, raw_content):
        """Set and parse downloaded json"""
        self.__raw_content = raw_content
        return self

    @staticmethod
    def __cell_list_to_columns(df: pd.DataFrame, column: str):
        """Construct multiple columns based on lists within specified column cells"""
        tags = df[column].apply(pd.Series)
        tags = tags.rename(columns=lambda x: column + "_" + str(x))
        df = pd.concat([df[:], tags[:]], axis=1)
        return df

    def __construct_table(self):
        self.__data_table = pd.read_json(self.__raw_content)
        return self

    def __melt_cell_lists(self):
        columns = ["Products", "Inconjunctions", "Images", "Injuries",
                   "Manufacturers", "Retailers", "Importers", "Distributors",
                   "ManufacturerCountries", "ProductUPCs", "Hazards",
                   "Remedies", "RemedyOptions"]
        for column in columns:
            self.__data_table = self.__cell_list_to_columns(
                self.__data_table, column)
        return self

    def process(self):
        self.__construct_table()
        self.__melt_cell_lists()
        return self

    def get_data_table(self):
        return self.__data_table
