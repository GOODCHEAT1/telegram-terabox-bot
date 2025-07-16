import requests

class TeraBoxClient:
    def __init__(self, access_token):
        self.base_url = "https://www.terabox.com/api"
        self.token = access_token
        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }

    def list_files(self):
        url = f"{self.base_url}/file/list"
        response = requests.get(url, headers=self.headers)
        if response.ok:
            return response.json()
        else:
            raise Exception(f"List files failed: {response.text}")

    def upload_file(self, file_path, file_name):
        url = f"{self.base_url}/file/upload"
        files = {'file': (file_name, open(file_path, 'rb'))}
        response = requests.post(url, headers=self.headers, files=files)
        if response.ok:
            return response.json()
        else:
            raise Exception(f"Upload failed: {response.text}")

    def download_file(self, file_id):
        url = f"{self.base_url}/file/download?file_id={file_id}"
        response = requests.get(url, headers=self.headers)
        if response.ok:
            return response.content
        else:
            raise Exception(f"Download failed: {response.text}")
