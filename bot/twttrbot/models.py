from django.db import models
from django.db.models import fields
from django.db.models.base import Model

# Create your models here.
class TweetLookUpWord(models.Model):
    keyword = models.CharField(max_length=255)

class TweetLookUpBadWord(models.Model):
    keyword = models.CharField(max_length=255)

class TweetLookUpCoordinates(models.Model):
    value = models.TextField()

class OutboundDirectMessage(models.Model):
    message = models.TextField()

class LastFollower(models.Model):
    last_follower_id = models.PositiveBigIntegerField()

class InboundDirectMessage(models.Model):
    sender = models.CharField(max_length=255)
    message = models.TextField()
    sent_on = models.DateTimeField()
