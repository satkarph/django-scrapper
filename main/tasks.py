from celery import shared_task
from celery_progress.backend import ProgressRecorder
from .utils import scraper_spectra
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




@shared_task(bind=True)
def go_to_sleep(self, duration):
    progress_recorder = ProgressRecorder(self)
    total=len(duration)
    for i,row in enumerate(duration):
        scraper_spectra(row[0])
        progress_recorder.set_progress(i, total, row[0])
    return 'Done'