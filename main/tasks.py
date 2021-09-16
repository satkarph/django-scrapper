from celery import shared_task
from celery_progress.backend import ProgressRecorder
from .utils import scraper_spectra,airtex,scraper_usmotorworks,scraper_densoautoparts,scraper_carter,scraper_opticat,scraper_standard,scraper_BWD ,\
    scraper_WVE,scraper_oreillyautoparts,scraper_autozone,scraper_advanceautoparts,webscraper_nepalonline,webscraplara
import csv
import boto3
import pandas as pd
from .utils2 import store_s3,northville_s3
from .northville import scrape_northville
import time
from time import sleep
import pandas as pd
from .social import main_socailmedia


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

from .models import File,Switch_Scrap


@shared_task(bind=True)
def go_to_sleep(self, duration,fileName):
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
            check =Switch_Scrap.objects.all()[0]
            stop = check.stop
            if stop:
                break


    # f = open("ecat.csv", "r", encoding='utf-8')
    # g=f.read()

    a= File.objects.all().count()+1
    filename="spectrapremium"+str(a)+".xlsx"
    folder = "ecaTspectrapremiumCom"
    url = store_s3(filecsv="ecat.csv", folder=folder, filename=filename,FileName=fileName)

    return url


@shared_task(bind=True)
def sairtex(self, duration,fileName):
    progress_recorder = ProgressRecorder(self)
    with open("air.csv", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(["Input Part #","Output Part#","OE","Part Name"])
        total = len(duration)
        for i,row in enumerate(duration):
            a = airtex(row)
            progress_recorder.set_progress(i+1, total, row)
            for b in a:
                wr.writerow(b)
            check = Switch_Scrap.objects.all()[0]
            stop = check.stop
            if stop:
                break
    #
    # f = open("air.xlsx", "r", encoding='utf-8')
    # g=f.read()

    a= File.objects.all().count()+1
    filename="Airtex"+str(a)+".xlsx"
    folder = "Airtex"
    url = store_s3(filecsv="air.csv", folder=folder, filename=filename,FileName=fileName)


    return url




@shared_task(bind=True)
def webmotors(self, duration,fileName):
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
            check = Switch_Scrap.objects.all()[0]
            stop = check.stop
            if stop:
                break

    # f = open("motor.xlsx", "r", encoding='utf-8')
    # g =f.read()
    #
    a = File.objects.all().count()+1
    filename="Usmotor"+str(a)+".xlsx"

    folder = "Usmotor"
    url = store_s3(filecsv="motor.csv", folder=folder, filename=filename,FileName=fileName)
    return url




@shared_task(bind=True)
def autoparts(self, duration,fileName):
    progress_recorder = ProgressRecorder(self)
    with open("DENSAutoparts.csv", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(["Input Part # (Mfg. Part Number)","Manufacturer","Part Type","DENSO Part Number"])
        total = len(duration)
        for i,row in enumerate(duration):
            a = scraper_densoautoparts(row)
            print(a)
            progress_recorder.set_progress(i+1, total, row)
            for b in a:
                print(row)
                wr.writerow(b)
            check = Switch_Scrap.objects.all()[0]
            stop = check.stop
            if stop:
                break
    a = File.objects.all().count()+1
    filename="DENSAutoparts"+str(a)+".xlsx"
    folder = "densoautoparts"
    url = store_s3(filecsv="DENSAutoparts.csv", folder=folder, filename=filename,FileName=fileName)
    return url

@shared_task(bind=True)
def carter(self, duration,fileName):
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
            check = Switch_Scrap.objects.all()[0]
            stop = check.stop
            if stop:
                break
    a = File.objects.all().count()+1
    filename="carter"+str(a)+".xlsx"
    folder = "Carter"
    url = store_s3(filecsv="carter.csv", folder=folder, filename=filename,FileName=fileName)
    return url


@shared_task(bind=True)
def opticat(self, duration,fileName):
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
            check = Switch_Scrap.objects.all()[0]
            stop = check.stop
            if stop:
                break

    #
    a = File.objects.all().count()+1
    filename="opticat"+str(a)+".xlsx"
    folder = "Opticat"
    url = store_s3(filecsv="opticat.csv", folder=folder, filename=filename,FileName=fileName)
    return url


@shared_task(bind=True)
def standard(self, duration,fileName):
    progress_recorder = ProgressRecorder(self)
    with open("standard.csv", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(["Input Part","Input Part # Description","Output - Part Number#","Part Type (Product Mfg. Name)","OE Number (Item/Part Description)"])
        total = len(duration)
        for i,row in enumerate(duration):
            a = scraper_standard(row)
            try:
                a.pop(1)
            except:
                pass
            print(a)
            progress_recorder.set_progress(i+1, total, row)
            for b in a:
                wr.writerow(b)
            check = Switch_Scrap.objects.all()[0]
            stop = check.stop
            if stop:
                break
    a = File.objects.all().count()+1
    filename="standard"+str(a)+".xlsx"
    folder = "Standard"
    url = store_s3(filecsv="standard.csv", folder=folder, filename=filename,FileName=fileName)
    return url

@shared_task(bind=True)
def bwd(self, duration,fileName):
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
                try:
                    b.pop(3)
                except:
                    pass
                wr.writerow(b)
            check = Switch_Scrap.objects.all()[0]
            stop = check.stop
            if stop:
                break
    a = File.objects.all().count()+1
    filename="bwd"+str(a)+".xlsx"
    folder = "BWD"
    url = store_s3(filecsv="bwd.csv", folder=folder, filename=filename,FileName=fileName)
    return url

@shared_task(bind=True)
def wve(self, duration,fileName):
    progress_recorder = ProgressRecorder(self)
    with open("wve.csv", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        # wr.writerow(["Input Part #","OE (Competitor Brand)","Competitor Part No.","Output – (WVE Part No.)","Part Type (Description)"])
        wr.writerow(["Input Part # (Mfg. Part Number)","OE (Comp/OE)","Output – Part#","Part Type"])

        total = len(duration)
        for i,row in enumerate(duration):
            a = scraper_WVE(row)
            print(a)
            progress_recorder.set_progress(i+1, total, row)
            for b in a:
                try:
                    b.pop(2)
                except:
                    pass
                print(b)
                wr.writerow(b)
            check = Switch_Scrap.objects.all()[0]
            stop = check.stop
            if stop:
                break
    a = File.objects.all().count()+1
    filename="wve"+str(a)+".xlsx"
    folder = "WVE"
    url = store_s3(filecsv="wve.csv", folder=folder, filename=filename,FileName=fileName)
    return url



@shared_task(bind=True)
def oreo(self, duration,fileName):
    progress_recorder = ProgressRecorder(self)
    with open("oreo.csv", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        # wr.writerow(["Input Part #","OE (Competitor Brand)","Competitor Part No.","Output – (WVE Part No.)","Part Type (Description)"])
        wr.writerow(["Input Part ","Output – Part#","Mfg and Part Type","Line","Replace"])

        total = len(duration)
        for i,row in enumerate(duration):
            a = scraper_oreillyautoparts(row)
            print(a)
            progress_recorder.set_progress(i+1, total, row)
            for b in a:
                wr.writerow(b)
            check = Switch_Scrap.objects.all()[0]
            stop = check.stop
            if stop:
                break
    a = File.objects.all().count()+1
    filename="oreillyautoparts"+str(a)+".xlsx"
    folder = "Oreillyautoparts"
    url = store_s3(filecsv="oreo.csv", folder=folder, filename=filename,FileName=fileName)
    return url

@shared_task(bind=True)
def autozone(self, duration,fileName):
    progress_recorder = ProgressRecorder(self)
    with open("autozone.csv", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        # wr.writerow(["Input Part #","OE (Competitor Brand)","Competitor Part No.","Output – (WVE Part No.)","Part Type (Description)"])
        wr.writerow(["Input Part ","Output – Part#","Mfg and Part Type","Price"])

        total = len(duration)
        for i,row in enumerate(duration):
            a = scraper_autozone(row)
            print(a)
            progress_recorder.set_progress(i+1, total, row)
            for b in a:
                wr.writerow(b)
            check = Switch_Scrap.objects.all()[0]
            stop = check.stop
            if stop:
                break
    a = File.objects.all().count()+1
    filename="autozone"+str(a)+".xlsx"
    folder = "Autozone"
    url = store_s3(filecsv="autozone.csv", folder=folder, filename=filename,FileName=fileName)
    return url



@shared_task(bind=True)
def advance(self, duration,fileName):
    progress_recorder = ProgressRecorder(self)
    with open("advance.csv", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        # wr.writerow(["Input Part #","OE (Competitor Brand)","Competitor Part No.","Output – (WVE Part No.)","Part Type (Description)"])
        wr.writerow(["Input Part ","Output – Part#","Mfg and Part Type","Price"])

        total = len(duration)
        for i,row in enumerate(duration):
            a = scraper_advanceautoparts(row)
            print(a)
            progress_recorder.set_progress(i+1, total, row)
            for b in a:
                wr.writerow(b)
            check = Switch_Scrap.objects.all()[0]
            stop = check.stop
            if stop:
                break
    a = File.objects.all().count()+1
    filename="advanceautopatrs"+str(a)+".xlsx"
    folder = "AdvanceAutoparts"
    url = store_s3(filecsv="advance.csv", folder=folder, filename=filename,FileName=fileName)
    return url




@shared_task(bind=True)
def nepalonline(self, duration,fileName):
    progress_recorder = ProgressRecorder(self)
    with open("napa.csv", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        # wr.writerow(["Input Part #","OE (Competitor Brand)","Competitor Part No.","Output – (WVE Part No.)","Part Type (Description)"])
        wr.writerow(["Input Part ","Output – Part#","Mfg and Part Type","OE(Product Line)"," Online Price"])

        total = len(duration)
        for i,row in enumerate(duration):
            a = webscraper_nepalonline(row)
            print(a)
            progress_recorder.set_progress(i+1, total, row)
            for b in a:
                wr.writerow(b)
            check = Switch_Scrap.objects.all()[0]
            stop = check.stop
            if stop:
                break
    a = File.objects.all().count()+1
    filename="napaonline"+str(a)+".xlsx"
    folder = "NapaOnline"
    url = store_s3(filecsv="napa.csv", folder=folder, filename=filename,FileName=fileName)
    return url


@shared_task(bind=True)
def laratask(self, duration,fileName):
    progress_recorder = ProgressRecorder(self)
    with open("lara.csv", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        # wr.writerow(["Input Part #","OE (Competitor Brand)","Competitor Part No.","Output – (WVE Part No.)","Part Type (Description)"])
        wr.writerow(["Input Company Name","IDNumber","EntityNameHead","EntityName","NameChange","EntityType","EntityIDNumber","EntityIDOldNumber","DateOfOrganization",
                     "DateOfOrganizationInactive","Purpose","Term","ResidentAgentName","ResidentStreetAddress","ResidentApt","ResidentCity","ResidentState",
                     "ResidentZip","PrincipleStreet","PrincipleApt","PrincipleCity","PrincipleState","PrincipleZip","ActFormedUnder","ManagedBy",
                     "Name of filing","Year filed","Date filed","Filling No","View Pdf"])

        total = len(duration)
        for i,row in enumerate(duration):
            # if i==0:
            #     continue
            a = webscraplara(row)
            print(a)
            progress_recorder.set_progress(i+1, total, row)
            for b in a:
                wr.writerow(b)
            check = Switch_Scrap.objects.all()[0]
            stop = check.stop
            if stop:
                break
    a = File.objects.all().count()+1
    filename="lara"+str(a)+".xlsx"
    folder = "Lara"
    url = store_s3(filecsv="lara.csv", folder=folder, filename=filename,FileName=fileName)
    return url



@shared_task(bind=True)
def northvilletask(self, duration,fileName):
    progress_recorder = ProgressRecorder(self)
    total = len(duration)
    whole_data=[]
    for i,row in enumerate(duration):
        # if i==0:
        #     continue
        a = scrape_northville(row)
        if a:
            whole_data = whole_data + a
        print("++++++++++++++++++++++++++++++++++++++++++++++++++")
        progress_recorder.set_progress(i+1, total, row)
        check = Switch_Scrap.objects.all()[0]
        stop = check.stop
        if stop:
            break
    a = File.objects.all().count()+1
    merged_df = pd.concat(whole_data)
    merged_df.to_csv('northville.csv')
    folder = "northville"
    filename="northville{0}.csv".format(str(a))
    url = northville_s3(filecsv="northville.csv", folder=folder, filename=filename,FileName=fileName)
    return url




@shared_task(bind=True)
def socialmedia(self, duration,fileName):
    progress_recorder = ProgressRecorder(self)
    with open("social.csv", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        # wr.writerow(["Input Part #","OE (Competitor Brand)","Competitor Part No.","Output – (WVE Part No.)","Part Type (Description)"])
        wr.writerow(['Input Company Name', 'Address', 'City', 'State', 'Zipcode', 'Website', 'latitude', 'Longitude', 'Facebook link', 'Facebook # followers', 'Facebook # Posts', 'Instagram link', 'Instagram # followers', 'Instagram # Posts', 'Twitter link', 'Twitter # followers', 'Twitter # Posts', 'LinkedIn link', 'LinkedIn # followers', 'LinkedIn # Posts', 'Pinterest link', 'Pinterest # followers', 'Pinterest # Posts'])

        total = len(duration)
        print(total)
        for i, row in enumerate(duration):
            if i==0:
                continue
            print("daaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            print("i am ogonal data ")
            print(row)
            if row['company']==None:
                break
            print("daaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaataaaaaaaaaaaaaaaaaa")
            a = main_socailmedia(row)

            progress_recorder.set_progress(i + 1, total, row)
            for b in a:
                wr.writerow(b)
            check = Switch_Scrap.objects.all()[0]
            stop = check.stop
            if stop:
                break
    a = File.objects.all().count() + 1
    filename = "social" + str(a) + ".xlsx"
    folder = "Socail"
    url = store_s3(filecsv="social.csv", folder=folder, filename=filename, FileName=fileName)
    return url


