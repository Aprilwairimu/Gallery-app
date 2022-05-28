from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name



class Photo(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.save()

    def update_image(self):
        self.save()

    def get_image_by_id(id):
        self.save()

    def search_image(Category):
        self.save()

    def filter_by_location(location):
        self.save()