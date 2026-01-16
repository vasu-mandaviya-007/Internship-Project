from django.db import models
from base.models import Base
import uuid

class Categories(Base):
    cname = models.CharField(max_length=200)
    parentname = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.cname