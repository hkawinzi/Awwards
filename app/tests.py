from django.test import TestCase
from .models import Project, Profile, Rate
# Create your tests here.


# Create your tests here.
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.awwwards = Profile( )

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.awwwards, Profile))


class ProjectTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.awwwards = Project()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.awwwards, Project))

    # Testing Save Method
    def test_save_method(self):
        self.awwwards.save_image()
        description = Project.objects.all()
        self.assertTrue(len(description) > 0)
