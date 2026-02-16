"""
S3 Service para subir informes de sesiones en formato .md
"""
import boto3
from botocore.exceptions import ClientError
from datetime import datetime
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()


class S3Service:
    """Servicio para manejar subidas de archivos a S3"""

    def __init__(self):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=os.getenv('AMAZON_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AMAZON_SECRET_ACCESS_KEY'),
            region_name=os.getenv('AMAZON_REGION', 'us-east-1')
        )
        self.bucket_name = os.getenv('S3_BUCKET_NAME')

    def upload_session_report(
        self,
        session_id: str,
        content: str,
        github_handle: str
    ) -> Optional[str]:
        """
        Sube un informe de sesión a S3 en formato .md

        Args:
            session_id: UUID de la sesión
            content: Contenido markdown del informe
            github_handle: Handle de GitHub del owner

        Returns:
            URL pública del archivo en S3, o None si falla
        """
        # Generar nombre del archivo con timestamp
        timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
        file_name = f"{session_id}_{timestamp}.md"

        # Path en S3: reports/{github_handle}/{session_id}_{timestamp}.md
        s3_key = f"reports/{github_handle}/{file_name}"

        try:
            # Subir archivo a S3
            # El acceso público se configura via Bucket Policy (no ACL)
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=s3_key,
                Body=content.encode('utf-8'),
                ContentType='text/markdown',
                ContentDisposition='inline',
                Metadata={
                    'session_id': session_id,
                    'owner': github_handle,
                    'uploaded_at': timestamp
                }
            )

            # Generar URL pública PERMANENTE
            # Este link funciona indefinidamente mientras el archivo exista
            url = f"https://{self.bucket_name}.s3.amazonaws.com/{s3_key}"

            return url

        except ClientError as e:
            print(f"Error uploading to S3: {e}")
            return None

    def delete_session_report(self, report_url: str) -> bool:
        """
        Elimina un informe de sesión de S3

        Args:
            report_url: URL del archivo a eliminar

        Returns:
            True si se eliminó exitosamente, False si falla
        """
        try:
            # Extraer key del URL
            # https://bucket.s3.amazonaws.com/reports/user/file.md -> reports/user/file.md
            s3_key = report_url.split('.com/')[-1]

            self.s3_client.delete_object(
                Bucket=self.bucket_name,
                Key=s3_key
            )

            return True

        except ClientError as e:
            print(f"Error deleting from S3: {e}")
            return False


# Singleton instance
s3_service = S3Service()
