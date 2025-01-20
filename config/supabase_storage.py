import requests
from django.core.files.storage import Storage
from django.conf import settings
from django.utils.deconstruct import deconstructible


@deconstructible
class SupabaseStorage(Storage):
    def __init__(self):
        self.supabase_url = settings.SUPABASE_URL
        self.supabase_key = settings.SUPABASE_API_KEY
        self.bucket_name = "rcka-bucket"
        self.headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/octet-stream",
        }

    def _save(self, name, content):
        file_path = f"{self.bucket_name}/{name}"
        upload_url = f"{self.supabase_url}/storage/v1/object/{file_path}"
        response = requests.post(upload_url, headers=self.headers, data=content.read())
        if response.status_code == 200:
            return name
        else:
            raise Exception(f"Failed to upload file: {response.text}")

    def exists(self, name):
        file_path = f"{self.bucket_name}/{name}"
        check_url = f"{self.supabase_url}/storage/v1/object/{file_path}"
        response = requests.head(check_url, headers=self.headers)
        return response.status_code == 200

    def delete(self, name):
        file_path = f"{self.bucket_name}/{name}"
        delete_url = f"{self.supabase_url}/storage/v1/object/{file_path}"
        response = requests.delete(delete_url, headers=self.headers)
        if response.status_code != 200:
            raise Exception(f"Failed to delete file: {response.text}")

    def url(self, name):
        return f"{self.supabase_url}/storage/v1/object/public/{self.bucket_name}/{name}"
