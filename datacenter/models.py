from django.db import models
import datetime
import pytz
import django


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def is_visit_long(self, minutes=60):
        duration = self.leaved_at - self.entered_at
        return duration.total_seconds() > 3600

    def get_duration(self):
        current_time = django.utils.timezone.localtime()
        curent_time_formatted = datetime.datetime(current_time.year,
                                                  current_time.month,
                                                  current_time.day,
                                                  current_time.hour,
                                                  current_time.minute,
                                                  current_time.second,
                                                  tzinfo=pytz.UTC)
        duration = curent_time_formatted - self.created_at
        return duration
