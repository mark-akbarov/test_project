from django.db import models


class VerifyUser(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    code = models.CharField(max_length=25)
    is_active = models.BooleanField(default=False)
