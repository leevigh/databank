from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

gender_choice = (
    ('m', 'Male'),
    ('f', 'Female')
)

# disabilities = (
#     ('n', 'None'),
#     ('s', 'Specify')
# )
educational_qualification = (
    ('ssce', 'SSCE'),
    ('undergrad', 'Undergraduate'),
    ('postgrad', 'Postgraduate'),
    ('hnd', 'HND'),
    ('nd', 'ND/Diploma'),
    ('bsc', 'BSc'),
    ('ba', 'BA'),
    ('be', 'BE'),
    ('msc', 'MSc'),
    ('ma', 'MA'),
    ('m.ed', 'MEd'),
    ('mba', 'MBA'),
    ('phd', 'PhD'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to = 'assets/images',
        #default = 'no-img.jpg',
        blank=True
    )
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField(default='none@email.com')
    birth_date = models.DateField(default='1999-12-31')
    bio = models.TextField(default='', blank=True)
    course_of_study = models.CharField(max_length=200, default='')
    educational_qualification = models.CharField(max_length=200, choices=educational_qualification, default='')
    skills = models.CharField(max_length=500, blank=True, default='')
    address = models.CharField(max_length=1200, default='')
    permanent_address = models.CharField(max_length=1200, default='')
    lga = models.CharField(max_length=20, default='')
    ward = models.CharField(max_length=1200, default='')
    village = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=gender_choice)
    disabilities = models.CharField(max_length=200, blank=True, default='')
    cv = models.FileField(upload_to='cv/%Y/%m/%d', max_length=200, blank=True)
    certs = models.FileField(upload_to='certs/%Y/%m/%d', max_length=200, default='', blank=True)

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

