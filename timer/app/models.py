from datetime import timedelta

from django.db import models

# Create your models here.
class Timer(models.Model):
    duration = models.IntegerField(max_length=10, verbose_name="Timer Duration")
    is_completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    started = models.DateTimeField(blank=True, null=True)

    @property
    def end_time(self):
        return self.created + timedelta(minutes=int(self.duration))

    @property
    def remaining_time(self):
        return self.end_time - self.created