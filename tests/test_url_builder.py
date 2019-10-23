import sys
sys.path.append("src/")
import pytest

from url_builder import URLBuilder
import exceptions

def test_add_recall_title():
    builder = URLBuilder()
    builder.add_recall_title("child").build()
    assert builder.url == "https://www.saferproducts.gov/RestWebServices/Recall?format=json&RecallTitle=child"

def test_invalid_param_name_exception():
    builder = URLBuilder()
    with pytest.raises(exceptions.InvalidRestApiArgumentNameError):
        builder.add_arg("RandomArgName", "random")
