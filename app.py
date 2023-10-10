from flask import Flask, render_template, request, send_from_directory
from extract_utils import extract_file
from transform_utils import transform_data
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

zip_path = os.getenv('ZIP_PATH')
ext_path = os.getenv('EXTRACT_PATH')
file_path = os.getenv('FILE_PATH')
file_tran = os.getenv('FILE_TRAN')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    
    if file:
        suffixName = file.filename.replace("jobResponse", "").replace(".zip", "")
        
        # Saving the file
        upload_path = os.path.join(base_dir, app.config['UPLOAD_FOLDER'], file.filename)
        file.save(upload_path)
        
        zip_abs_path = os.path.join(base_dir, zip_path)
        ext_abs_path = os.path.join(base_dir, ext_path)
        if extract_file(zip_abs_path, suffixName, ext_abs_path):
            
            file_abs_path = os.path.join(base_dir, file_path)
            file_tran_abs_path = os.path.join(base_dir, file_tran)
            transform_data(file_abs_path, file_tran_abs_path)
        return 'File uploaded and processed. <a href="/download">Download Transformed File</a>'
    

@app.route('/download')
def download_file():
    if not os.path.isfile(file_tran):
        return f"File not found at: {file_tran}", 404
    return send_from_directory(directory=os.path.dirname(file_tran), path=os.path.basename(file_tran))

# def download_file():
#     file_path = os.path.join(file_tran, "transformed_Position.csv")
#     if os.path.exists(file_tran):
#         return send_from_directory(directory=file_tran, filename="transformed_Position.csv")
#     else:
#         return f"File not found at: {file_tran}", 404

@app.errorhandler(500)
def handle_internal_error(error):
    return f"Internal error: {str(error)}", 500


if __name__ == '__main__':
    app.run(debug=True)
