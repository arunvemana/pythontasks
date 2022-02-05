from django.db import models


# Create your models here.

class StoreException(models.Model):
    """
    :param int error_code\n
    :param str error_type\n
    :param str error_traceback\n
    """
    error_code = models.IntegerField()
    error_type = models.CharField(max_length=100)
    error_traceback = models.CharField(max_length=300)
