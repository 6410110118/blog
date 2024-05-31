from django.db import models

# Create your models here.


class Product(models.Model):

    name = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    description = models.TextField()
    imag = models.ImageField( upload_to= 'products/')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self) :
        return self.name
    
    def edit(self, name ,author, description , imag):
        self.name = name
        self.author = author
        self.description = description
        self.imag = imag
        self.save()


    def short_description(self):

        words = self.description.split()

        if len(words) > 50:
            return ' '.join(words[:30]) + '...'
        else:
            return self.description
        
