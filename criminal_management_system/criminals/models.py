from django.db import models

# Create your models here.

class Criminal(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    aadhaar_number = models.CharField(max_length=12, unique=True)
    crime_description = models.TextField()
    date_of_crime = models.DateField()
    arrest_date = models.DateField()
    photo = models.ImageField(upload_to='criminals/')

    def __str__(self):
        return self.name