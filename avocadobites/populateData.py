import os
import json
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'avocadobites.settings')

import django
# Import settings
django.setup()

from userprofile.models import Profile
from django.contrib.auth.models import User
from faker import Faker
import random
fakegen = Faker()


def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''
    N = 5
    for entry in range(N):
        # Create Fake Data for entry
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()
        faker_username = fake_last_name[:2]+fake_first_name[:3]
        faker_username = faker_username.lower()
        new_password = fake_last_name+"@123"
        # Create new User Entry
        # print(fake_name, fake_first_name, fake_last_name, fake_email, new_password)
        user1 = User.objects.get_or_create(username=faker_username,
                                          first_name=fake_first_name,
                                          last_name=fake_last_name,
                                          email=fake_email,
                                          password=new_password)[0]
        
        
        employee_code = "AB0000"+str(N)
        N = N+1
        department = random.randint(1, 24)     
        designation = "Default"
        skill_level = random.randint(1, 10)
        date_of_birth = fakegen.date_of_birth()
        birth_place = "bellary"
        current_location = fakegen.city()
        date_of_joining = fakegen.date_of_birth()
        gender = random.choice(["male", "female"])
        blood_group = random.choice(["A","A+","B","B+","AB","AB+"])
        personal_phone_number = fakegen.phone_number()
        Profile.objects.get_or_create(user=user1, employee_code=employee_code, designation=designation, skill_level=skill_level, 
        date_of_birth=date_of_birth, birth_place=birth_place, current_location=current_location, 
        date_of_joining=date_of_joining, gender=gender, blood_group=blood_group, personal_phone_number=personal_phone_number)
        

populate(N=100)
# imp_users = ['desan','hurni','deray','avocado','desam']
# all_users = User.objects.all()
# for i in all_users:
#     if i.username not in imp_users:
#         i.delete()