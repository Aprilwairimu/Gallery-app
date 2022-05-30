from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

    def save_category(self):
            self.save()
        
    def delete_category(self):
            self.delete()

    def update_category(self):
            self.update()

class Location(models.Model):
    location = models.CharField(max_length=100,null=False, blank=False)

    def save_location(self):
            self.save()
        
    def delete_location(self):
            self.delete()

    def update_location(self):
            self.update()

class Photo(models.Model):
    image = models.ImageField (null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=300)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    def save_photo(self):
        self.save()
    
    def delete_photo(self):
        self.delete()

    def update_photo(self):
        self.update()

    # def get_photo_by_id(id):
    #     self.save()

    # def search_photo(Category):
    #     self.save()

    # def filter_by_location(location):
    #     self.save()

    @classmethod
    def search_by_category(cls,search_term):
        gallery = cls.objects.filter(category__icontains=search_term)
        return gallery