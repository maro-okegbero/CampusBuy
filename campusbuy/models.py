from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField
import PIL.Image as Image



# Create your models here.

class Category(models.Model):

    Name = models.CharField(max_length=30, null=True, blank=True)
    Details = models.CharField(max_length=100, default="Default")
    Category_Logo = CloudinaryField('Category_Logo')

    def __str__(self):
        return self.Name

class Advert(models.Model):
    HALL3 = 'HALL3'
    HALL4 = 'HALL4'
    HALL2 = 'HALL2'
    MAIN_GATE = 'MAINGATE'
    HALL1 = 'HALL1'

    Location_Choices = (
        (HALL3, 'Hall3'),
        (HALL4, 'Hall4'),
        (HALL2, 'Hall2'),
        (MAIN_GATE, 'Main_gate'),
        (HALL1, 'Hall1')
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Seller_Name = models.CharField(max_length=50, blank=False, null=False)
    Phone_Number = models.CharField(max_length=11, blank=False, null=False,
                                    help_text='<p style="color: red; font: italic 12px tahoma;">**Please input a working Phone Number that you can be contacted with on the fly</p>')
    image = CloudinaryField('image')
    Item = models.CharField(max_length=20, blank=False, null=False)
    Location = models.CharField(max_length=10, choices=Location_Choices, default=HALL3, blank=False)
    Description = models.TextField(max_length=250, blank=False, null=False)
    Asking_Price = models.CharField(max_length=20, blank=False, null=False)
    published_date = models.DateTimeField(blank=False, default=timezone.now)

    def published(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Seller_Name + '- ' + self.Item + '- ' + self.Location + '- ' + self.Phone_Number


    class Meta:
        ordering = ['-published_date']
