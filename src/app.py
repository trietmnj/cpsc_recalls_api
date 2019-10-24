import sys
import os
sys.path.append("src/")
from datetime import datetime

from userinterface import UserInterface
from urlbuilder import URLBuilder
from webdao import WebDAO
from dataprocessor import DataProcessor

def main():
    ui = UserInterface()
    url_builder = URLBuilder()
    web_dao = WebDAO()
    data_processor = DataProcessor()

    url_builder\
        .set_args_dict(ui.get_args_dict())\
            .build()
    
    web_dao\
        .set_download_url(url_builder.get_url())\
            .download()
    
    data_processor\
        .set_raw_content(web_dao.get_raw_content())

    data_processor.save_json(
        f"target/cpsc_recalls_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")

if __name__ == "__main__":
    main()