import os
from dotenv import load_dotenv
from zipfile import ZipFile as zp

def extract_file(zipDir, suffixName, extract_path):
    
    # zip_filename = os.path.join(zipDir, f"jobResponse{suffixName}.zip")
    zip_filename = os.path.join("..", zipDir, f"jobResponse{suffixName}.zip")


    if not os.path.exists(zip_filename):
        print(f"The ZIP file '{zip_filename}' does not exist.")
        return False
    with zp(zip_filename, 'r') as zObject:
        zObject.extract('Position.csv', path=extract_path)
    print(f"'Positionx.csv' extracted to '{extract_path}'.")
    return True

# def main():
    
#     load_dotenv()
    

#     if __name__ == "__main__":
#         main()