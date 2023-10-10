from extract_utils import extract_file
from transform_utils import transform_data
from dotenv import load_dotenv
import os

load_dotenv()

zip_path = os.getenv('ZIP_PATH')
ext_path = os.getenv('EXTRACT_PATH')
file_path = os.getenv('FILE_PATH')
file_tran = os.getenv('FILE_TRAN')
suffixName = "4739429"

if extract_file(zip_path, suffixName, ext_path):
    transform_data(file_path, file_tran)