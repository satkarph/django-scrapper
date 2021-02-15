from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView
# from .utils import scraper_spectra
from rest_framework.response import Response
from .tasks import go_to_sleep,sairtex,webmotors,autoparts,carter,opticat,standard,bwd
import io
import csv

# Create your views here.
class Userdetail(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        uuid = self.request.query_params.get('id', None)

        file = request.FILES['file']
        decoded_file = file.read().decode()
        io_string = io.StringIO(decoded_file)
        reader = csv.reader(io_string)

        # go_to_sleep.delay(uuid=["16147161387"])

        task = go_to_sleep.delay(list(reader))
        print(task)
        # a = scraper_spectra(uuid)
        content={"task_id":str(task)}
        return Response(content)

class Airtex(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        uuid = self.request.query_params.get('id', None)

        file = request.FILES['file']
        decoded_file = file.read().decode()
        io_string = io.StringIO(decoded_file)
        reader = csv.reader(io_string)

        # go_to_sleep.delay(uuid=["16147161387"])

        task = sairtex.delay(list(reader))
        print(task)
        # a = scraper_spectra(uuid)
        content={"task_id":str(task)}
        return Response(content)


class Mootors(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        uuid = self.request.query_params.get('id', None)

        file = request.FILES['file']
        decoded_file = file.read().decode()
        io_string = io.StringIO(decoded_file)
        reader = csv.reader(io_string)

        # go_to_sleep.delay(uuid=["16147161387"])

        task = webmotors.delay(list(reader))
        print(task)
        # a = scraper_spectra(uuid)
        content={"task_id":str(task)}
        return Response(content)


class Autoparts(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        uuid = self.request.query_params.get('id', None)

        file = request.FILES['file']
        decoded_file = file.read().decode()
        io_string = io.StringIO(decoded_file)
        reader = csv.reader(io_string)

        # go_to_sleep.delay(uuid=["16147161387"])

        task = autoparts.delay(list(reader))
        print(task)
        # a = scraper_spectra(uuid)
        content={"task_id":str(task)}
        return Response(content)


class Carter(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        uuid = self.request.query_params.get('id', None)

        file = request.FILES['file']
        decoded_file = file.read().decode()
        io_string = io.StringIO(decoded_file)
        reader = csv.reader(io_string)

        # go_to_sleep.delay(uuid=["16147161387"])

        task = carter.delay(list(reader))
        print(task)
        # a = scraper_spectra(uuid)
        content={"task_id":str(task)}
        return Response(content)

class Opticat(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        uuid = self.request.query_params.get('id', None)

        file = request.FILES['file']
        decoded_file = file.read().decode()
        io_string = io.StringIO(decoded_file)
        reader = csv.reader(io_string)

        # go_to_sleep.delay(uuid=["16147161387"])

        task = opticat.delay(list(reader))
        print(task)
        # a = scraper_spectra(uuid)
        content={"task_id":str(task)}
        return Response(content)

class Standard(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        uuid = self.request.query_params.get('id', None)

        file = request.FILES['file']
        decoded_file = file.read().decode()
        io_string = io.StringIO(decoded_file)
        reader = csv.reader(io_string)

        # go_to_sleep.delay(uuid=["16147161387"])

        task = standard.delay(list(reader))
        print(task)
        # a = scraper_spectra(uuid)
        content={"task_id":str(task)}
        return Response(content)

class BWD(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        uuid = self.request.query_params.get('id', None)

        file = request.FILES['file']
        decoded_file = file.read().decode()
        io_string = io.StringIO(decoded_file)
        reader = csv.reader(io_string)

        # go_to_sleep.delay(uuid=["16147161387"])

        task = bwd.delay(list(reader))
        print(task)
        # a = scraper_spectra(uuid)
        content={"task_id":str(task)}
        return Response(content)
