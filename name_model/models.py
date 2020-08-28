from django.db import models


# Create your models here.
class myprofile(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    e_mail = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='pictures')


#    def __str__(self):
 #       return self.title()