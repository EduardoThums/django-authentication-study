from django.conf import settings
from django.db import models


class Trainer(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='trainer',
        null=False,
        primary_key=True
    )

    gender = models.CharField(default='male', null=False, max_length=6)

    class Meta:
        db_table = 'trainer'
