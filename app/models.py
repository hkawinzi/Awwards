from django.db import models
from django.contrib.auth.models import User


# Create your models here
class Profile(models.model):
    user = models.OneToOneField(User)
    image = models.ImageField(upload_to='picture/', blank=True)
    bio = models.TextField(default='')
    posted_project = models.ForeignKey('Project', on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_bio(self, bio):
        self.bio = bio
        self.save()

class Project(models.Model):
    title = models.CharField(max_length=300)
    details = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save_title(self):
        self.save()

    def delete_title(self, title):
        self.title = title
        self.save()
