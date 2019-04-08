from django.core.management.base import BaseCommand, CommandError
from campusbuy.models import Category, Advert
from datetime import datetime, timedelta
from django.utils import timezone

class Command(BaseCommand):
    help = 'Delete Ads that are more than 30 days old'

    def handle(self, *args, **options):
        Advert.objects.filter(published_date__lte= timezone.now() + timedelta(days=30)).delete()
        self.stdout.write(self.style.SUCCESS('Deleted Ads older than 30 days'))
