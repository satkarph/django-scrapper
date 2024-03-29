import io
import pandas as pd
import boto3
from .models import File,Switch_Scrap

def store_s3(filecsv,folder,filename,FileName):
    df = pd.read_csv(filecsv,error_bad_lines=False)
    index = df.index
    number_of_rows = len(index)
    with io.BytesIO() as output:
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer,index=False)
        data = output.getvalue()

    bucketname = "scrapers1"
    # bucketname = "iatcrm"


    s3 = boto3.resource('s3')
    s3.Bucket(bucketname).put_object(Key='{0}/{1}'.format(folder, filename), Body=data, ACL='public-read')
    url = "https://{0}.s3.amazonaws.com/{1}/{2}".format(bucketname, folder, filename)
    File.objects.create(name=folder,url=url,column=number_of_rows,fileName=FileName)
    return url


def northville_s3(filecsv,folder,filename,FileName):
    df = pd.read_csv(filecsv)
    index = df.index
    number_of_rows = len(index)
    bucketname = "scrapers1"
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer)
    s3 = boto3.resource('s3')
    s3.Bucket(bucketname).put_object(Key='{0}/{1}'.format(folder, filename), Body=csv_buffer.getvalue(), ACL='public-read')
    url = "https://{0}.s3.amazonaws.com/{1}/{2}".format(bucketname, folder, filename)
    File.objects.create(name=folder,url=url,column=number_of_rows,fileName=FileName)
    return url


def check_status():
    a=Switch_Scrap.objects.all()
    if a:
        obj = a[0]
        obj.stop =False
        obj.save()
    else:
       da= Switch_Scrap.objects.create(stop=False)
