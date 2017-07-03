from django.core.management.base import BaseCommand, CommandError
from core.models import Verification

class Command(BaseCommand):
    help = 'Counting all fake assets'

    def add_arguments(self, parser):
        parser.add_argument('status', nargs='+', type=int)

    def handle(self, *args, **options):
        status = options['status']
        print "filter by status ",status
        vobjs=Verification.objects.values('asset_code').distinct()
        print len(vobjs)
