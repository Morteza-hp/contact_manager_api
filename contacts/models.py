from django.db import models
from django.utils.translation import gettext as _

class Contact(models.Model):
    first_name = models.CharField(verbose_name=_('Name'),max_length=20)
    last_name = models.CharField(verbose_name=_('Last name'),max_length=30)
    age = models.PositiveSmallIntegerField(verbose_name=_('Age'),null=True,blank=True)
    email = models.EmailField(verbose_name=_('Email'),null=True,blank=True)
    picture = models.ImageField(verbose_name=_('Picture'),null=True,blank=True)
    phone_number = models.CharField(verbose_name=_('Phone number'),max_length=15)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
