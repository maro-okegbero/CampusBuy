from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField
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
    HALL4 = 'H4'
    HALL3 = 'H3'
    HALL2 = 'H2'
    HALL1 = 'H1'
    MAIN_GATE = 'MG'
    GREEN_PARK = 'GP'
    GTBANK = 'GTBWS'
    NAAS_GARDEN = 'NAASG'
    PHYSICAL_SCIENCE_COMPLEX = 'PSC'
    MEDICAL_SCIENCE_COMPLEX = 'MSC'
    ORCHARD = 'ORC'
    JUNE12 = 'J12'




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
        (ORCHARD,'Orchard'),
        (JUNE12, 'June12')


    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Seller_Name = models.CharField(max_length=50, blank=False, null=False)
    Phone_Number = models.IntegerField(blank=False, null=False,
                                    help_text='<p style="color: red; font: italic 12px tahoma;">**Please input a working Phone Number that you can be contacted with on the fly</p>')
    image = CloudinaryField('image')#  Cloudinary image Field
    Item = models.CharField(max_length=20, blank=False, null=False)
    Location = models.CharField(max_length=10, choices=Location_Choices, default=HALL3, blank=False,  help_text='<p style="color: red; font: italic 12px tahoma;">**Choose a location where you can easily meet up with potential buyers</p>')
    Description = models.TextField(max_length=250, blank=False, null=False)
    Asking_Price = models.IntegerFieldField(blank=False, null=False)
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
