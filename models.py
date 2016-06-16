#import datetime
from django.db                              import models
from django.utils                           import timezone

class StSt(models.Model):
  advert                  = models.TextField          (blank=True, null=True)
  contact_info         = models.CharField          (max_length=200, blank=True, null=True)
  created_date            = models.DateTimeField      (blank=True, null=True, default=timezone.now)
  published_date          = models.DateTimeField      (blank=True, null=True)
  def publish(self):
    self.published_date = timezone.now()
    self.save()
  def __str__(self):
    return str(self.contact_info)