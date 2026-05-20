from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from entitlements_app.models import Entitlement, Product
from django.utils import timezone
from datetime import timedelta


class Command(BaseCommand):
    help = "Seeds demo entitlement data"

    def handle(self, *args, **kwargs):

        users = [
            ("digital", Product.DIGITAL),
            ("print", Product.PRINT),
            ("premium", Product.PREMIUM),
        ]

        for username, product in users:

            user, created = User.objects.get_or_create(
                username=username
            )

            if created:
                user.set_password("password")
                user.save()

            Entitlement.objects.create(
                user=user,
                product=product,
                end_date=timezone.now() + timedelta(days=30)
            )

        self.stdout.write(
            self.style.SUCCESS("Seed data created successfully.")
        )