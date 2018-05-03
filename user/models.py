#!/usr/bin/env python
''' 用户模块 '''
import os
import uuid
from django.conf import settings
from collections import OrderedDict
from django.db import models
from django.shortcuts import reverse
from django.core import signing
from django.contrib.auth.models import  AbstractUser
from django.contrib.auth.hashers import make_password
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
#from common.utils import date_expired_default, signer
#from simple_history.models import HistoricalRecords
#from .group import UserGroup

class Users(AbstractUser):
    USER_ROLE_CHOICES = (
        ('SU', 'SuperUser'),
        ('GA', 'GroupAdmin'),
        ('CU', 'CommonUser'),
    )
    name = models.CharField(max_length=80)
    uuid = models.CharField(max_length=100)
    role = models.CharField(max_length=2, choices=USER_ROLE_CHOICES, default='CU')
    ssh_key_pwd = models.CharField(max_length=200)

    def __unicode__(self):
        return self.username


