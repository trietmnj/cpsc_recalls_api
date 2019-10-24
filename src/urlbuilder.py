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
    __arg_list = None
    url = ""

    def set_args_dict(self, args_list: dict):
        self.__arg_list = args_list
        if self.__arg_list is not None:
            for key in self.__arg_list.keys():
                if key not in self.AVAILABLE_ARG_NAMES:
                    raise exceptions.InvalidRestApiKeyValuePair(
                        f"{key} is not an acceptable argument key")
        return self

    def add_recall_title(self, recall_title: str):
        self.__add_url_arg("RecallTitle", recall_title)
        return self

    def add_arg(self, arg_name: str, arg_param: str):
        self.__add_url_arg(arg_name, arg_param)
        return self

    def build(self) -> None:
        """Builds url"""
        # list validation

        self.url = self.BASE_URL if self.__arg_list is None \
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
