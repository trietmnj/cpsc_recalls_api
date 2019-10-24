import exceptions
from userinterface import UserInterface


class URLBuilder:
    """Builds json-based query url"""
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
    ]
    __arg_list = dict()
    url = ""

    def set_args_dict(self, args_list: dict):
        if args_list is not None:
            for key, value in args_list.items():
                self.add_arg(key, value)
        return self

    def add_recall_title(self, recall_title: str):
        self.__add_url_arg("RecallTitle", recall_title)
        return self

    def add_arg(self, arg_name: str, arg_param: str):
        """Add key/value pair"""
        self.__add_url_arg(arg_name, arg_param)
        return self

    def build(self) -> None:
        """Builds url"""
        self.url = self.BASE_URL if self.__arg_list is None \
            else (self.BASE_URL + "&" + "&".join([key+"="+value for key, value in self.__arg_list.items()]))

    def get_url(self) -> str:
        """Returns string url"""
        return self.url

    def __add_url_arg(self, arg_name: str, arg_param: str) -> None:
        """Argument validation"""
        if arg_name not in self.AVAILABLE_ARG_NAMES:
            raise exceptions.InvalidRestApiArgumentKeyError(
                f"{arg_name} is not an acceptable argument key. Available keys: {self.AVAILABLE_ARG_NAMES}")
        else:
            self.__arg_list[arg_name] = arg_param
