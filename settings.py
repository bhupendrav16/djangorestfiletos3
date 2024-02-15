#install boto3 and django-storage

AWS_ACCESS_KEY_ID = 'your access id'
AWS_SECRET_ACCESS_KEY= 'your access key'
AWS_STORAGE_BUCKET_NAME='bucket name'
AWS_S3_SIGNATURE_NAME='s3v4'
AWS_S3_REGION_NAME='region name'
AWS_S3_FILE_OVERWRITE=False
AWS_DEFAULT_ACT=None
AWS_S3_VERIFY= True
DEFAULT_FILE_STORAGE= 'storages.backends.s3boto3.S3Boto3Storage'



#in urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)
