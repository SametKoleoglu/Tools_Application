from django.db import models

# Create your models here.

class Ping(models.Model):
    protocol_choices = [
        ('https', 'https'),
        ('ping', 'ICMP'),
        ('host', 'Port'),
    ]
    protocol = models.CharField(max_length=15, choices=protocol_choices)
    url = models.TextField()
    status = models.CharField(max_length=100, blank=True)
    response_time = models.FloatField(blank=True, null=True)
    response_code = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.url
