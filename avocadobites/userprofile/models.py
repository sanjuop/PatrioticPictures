from django.db import models
from django.contrib.auth.models import User

def user_image_path(instance, filename):
    # image file will be uploaded to MEDIA_ROOT/<username>/<filename>
    return '{0}/{1}'.format(instance.employee_code, filename)

# Create your models here.
class profile(models.Model):

    MARITAL_STATUS_CHOICES = (
        (1, 'Single'),
        (2, 'Married'),
        (3, 'Widowed'),
        (4, 'Divorced'),
        (5, 'Engaged')
    )

    GENDER_CHOICES = (
        (1, 'MALE'),
        (2, 'FEMALE'),
        (3, 'OTHER')

    )

    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_image_path, blank=True)
    employee_code = models.CharField(max_length=20, unique=True)
    middle_name = models.CharField(max_length=200)
    department = models.ForeignKey
    designation = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    birth_place = models.CharField(max_length=200)
    current_location = models.CharField(max_length=20)
    date_of_joining = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=10)
    alternate_email_id = models.EmailField(blank = True, null=True, max_length=50)
    permanent_address = models.TextField(null=True, blank = True)
    current_address = models.TextField(null=True, blank = True)
    personal_phone_number = models.CharField(max_length=50)
    altername_phone_number = models.CharField(max_length=50)
    pan_number = models.CharField(max_length=50)
    passpart_number = models.CharField(max_length=50)
    father_name = models.CharField(max_length=300)
    mother_name = models.CharField(max_length=300)
    marital_status = models.CharField(max_length=300, choices=MARITAL_STATUS_CHOICES)
    spouse_name = models.CharField(max_length=300)
    emergency_contact_number_1 = models.CharField(max_length=40)
    emergency_contact_number_2 = models.CharField(max_length=40)




