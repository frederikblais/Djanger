from django.contrib import admin

# Register your models here.
from .models import TweetLookUpWord, TweetLookUpBadWord, OutboundDirectMessage, TweetLookUpCoordinates

admin.site.register(TweetLookUpWord)
admin.site.register(TweetLookUpBadWord)
admin.site.register(OutboundDirectMessage)
admin.site.register(TweetLookUpCoordinates)

