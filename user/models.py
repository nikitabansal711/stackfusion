from django.db import models
from phone_field import PhoneField


class Profile(models.Model):
    name = models.CharField(max_length=200, null=True)
    mobile = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(max_length=200, null=True)
    date_of_birth = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
