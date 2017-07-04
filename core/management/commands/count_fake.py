import os
import datetime
from django.core.management.base import BaseCommand, CommandError
from core.models import Verification
from core.models import STATUS_CHOICES

CURRENT_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = CURRENT_PATH.split('core')[0]

class Command(BaseCommand):
    help = 'Counting all fake assets'

    def add_arguments(self, parser):
        parser.add_argument('status', nargs='+', type=int)

    def handle(self, *args, **options):
        status = options['status']
        vobjs=Verification.objects.filter(status=status[0])
        fakes=vobjs.values('asset_code').distinct()
        f=open(BASE_DIR+'media/analytics/counter.txt','w+')
        current_time=datetime.datetime.now()
        f.write("Total "+str(len(fakes))+" assets found "+str(STATUS_CHOICES[status[0]-1][1])+" ----- "+str(current_time))
        f.close()
