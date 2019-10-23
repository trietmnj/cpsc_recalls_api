import exceptions


class URLBuilder:
    """Builds json-based query url using a fluent interface"""
    BASE_URL = "https://www.saferproducts.gov/RestWebServices/Recall?format=json"
    AVAILABLE_ARG_NAMES = [
        "RecallID",
        "RecallNumber",
        "RecallDateStart",
        "RecallDateEnd",
        "LastPublishDateStart",
        "LastPublishDateEnd",
        "RecallURL",
        "RecallTitle",
        "ConsumerContact",
        "RecallDescription",
        "ProductName",
        "ProductDescription",
        "ProductModel",
        "ProductType",
        "InconjunctionURL",
        "ImageURL",
        "Injury",
        "Manufacturer",
        "Retailer",
        "Importer",
        "Distributor",
        "ManufacturerCountry",
        "UPC",
        "Hazard",
        "Remedy",
        "RemedyOption"
    ]Returns string url
    __arg_list = dict()
    url = ""

    def add_recall_title(self, recall_title: str):
        self.__add_url_arg("RecallTitle", recall_title)
        return self

    def add_arg(self, arg_name: str, arg_param: str):
        self.__add_url_arg(arg_name, arg_param)
        return self

    def build(self) -> None:
        """Builds url"""
        self.url = self.BASE_URL if len(self.__arg_list.keys()) == 0 \
            else (self.BASE_URL + "&" + "&".join([key+"="+value for key, value in self.__arg_list.items()]))

    def get_url(self) -> str:
        """Returns string url"""
        return self.url

    def __add_url_arg(self, arg_name: str, arg_param: str) -> None:
        """Argument validation"""
        if arg_name not in self.AVAILABLE_ARG_NAMES:
            raise exceptions.InvalidRestApiArgumentNameError
        else:
            self.__arg_list[arg_name] = arg_param
