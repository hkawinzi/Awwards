from django.db import models
from django.contrib.auth.models import User


# Create your models here
class Profile(models.model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='picture/', blank=True)
    bio = models.TextField(default='')
    posted_project = models.ForeignKey('Project', on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=300, blank=True)
