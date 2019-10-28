from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


# Create your models here
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='picture/', blank=True)
    bio = models.TextField(default='')
    posted_project = models.ForeignKey('Project', on_delete=models.CASCADE, null=True)
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
    image = models.ImageField(upload_to='image/', blank=True)

    def __str__(self):
        return self.title

    def save_title(self):
        self.save()

    def delete_title(self, title):
        self.title = title
        self.save()

    @classmethod
    def fetch_all_images(cls):
        all_images = Project.objects.all()
        return all_images

    @classmethod
    def search_project_by_title(cls, search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project


class Comment(models.Model):
    comment = models.TextField(max_length=300)

    def __str__(self):
        return self.comment()

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()


class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Project, on_delete=models.PROTECT, related_name='likes', null=True)
    design = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    usability = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], null=True)
    creativity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    content = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    def save_rate(self):
        self.save()

    def delete_rate(self):
        self.delete()
