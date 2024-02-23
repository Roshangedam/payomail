import os
import requests
from urllib.parse import urlparse, unquote
from sre_constants import MAGIC
from datetime import datetime

def get_file_type_from_url(url):
    try:
        response = requests.head(url)
        content_type = response.headers.get('content-type')

        if content_type:
            if 'application/pdf' in content_type:
                return 'pdf'
            elif 'image' in content_type:
                return 'png'
            elif 'video' in content_type:
                return 'mp4'
            elif 'audio' in content_type:
                return 'mp3'
            else:
                return ''
        else:
            with requests.get(url, stream=True) as r:
                return detect_file_type(r.content)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return 'Unknown'

def detect_file_type(file_content):
    file_type = MAGIC.Magic(mime=True).from_buffer(file_content)
    if 'application/pdf' in file_type:
        return 'pdf'
    elif 'image' in file_type:
        return 'png'
    elif 'video' in file_type:
        return 'mp4'
    elif 'audio' in file_type:
        return 'mp3'
    else:
        return ''

def download_file(file_source, max_attachment_size_bytes):
    try:
        # Determine file type and generate filename based on URL
        file_type = get_file_type_from_url(file_source)
        parsed_url = urlparse(file_source)
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        filename = None
        
        # If the URL contains a filename with extension, use it
        if parsed_url.path and '.' in parsed_url.path:
            filename = os.path.basename(unquote(parsed_url.path))
            filename = f"{os.path.splitext(filename)[0]}_{timestamp}{os.path.splitext(filename)[1]}"
        
        # If the response has a filename, use it
        if 'filename' in parsed_url.params:
            filename = parsed_url.params['filename']
        
        # If neither the URL nor the response contains a filename, generate one
        if not filename:
            filename = f"unknown_{timestamp}.{file_type.lower()}"
        
        # Download the file
        response = requests.get(file_source)
        response.raise_for_status()
        file_data = response.content
        
        # Save the file with the generated filename
        temp_folder = os.path.join(os.getcwd(), 'payomail', 'temp')
        os.makedirs(temp_folder, exist_ok=True)
        file_path = os.path.join(temp_folder, filename)

        if len(file_data) > max_attachment_size_bytes:
            return {'status': 'Failure', 'path': '', 'error_message': f"File size exceeds the maximum allowed size ({max_attachment_size_bytes} bytes)."}

        with open(file_path, 'wb') as file:
            file.write(file_data)

        return {'status': 'Success', 'path': file_path, 'error_message': ''}
    
    except requests.exceptions.RequestException as e:
        return {'status': 'Failure', 'path': '', 'error_message': f"Error downloading file: {str(e)}"}
    
    except Exception as e:
        return {'status': 'Failure', 'path': '', 'error_message': f"An unexpected error occurred: {str(e)}"}

def get_size_by_path(file_path):
    try:
        os.path.exists(file_path)
        size:int
        return {'status': 'Failure', 'size': os.path.getsize(file_path), 'error_message': f"error: {str(e)}"}
    except Exception as e:
        return {'status': 'Failure', 'size': -1, 'error_message': f"error: {str(e)}"}
