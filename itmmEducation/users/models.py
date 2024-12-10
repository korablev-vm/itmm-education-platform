from django.db import models
from django.conf import settings

class Token(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='token')
    amount = models.IntegerField(default=0)  # Количество токенов

    def add_tokens(self, amount):
        self.amount += amount
        self.save()

    def subtract_tokens(self, amount):
        if self.amount >= amount:
            self.amount -= amount
            self.save()
            return True
        return False
