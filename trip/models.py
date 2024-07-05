from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Navbar(models.Model):
    title = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=13)
    telegram = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Header(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Amenity(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    durability = models.CharField(max_length=25)
    eat = models.CharField(max_length=25)
    visa = models.BooleanField()
    help = models.CharField(max_length=10)
    pioneer = models.CharField(max_length=50)
    water = models.CharField(max_length=25)
    clothes = models.CharField(max_length=25)
    weapons = models.CharField(max_length=50)

    def __str__(self):
        return self.company



class About(models.Model):
    image = models.ImageField(upload_to='media')
    text = models.TextField()

    def __str__(self):
        return self.image


class Social(models.Model):
    instagram = models.CharField(max_length=20)
    telegram = models.CharField(max_length=20)
    you_tube = models.CharField(max_length=20)
    facebook = models.CharField(max_length=20)
    tok_tok = models.CharField(max_length=20)

    def __str__(self):
        return self.telegram




class Comment(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    star = models.PositiveIntegerField()
    description = models.TextField()


    def __str__(self):
        return self.first_name
