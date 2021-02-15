from celery import shared_task
from celery_progress.backend import ProgressRecorder
from .utils import scraper_spectra,airtex,scraper_usmotorworks,scraper_densoautoparts,scraper_carter,scraper_opticat,scraper_standard,scraper_BWD
import csv
import boto3
import time
from time import sleep


# @shared_task(bind=True)
# def my_task(self, seconds):
#     progress_recorder = ProgressRecorder(self)
#     result = 0
#     for i in range(seconds):
#         time.sleep(1)
#         result += i
#         progress_recorder.set_progress(i + 1, seconds)
#     return result

# @shared_task(bind=True)
# def go_to_sleep(self, uuid):
#     progress_recorder = ProgressRecorder(self)
#     length = len(uuid)
#     for count,i in enumerate(uuid):
#         # a =scraper_spectra(i)
#         time.sleep(20)
#         progress_recorder.set_progress(count, length, f'Hiiiiiiiiiiiiiiiiiii  {i}')
#         print("heheheheh")
#     return 'Done'

from .models import File


@shared_task(bind=True)
def go_to_sleep(self, duration):
    progress_recorder = ProgressRecorder(self)
    with open("ecat.xlsx", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        # wr.writerow(["Input Part #","Output Part#","Part Name","OE"])
        total = len(duration)
        for i,row in enumerate(duration):
            a = scraper_spectra(row[0])
            progress_recorder.set_progress(i+1, total, row[0])
            for b in a:
                wr.writerow(b)

    f = open("ecat.xlsx", "r", encoding='utf-8')
    g=f.read()

    a= File.objects.all().count()+1
    filename="spectrapremium"+str(a)+".xlsx"
    s3 = boto3.resource('s3')
    bucketname = "scrapers1"
    folder = "spectrapremium"
    s3.Bucket(bucketname).put_object(ContentType= "'text/csv'", ACL='public-read',
                                     Key='{0}/{1}'.format(folder, filename), Body=g)
    url = "https://{0}.s3.amazonaws.com/{1}/{2}".format(bucketname, folder, filename)
    print(url)
    File.objects.create(name="spectrapremium",url=url)

    return url


@shared_task(bind=True)
def sairtex(self, duration):
    progress_recorder = ProgressRecorder(self)
    with open("air.xlsx", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(["Input Part #","Output Part#","Part Name","OE"])
        total = len(duration)
        for i,row in enumerate(duration):
            a = airtex(row[0])
            progress_recorder.set_progress(i+1, total, row[0])
            for b in a:
                wr.writerow(b)

    f = open("air.xlsx", "r", encoding='utf-8')
    g=f.read()

    a= File.objects.all().count()+1
    filename="Airtex"+str(a)+".xlsx"
    s3 = boto3.resource('s3')
    bucketname = "scrapers1"
    folder = "Airtex"
    s3.Bucket(bucketname).put_object(ContentType= "'text/csv'", ACL='public-read',
                                     Key='{0}/{1}'.format(folder, filename), Body=g)
    url = "https://{0}.s3.amazonaws.com/{1}/{2}".format(bucketname, folder, filename)
    print(url)
    File.objects.create(name="Airtex",url=url)
    return url




@shared_task(bind=True)
def webmotors(self, duration):
    progress_recorder = ProgressRecorder(self)
    with open("motor.xlsx", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(["Input Part # (Mfg. Part Number)","Output - Part Number#","Source","Part Type"])
        total = len(duration)
        for i,row in enumerate(duration):
            a = scraper_usmotorworks(row[0])
            print(a)
            progress_recorder.set_progress(i+1, total, row[0])
            for b in a:
                wr.writerow(b)

    f = open("motor.xlsx", "r", encoding='utf-8')
    g =f.read()
    #
    a = File.objects.all().count()+1
    filename="Usmotor"+str(a)+".xlsx"
    s3 = boto3.resource('s3')
    bucketname = "scrapers1"
    folder = "Usmotor"
    s3.Bucket(bucketname).put_object(ContentType= "'text/csv'", ACL='public-read',
                                     Key='{0}/{1}'.format(folder, filename), Body=g)
    url = "https://{0}.s3.amazonaws.com/{1}/{2}".format(bucketname, folder, filename)
    print(url)
    File.objects.create(name="Usmotor",url=url)
    return url




@shared_task(bind=True)
def autoparts(self, duration):
    progress_recorder = ProgressRecorder(self)
    with open("DENSAutoparts.xlsx", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(["Input Part # (Mfg. Part Number)","Output - Part Number#","Source","Part Type"])
        total = len(duration)
        for i,row in enumerate(duration):
            a = scraper_densoautoparts(row[0])
            print(a)
            progress_recorder.set_progress(i+1, total, row[0])
            for b in a:
                print(row[0])
                wr.writerow(b)

    f = open("DENSAutoparts.xlsx", "r", encoding='utf-8')
    g =f.read()
    #
    a = File.objects.all().count()+1
    filename="DENSAutoparts"+str(a)+".xlsx"
    s3 = boto3.resource('s3')
    bucketname = "scrapers1"
    folder = "DENSAutoparts"
    s3.Bucket(bucketname).put_object(ContentType= "'text/csv'", ACL='public-read',
                                     Key='{0}/{1}'.format(folder, filename), Body=g)
    url = "https://{0}.s3.amazonaws.com/{1}/{2}".format(bucketname, folder, filename)
    print(url)
    File.objects.create(name="DENSAutoparts",url=url)
    return url

@shared_task(bind=True)
def carter(self, duration):
    progress_recorder = ProgressRecorder(self)
    with open("carter.xlsx", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(["Input Part # (Mfg. Part Number)","Output - Part Number#","Description","Manufacturer","Manufacturer"])
        total = len(duration)
        for i,row in enumerate(duration):
            a = scraper_carter(row[0])
            print(a)
            progress_recorder.set_progress(i+1, total, row[0])
            for b in a:
                wr.writerow(b)

    f = open("carter.xlsx", "r", encoding='utf-8')
    g =f.read()
    #
    a = File.objects.all().count()+1
    filename="carter"+str(a)+".xlsx"
    s3 = boto3.resource('s3')
    bucketname = "scrapers1"
    folder = "Carter"
    s3.Bucket(bucketname).put_object(ContentType= "'text/csv'", ACL='public-read',
                                     Key='{0}/{1}'.format(folder, filename), Body=g)
    url = "https://{0}.s3.amazonaws.com/{1}/{2}".format(bucketname, folder, filename)
    print(url)
    File.objects.create(name="Carter",url=url)
    return url


@shared_task(bind=True)
def opticat(self, duration):
    progress_recorder = ProgressRecorder(self)
    with open("opticat.xlsx", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(["Input Part # (Mfg. Part Number)","Output - Part Number#","Manufacturer","	OE (Item/part Description)","OE Number (Item/Part Description)"])
        total = len(duration)
        for i,row in enumerate(duration):
            a = scraper_opticat(row[0])
            print(a)
            progress_recorder.set_progress(i+1, total, row[0])
            for b in a:
                wr.writerow(b)

    f = open("opticat.xlsx", "r", encoding='utf-8')
    g =f.read()
    #
    a = File.objects.all().count()+1
    filename="opticat"+str(a)+".xlsx"
    s3 = boto3.resource('s3')
    bucketname = "scrapers1"
    folder = "Opticat"
    s3.Bucket(bucketname).put_object(ContentType= "'text/csv'", ACL='public-read',
                                     Key='{0}/{1}'.format(folder, filename), Body=g)
    url = "https://{0}.s3.amazonaws.com/{1}/{2}".format(bucketname, folder, filename)
    print(url)
    File.objects.create(name="Opticat",url=url)
    return url


@shared_task(bind=True)
def standard(self, duration):
    progress_recorder = ProgressRecorder(self)
    with open("standard.xlsx", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(["Input Part # (Mfg. Part Number)","Output - Part Number#","Part Type (Product Mfg. Name)","OE Number (Item/Part Description)"])
        total = len(duration)
        for i,row in enumerate(duration):
            a = scraper_standard(row[0])
            print(a)
            progress_recorder.set_progress(i+1, total, row[0])
            for b in a:
                wr.writerow(b)

    f = open("standard.xlsx", "r", encoding='utf-8')
    g =f.read()
    #
    a = File.objects.all().count()+1
    filename="standard"+str(a)+".xlsx"
    s3 = boto3.resource('s3')
    bucketname = "scrapers1"
    folder = "Standard"
    s3.Bucket(bucketname).put_object(ContentType= "'text/csv'", ACL='public-read',
                                     Key='{0}/{1}'.format(folder, filename), Body=g)
    url = "https://{0}.s3.amazonaws.com/{1}/{2}".format(bucketname, folder, filename)
    print(url)
    File.objects.create(name="Standard",url=url)
    return url

@shared_task(bind=True)
def bwd(self, duration):
    progress_recorder = ProgressRecorder(self)
    with open("bwd.xlsx", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(["Input Part # (Mfg. Part Number)","Output - Part Number#","Part Type (Product Mfg. Name)","OE Number (Item/Part Description)"])
        total = len(duration)
        for i,row in enumerate(duration):
            a = scraper_BWD(row[0])
            print(a)
            progress_recorder.set_progress(i+1, total, row[0])
            for b in a:
                wr.writerow(b)

    f = open("bwd.xlsx", "r", encoding='utf-8')
    g =f.read()
    #
    a = File.objects.all().count()+1
    filename="bwd"+str(a)
    s3 = boto3.resource('s3')+".xlsx"
    bucketname = "scrapers1"
    folder = "BWD"
    s3.Bucket(bucketname).put_object(ContentType= "'text/csv'", ACL='public-read',
                                     Key='{0}/{1}'.format(folder, filename), Body=g)
    url = "https://{0}.s3.amazonaws.com/{1}/{2}".format(bucketname, folder, filename)
    print(url)
    File.objects.create(name="BWD",url=url)
    return url


