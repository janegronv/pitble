from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
class User(AbstractUser):

    followings = models.ManyToManyField('User', verbose_name=_('Followings'))

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

@python_2_unicode_compatible
class Pitble(models.Model):
    text = models.TextField(verbose_name=_('Text'))
    owner = models.ForeignKey(User, verbose_name=_('Owner'))
    def __str__(self):
        return self.text