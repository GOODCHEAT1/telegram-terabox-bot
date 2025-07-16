from terabox import Terabox

class TeraBoxClient:
    def __init__(self, email, password):
        self.client = Terabox(email, password)
        self.client.login()

    def list_files(self):
        return self.client.list_files()

    def get_download_link(self, file_id):
        return self.client.get_download_link(file_id)
