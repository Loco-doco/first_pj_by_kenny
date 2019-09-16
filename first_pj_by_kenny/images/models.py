from django.db import models
from first_pj_by_kenny.users import models as user_models

# Create your models here.

class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Image(TimeStampedModel):
    """Image Models"""

    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, models.PROTECT, null=True)

class Comment(TimeStampedModel):
    """Comment Models"""

    message = models.TextField()
    creator = models.ForeignKey(user_models.User, models.PROTECT, null=True)
    image = models.ForeignKey(Image, models.PROTECT, null=True)

class Like(TimeStampedModel):
    """Like Models"""

    creator = models.ForeignKey(user_models.User, models.PROTECT, null=True)
    image = models.ForeignKey(Image, models.PROTECT, null=True)