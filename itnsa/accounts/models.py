from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission
from django.utils.translation import gettext_lazy as _


# Create your models here.

class User(AbstractUser):
    real_name = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    is_student = models.BooleanField(default=False)
    is_coach = models.BooleanField(default=False)
    is_competitor = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        _("staff status"),
        default=True,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    class Meta(AbstractUser.Meta):
        pass

    def __str__(self):
        if self.real_name:
            return self.real_name
        return self.username

