from celery import shared_task
from celery_progress.backend import ProgressRecorder
from .utils import scraper_spectra,airtex,scraper_usmotorworks,scraper_densoautoparts,scraper_carter,scraper_opticat,scraper_standard,scraper_BWD ,\
    scraper_WVE
import csv
import boto3
import pandas as pd
from .utils2 import store_s3

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
        wr.writerow(["Input Part #","Output Part#","Part Name","OE"])
        total = len(duration)
        for i,row in enumerate(duration):
            a = scraper_spectra(row)
            progress_recorder.set_progress(i+1, total, row)
            for b in a:
                wr.writerow(b)

    # f = open("ecat.csv", "r", encoding='utf-8')
    # g=f.read()

    a= File.objects.all().count()+1
    filename="spectrapremium"+str(a)+".xlsx"
    folder = "ecaTspectrapremiumCom"
    url = store_s3(filecsv="ecat.csv", folder=folder, filename=filename)

    return url


@shared_task(bind=True)
def sairtex(self, duration):
    progress_recorder = ProgressRecorder(self)
    with open("air.csv", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(["Input Part #","Output Part#","Part Name","OE"])
        total = len(duration)
        for i,row in enumerate(duration):
            a = airtex(row)
            progress_recorder.set_progress(i+1, total, row)
            for b in a:
                wr.writerow(b)
    #
    # f = open("air.xlsx", "r", encoding='utf-8')
    # g=f.read()

    a= File.objects.all().count()+1
    filename="Airtex"+str(a)+".xlsx"
    folder = "Airtex"
    url = store_s3(filecsv="air.csv", folder=folder, filename=filename)


    return url




@shared_task(bind=True)
def webmotors(self, duration):
    progress_recorder = ProgressRecorder(self)
    with open("motor.csv", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(["Input Part # (Mfg. Part Number)","Output - Part Number#","Source","Part Type"])
        total = len(duration)
        for i,row in enumerate(duration):
            a = scraper_usmotorworks(row)
            print(a)
            progress_recorder.set_progress(i+1, total, row)
            for b in a:
                wr.writerow(b)

    # f = open("motor.xlsx", "r", encoding='utf-8')
    # g =f.read()
    #
    a = File.objects.all().count()+1
    filename="Usmotor"+str(a)+".xlsx"

    folder = "Usmotor"
    url = store_s3(filecsv="motor.csv", folder=folder, filename=filename)
    return url




@shared_task(bind=True)
def autoparts(self, duration):
    progress_recorder = ProgressRecorder(self)
    with open("DENSAutoparts.csv", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(["Input Part # (Mfg. Part Number)","Output - Part Number#","Source","Part Type"])
        total = len(duration)
        for i,row in enumerate(duration):
            a = scraper_densoautoparts(row)
            print(a)
            progress_recorder.set_progress(i+1, total, row)
            for b in a:
                print(row)
                wr.writerow(b)
    a = File.objects.all().count()+1
    filename="DENSAutoparts"+str(a)+".xlsx"
    folder = "densoautoparts"
    url = store_s3(filecsv="DENSAutoparts.csv", folder=folder, filename=filename)
    return url

@shared_task(bind=True)
def carter(self, duration):
    progress_recorder = ProgressRecorder(self)
    with open("carter.csv", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(["Input Part # (Mfg. Part Number)","Output - Part Number#","Description","Manufacturer","Manufacturer"])
        total = len(duration)
        for i,row in enumerate(duration):
            a = scraper_carter(row)
            print(a)
            progress_recorder.set_progress(i+1, total, row)
            for b in a:
                wr.writerow(b)
    a = File.objects.all().count()+1
    filename="carter"+str(a)+".xlsx"
    folder = "Carter"
    url = store_s3(filecsv="carter.csv", folder=folder, filename=filename)
    return url


@shared_task(bind=True)
def opticat(self, duration):
    progress_recorder = ProgressRecorder(self)
    with open("opticat.csv", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(["Input Part # (Mfg. Part Number)","Output - Part Number#","Manufacturer","	OE (Item/part Description)","OE Number (Item/Part Description)"])
        total = len(duration)
        for i,row in enumerate(duration):
            a = scraper_opticat(row)
            print(a)
            progress_recorder.set_progress(i+1, total, row)
            for b in a:
                wr.writerow(b)

    #
    a = File.objects.all().count()+1
    filename="opticat"+str(a)+".xlsx"
    folder = "Opticat"
    url = store_s3(filecsv="opticat.csv", folder=folder, filename=filename)
    return url


@shared_task(bind=True)
def standard(self, duration):
    progress_recorder = ProgressRecorder(self)
    with open("standard.csv", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(["Input Part # (Mfg. Part Number)","Output - Part Number#","Part Type (Product Mfg. Name)","OE Number (Item/Part Description)"])
        total = len(duration)
        for i,row in enumerate(duration):
            a = scraper_standard(row)
            print(a)
            progress_recorder.set_progress(i+1, total, row)
            for b in a:
                wr.writerow(b)
    filename="standard"+str(a)+".xlsx"
    folder = "Standard"
    url = store_s3(filecsv="standard.csv", folder=folder, filename=filename)
    return url

@shared_task(bind=True)
def bwd(self, duration):
    progress_recorder = ProgressRecorder(self)
    with open("bwd.csv", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(["Input Part # (Mfg. Part Number)","Output - Part Number#","Part Type (Product Mfg. Name)","OE Number (Item/Part Description)"])
        total = len(duration)
        for i,row in enumerate(duration):
            a = scraper_BWD(row)
            print(a)
            progress_recorder.set_progress(i+1, total, row)
            for b in a:
                wr.writerow(b)
    a = File.objects.all().count()+1
    filename="bwd"+str(a)+".xlsx"
    folder = "BWD"
    url = store_s3(filecsv="bwd.csv", folder=folder, filename=filename)
    return url

@shared_task(bind=True)
def wve(self, duration):
    progress_recorder = ProgressRecorder(self)
    with open("wve.csv", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(["Input Part # (Mfg. Part Number)","Output - Part Number#","Part Type (Product Mfg. Name)","OE Number (Item/Part Description)"])
        total = len(duration)
        for i,row in enumerate(duration):
            a = scraper_WVE(row)
            print(a)
            progress_recorder.set_progress(i+1, total, row)
            for b in a:
                wr.writerow(b)
    a = File.objects.all().count()+1
    filename="wve"+str(a)+".xlsx"
    folder = "WVE"
    url = store_s3(filecsv="wve.csv", folder=folder, filename=filename)
    return url



