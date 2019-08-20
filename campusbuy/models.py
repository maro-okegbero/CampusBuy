from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField
import PIL.Image as Image



# Create your models here.

class Category(models.Model):

    Name = models.CharField(max_length=30, null=True, blank=True)
    Details = models.CharField(max_length=100, default="Default")
    # Special Cloudinary image Field
    Category_Logo = CloudinaryField('Category_Logo')

    def __str__(self):
        return self.Name

class Advert(models.Model):
    HALL4 = 'HALL4'
    HALL3 = 'HALL3'
    HALL2 = 'HALL2'
    HALL1 = 'HALL1'
    MAIN_GATE = 'MAIN_GATE'
    GREEN_PARK = 'GREEN_PARK'
    GTBANK = 'GTBANK'
    NAAS_GARDEN = 'NAAS_GARDEN'
    PHYSICAL_SCIENCE_COMPLEX = 'PHYSICAL_SCIENCE_COM'
    MEDICAL_SCIENCE_COMPLEX = 'MED_COM'
    BASEMENT = 'BASEMENT'
    JUNE12 = 'JUNE12'
    ENGINEERING = 'ENGINEERING_PARK'





    Location_Choices = (
        (HALL4, 'Hall4'),
        (HALL3, 'Hall3'),
        (HALL2, 'Hall2'),
        (HALL1, 'Hall1'),
        (MAIN_GATE, 'Main gate'),
        (GREEN_PARK, 'Green Park'),
        (GTBANK, 'GTBank Wifi Spot'),
        (NAAS_GARDEN, 'Naas Garden'),
        (PHYSICAL_SCIENCE_COMPLEX, 'Physical Science Complex'),
        (MEDICAL_SCIENCE_COMPLEX, 'Medical Science Complex'),
        (BASEMENT,'Basement'),
        (JUNE12, 'June12'),
        (ENGINEERING, 'Engineering Park')



    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Seller_Name = models.CharField(max_length=50, blank=False, null=False)
    Phone_Number = models.CharField(max_length= 12, blank=False, null=False)
    # Special Cloudinary image Field
    image = CloudinaryField('image')

    Item = models.CharField(max_length=70, blank=False, null=False)
    Location = models.CharField(max_length=70,choices=Location_Choices, default=HALL3, blank=False,  help_text='<p style="color: red; font: italic 12px tahoma;">**Choose a location where you can easily meet up with potential buyers</p>')
    Description = models.TextField(max_length=250, blank=False, null=False)
    Asking_Price = models.IntegerField(blank=False, null=False)
    published_date = models.DateTimeField(blank=False, default=timezone.now)

    def __unicode__(self):
        try:
            public_id = self.image.public_id
        except AttributeError:
            public_id = ''
        return "Photo <%s:%s>" % (self.title, public_id)

    def published(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Seller_Name + '- ' + self.Item + '- ' + self.Location + '- ' + self.Phone_Number





    class Meta:
        ordering = ['-published_date']
