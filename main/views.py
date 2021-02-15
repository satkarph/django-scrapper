from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView
# from .utils import scraper_spectra
from rest_framework.response import Response
from .tasks import go_to_sleep,sairtex,webmotors,autoparts,carter,opticat,standard,bwd
import io
import csv
import pandas as pd
import openpyxl

# Create your views here.
class Userdetail(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        uuid = self.request.query_params.get('id', None)

        file = request.FILES['file']
        wb = openpyxl.load_workbook(file)
        worksheet = wb["Sheet1"]

        data = []
        for row in worksheet.iter_rows():
            for cell in row:
                data.append(str(cell.value))


        # a= file.read()
        # print(a)
        # print(type(a))
        # decoded_file = file.read().decode()
        # io_string = io.StringIO(decoded_file)
        # reader = csv.reader(io_string)

        # go_to_sleep.delay(uuid=["16147161387"])

        task = go_to_sleep.delay(data)
        print(task)
        # a = scraper_spectra(uuid)
        content={"task_id":str(task)}
        return Response("hello")

class Airtex(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        uuid = self.request.query_params.get('id', None)

        file = request.FILES['file']
        wb = openpyxl.load_workbook(file)
        worksheet = wb["Sheet1"]

        data = []
        for row in worksheet.iter_rows():
            for cell in row:
                data.append(str(cell.value))

        # go_to_sleep.delay(uuid=["16147161387"])

        task = sairtex.delay(data)
        print(task)
        # a = scraper_spectra(uuid)
        content={"task_id":str(task)}
        return Response(content)


class Mootors(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        uuid = self.request.query_params.get('id', None)

        file = request.FILES['file']
        wb = openpyxl.load_workbook(file)
        worksheet = wb["Sheet1"]

        data = []
        for row in worksheet.iter_rows():
            for cell in row:
                data.append(str(cell.value))

        # go_to_sleep.delay(uuid=["16147161387"])

        task = webmotors.delay(data)
        print(task)
        # a = scraper_spectra(uuid)
        content={"task_id":str(task)}
        return Response(content)


class Autoparts(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        uuid = self.request.query_params.get('id', None)

        file = request.FILES['file']
        wb = openpyxl.load_workbook(file)
        worksheet = wb["Sheet1"]

        data = []
        for row in worksheet.iter_rows():
            for cell in row:
                data.append(str(cell.value))

        # go_to_sleep.delay(uuid=["16147161387"])

        task = autoparts.delay(data)
        print(task)
        # a = scraper_spectra(uuid)
        content={"task_id":str(task)}
        return Response(content)


class Carter(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        uuid = self.request.query_params.get('id', None)
        file = request.FILES['file']
        wb = openpyxl.load_workbook(file)
        worksheet = wb["Sheet1"]

        data = []
        for row in worksheet.iter_rows():
            for cell in row:
                data.append(str(cell.value))

        # go_to_sleep.delay(uuid=["16147161387"])

        task = carter.delay(data)
        print(task)
        # a = scraper_spectra(uuid)
        content={"task_id":str(task)}
        return Response(content)

class Opticat(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        uuid = self.request.query_params.get('id', None)

        file = request.FILES['file']
        wb = openpyxl.load_workbook(file)
        worksheet = wb["Sheet1"]

        data = []
        for row in worksheet.iter_rows():
            for cell in row:
                data.append(str(cell.value))

        task = opticat.delay(data)
        print(task)
        # a = scraper_spectra(uuid)
        content={"task_id":str(task)}
        return Response(content)

class Standard(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        uuid = self.request.query_params.get('id', None)

        file = request.FILES['file']
        wb = openpyxl.load_workbook(file)
        worksheet = wb["Sheet1"]

        data = []
        for row in worksheet.iter_rows():
            for cell in row:
                data.append(str(cell.value))

        # go_to_sleep.delay(uuid=["16147161387"])

        task = standard.delay(data)
        print(task)
        # a = scraper_spectra(uuid)
        content={"task_id":str(task)}
        return Response(content)

class BWD(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        uuid = self.request.query_params.get('id', None)

        file = request.FILES['file']
        wb = openpyxl.load_workbook(file)
        worksheet = wb["Sheet1"]

        data = []
        for row in worksheet.iter_rows():
            for cell in row:
                data.append(str(cell.value))

        # go_to_sleep.delay(uuid=["16147161387"])

        task = bwd.delay(data)
        print(task)
        # a = scraper_spectra(uuid)
        content={"task_id":str(task)}
        return Response(content)
