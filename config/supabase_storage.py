import requests
from django.core.files.storage import Storage
from django.conf import settings
from django.utils.deconstruct import deconstructible


@deconstructible
class SupabaseStorage(Storage):
    def __init__(self):
        self.supabase_url = settings.SUPABASE_URL.rstrip("/")
        self.supabase_key = settings.SUPABASE_API_KEY
        self.bucket_name = "rcka-bucket"
        self.headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
        }

    def _save(self, name, content):
        file_path = f"{self.bucket_name}/{name}"
        upload_url = f"{self.supabase_url}/storage/v1/object/{file_path}"

        if hasattr(content, "seek"):
            content.seek(0)

        response = requests.put(
            upload_url,
            headers={**self.headers, "Content-Type": "application/octet-stream"},
            data=content.read(),
        )

        if response.status_code == 200 or response.status_code == 201:
            return name
        else:
            raise Exception(f"Failed to upload file: {response.text}")

    def exists(self, name):
        file_path = f"{self.bucket_name}/{name}"
        check_url = f"{self.supabase_url}/storage/v1/object/{file_path}"

        response = requests.get(
            check_url, headers={**self.headers, "Range": "bytes=0-0"}
        )

        return response.status_code == 206 or response.status_code == 200

    def delete(self, name):
        delete_url = f"{self.supabase_url}/storage/v1/object/{self.bucket_name}"

        response = requests.delete(
            delete_url, headers=self.headers, json={"paths": [name]}
        )

        if response.status_code not in [200, 204]:
            raise Exception(f"Failed to delete file: {response.text}")

    def url(self, name):
        return f"{self.supabase_url}/storage/v1/object/public/{self.bucket_name}/{name}"
