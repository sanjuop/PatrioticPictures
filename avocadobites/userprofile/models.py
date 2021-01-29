from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Department(models.Model):
    department = models.CharField(max_length=200)
    short_name = models.CharField(max_length=20, null=True, blank=True)
    department_type = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.department

def user_image_path(instance, filename):
    # image file will be uploaded to MEDIA_ROOT/<username>/<filename>
    return '{0}/{1}'.format(instance.employee_code, filename)

# Create your models here.
class Profile(models.Model):

    MARITAL_STATUS_CHOICES = (
        ("1", 'Single'),
        ("2", 'Married'),
        ("3", 'Widowed'),
        ("4", 'Divorced'),
        ("5", 'Engaged')
    )

    GENDER_CHOICES = (
        ("1", 'MALE'),
        ("2", 'FEMALE'),
        ("3", 'OTHER')

    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_image_path, null=True, blank=True,)
    employee_code = models.CharField(max_length=20, unique=True)
    middle_name = models.CharField(max_length=200, null=True, blank=True,)
    department = models.ForeignKey(Department, default=1, verbose_name='emp_department', on_delete=models.SET_DEFAULT)
    designation = models.CharField(max_length=50)
    skill_level = models.CharField(max_length=10)
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
    alternate_phone_number = models.CharField(max_length=50, null=True, blank=True,)
    nationality = models.CharField(max_length=50, default="Indian")
    state = models.CharField(max_length=50, default="Karnataka")
    pan_number = models.CharField(max_length=50, null=True, blank=True,)
    passport_number = models.CharField(max_length=50, null=True, blank=True,)
    father_name = models.CharField(max_length=300, null=True, blank=True,)
    mother_name = models.CharField(max_length=300, null=True, blank=True,)
    marital_status = models.CharField(max_length=300, choices=MARITAL_STATUS_CHOICES, null=True, blank=True,)
    spouse_name = models.CharField(max_length=300, null=True, blank=True,)
    emergency_contact_number_1 = models.CharField(max_length=40, null=True, blank=True,)
    emergency_contact_number_2 = models.CharField(max_length=40, null=True, blank=True,)
    project_assigned = models.CharField(max_length=40, null=True, blank=True,)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def get_full_name(self):
        return self.user.first_name + ' ' + self.user.last_name

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"id":self.user.id})

    def __str__(self):
        return self.user.username






