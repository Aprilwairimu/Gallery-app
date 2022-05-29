from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

 # def save_photo(self):
    #     self.save()
    
    # def delete_photo(self):
    #     self.save()

    # def update_photo(self):
    #     self.save()

class Location(models.Model):
    location = models.CharField(max_length=100,null=False, blank=False)

 # def save_photo(self):
    #     self.save()
    
    # def delete_photo(self):
    #     self.save()

    # def update_photo(self):
    #     self.save()

class Photo(models.Model):
    image = models.ImageField (null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=300)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    # def save_photo(self):
    #     self.save()
    
    # def delete_photo(self):
    #     self.save()

    # def update_photo(self):
    #     self.save()

    # def get_photo_by_id(id):
    #     self.save()

    # def search_photo(Category):
    #     self.save()

    # def filter_by_location(location):
    #     self.save()

    # @classmethod
    # def search_by_name(cls,search_term):
    #     gallery = cls.objects.filter(name__icontains=search_term)
    #     return gallery