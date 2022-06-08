from datetime import datetime, timedelta

from azure.storage.blob import generate_blob_sas, BlobSasPermissions, BlobServiceClient


class BlobService:
    def __init__(self, account_name: str, account_key: str, container: str, conn_str: str):
        self.account_name = account_name
        self.account_key = account_key
        self.container_name = container
        self.connect_str = conn_str
        self.blob_service_client = BlobServiceClient.from_connection_string(self.connect_str)

    def post_blob(self, file_path: str) -> str:
        blob_client = self.blob_service_client.get_blob_client(
            container=self.container_name,
            blob=file_path
        )
        with open(file_path, "rb") as data:
            blob_client.upload_blob(
                data,
                overwrite=True
            )
        return file_path

    def get_blob_sas(self, name: str) -> str:
        sas_blob = generate_blob_sas(
            account_name=self.account_name,
            container_name=self.container_name,
            blob_name=name,
            account_key=self.account_key,
            permission=BlobSasPermissions(read=True),
            expiry=datetime.utcnow() + timedelta(hours=3)
        )
        url = 'https://{}.blob.core.windows.net/{}/{}?{}'.format(
            self.account_name,
            self.container_name,
            name,
            sas_blob
        )
        return url
