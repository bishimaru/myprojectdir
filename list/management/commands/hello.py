from django.core.management.base import BaseCommand, CommandError
from ... models import SlotData
from django.utils import timezone


class Command(BaseCommand):
    def handle(self, *args, **options):
        d = SlotData(
            store_name='cron',
            name='cron',
            number=1,
            # date=timezone.now,
            bigbonus=1,
            regularbonus=1,
            count=1,
            bbchance='1',
            rbchance='1',
            totalchance='1',
            lastgames=1,
            payout=1,

        )
        d.save()
