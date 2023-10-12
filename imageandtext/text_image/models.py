from django.db import models

# Create your models here.
choise_field = (
    ('Sahih', 'Sahih'),
    ('Zaif', 'Zaif'),
    ('Hasan', 'Hasan'),
)

class hadithsModel(models.Model):
    chapter_name = models.CharField(max_length=100)
    hadith_number = models.IntegerField()
    text = models.TextField()
    hadith_status = models.CharField(max_length=5, choices=choise_field)


    def __str__(self):
        return f'{self.hadith_number} {self.hadith_status}'
    




class tatorial(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title