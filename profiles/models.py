from django.db import models
# from datetime import date

from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

from django.utils.translation import gettext_lazy as _

from django.contrib.auth.validators import UnicodeUsernameValidator


# Create your models here.

class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=40,
        unique=True,
        help_text=_('Required. 40 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = None
    last_name = None
    email = models.EmailField(_('email address'), unique=True)
    full_name = models.CharField(_('full name'), max_length=255, blank=True)
    phone_number = models.CharField(_('phone number'), max_length=15, blank=True)
    address = models.CharField(_('address'), max_length=255, blank=True)
    about = models.CharField(_('about'), max_length=500, blank=True)

    dob = models.DateField(_('date of birth'), blank=True, null=True) # Date Of Birth
    avatar = models.URLField(_('avatar'), blank=True, max_length=1000)

    # def calculate_age(self):
    #     today = date.today()

    #     try:
    #         birthday = self.dob.replace(year=today.year)
    #     # raised when birth date is February 29 and the current year is not a leap year
    #     except ValueError:
    #         birthday = self.dob.replace(year=today.year, day=born.day-1)

    #     if birthday > today:
    #         return today.year - born.year - 1
    #     else:
    #         return today.year - born.year

    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Nam'), (GENDER_FEMALE, 'Nữ')]
    gender = models.IntegerField(_('gender'), blank=True, null=True, choices=GENDER_CHOICES)

    def __str__(self):
        return self.username





