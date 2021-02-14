from celery import shared_task
from celery_progress.backend import ProgressRecorder
from .utils import scraper_spectra
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
    with open("ecat.csv", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        # wr.writerow(["Input Part #","Output Part#","Part Name","OE"])
        total = len(duration)
        for i,row in enumerate(duration):
            a = scraper_spectra(row[0])
            progress_recorder.set_progress(i+1, total, row[0])
            wr.writerow(a[0])

        a= File.objects.all().count()+1
        filename="spectrapremium"+a
        s3 = boto3.resource('s3')
        bucketname = "scrapers1"
        folder = "spectrapremium"
        s3.Bucket(bucketname).put_object(ContentType= "application/CSV", ACL='public-read',
                                         Key='{0}/{1}'.format(folder, filename), Body=myfile)
        url = "https://{0}.s3.amazonaws.com/{1}/{2}".format(bucketname, folder, filename)
        print(url)
        File.objects.create(name="spectrapremium",url=url)

    return 'Done'