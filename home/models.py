# DARYO UZ sayti modeli

from django.db import models

# class Post(models.Model):
#     DAYS_OF_WEAK = (
#         'du',
#         'se',
#         'chor',
#         'pay',
#         'juma',
#         'shanba',
#         'yak',
#     )
#     EXCHANGE_CHOICE = (
#         'bull',
#         'bear',
#         'neutral'
#     )

#     title = models.CharField(max_length=256)
#     description = models.CharField(max_length=256)
#     post_body = models.TextField()
#     type_of_post = models.ForeignKey(TYPES, on_delete=models.CASCADE)

#     image = models.ImageField(upload_to='images/')
#     video = models.FileField(upload_to='videos/')
    
#     topic_is_about = models.ManyToManyField("self") # mavzuga doir postlar

#     views_count = models.IntegerField(default=0)

#     created_at = models.DateTimeField(auto_now_add=True)

# class Weather(models.Model):
#     date = models.DateTimeField(auto_now_add=True)
#     day_of_weak = models.ForeignKey(DAYS_OF_WEAK, on_delete=models.CASCADE) # hafta kuni
#     city = models.CharField(max_length=20) # model

#     temperature = models.CharField(max_length=5)

# class ExchangeRate(models.Model):
#     name = models.CharField(max_length=5)
#     amount = models.FloatField(default=0)
#     raised_or_fell = models.CharField(max_length=EXCHANGE_CHOICE) # kotarilgan yoki tushgani

# KUN UZ sayti modeli

class Types(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Locations(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Post(models.Model):
    LANGUAGE_CHOICE = (
        ('uz_latin','uz_latin'),
        ('uz_kirill', 'uz_kirill'),
        ('rus', 'rus'),
        ('eng', 'eng'),
    )
    
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    post_body = models.TextField()
    type_of_post = models.ForeignKey(Types, on_delete=models.CASCADE)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICE, default='uz_latin')

    regions = models.ForeignKey(Locations, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    is_advertising = models.BooleanField(default=False)

    views_count = models.IntegerField(default=0)

    image = models.ImageField(upload_to='images/')
    author_image = models.CharField(max_length=50)
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title

