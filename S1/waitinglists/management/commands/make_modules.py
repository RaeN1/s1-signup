from django.core.management.base import BaseCommand

from waitinglists.models import Module


class Command(BaseCommand):
    help = "Initial setup to create modules"

    def handle(self, *args, **kwargs):
        for name in ("Module 1", "Module 3", "Module 4", "Module 5"):
            Module.objects.get_or_create(name=name)