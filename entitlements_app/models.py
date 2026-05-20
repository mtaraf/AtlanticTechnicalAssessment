from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Product(models.TextChoices):
    DIGITAL = "DIGITAL", "Digital"
    PRINT = "PRINT", "Print"
    PREMIUM = "PREMIUM", "Premium"

class Entitlement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="entitlements")
    product = models.CharField(max_length=20, choices=Product.choices)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True, blank=True)
    revoked = models.BooleanField(default=False)

    class Meta:
        ordering = ['-start_date']

    def is_active(self):
        now = timezone.now()
        if self.revoked:
            return False
        if self.end_date and self.end_date < now:
            return False
        return True

    def entitlements(self):
        if self.product == Product.DIGITAL:
            return ["website_content"]
        elif self.product == Product.PRINT:
            return ["website_content", "print_magazine"]
        elif self.product == Product.PREMIUM:
            return ["website_content", "print_magazine", "no_ads"]
        return []