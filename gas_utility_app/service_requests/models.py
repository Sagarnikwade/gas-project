from django.db import models
from django.conf import settings

class ServiceRequest(models.Model):
    SERVICE_TYPES = [
        ('installation', 'Installation'),
        ('maintenance', 'Maintenance'),
        ('complaint', 'Complaint'),
    ]

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.service_type} - {self.customer.username}"
