from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView
# from .utils import scraper_spectra
from rest_framework.response import Response
from .tasks import go_to_sleep
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
        return Response("sd")
