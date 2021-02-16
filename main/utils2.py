import io
import pandas as pd
import boto3
from .models import File
def store_s3(filecsv,folder,filename):
    df = pd.read_csv(filecsv)
    with io.BytesIO() as output:
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer,index=False)
        data = output.getvalue()

    bucketname = "scrapers1"

    s3 = boto3.resource('s3')
    s3.Bucket(bucketname).put_object(Key='{0}/{1}'.format(folder, filename), Body=data, ACL='public-read')
    url = "https://{0}.s3.amazonaws.com/{1}/{2}".format(bucketname, folder, filename)
    File.objects.create(name=folder,url=url)
    return url


