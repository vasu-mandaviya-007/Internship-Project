from django.db import models
import uuid

class Base(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
