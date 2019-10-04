import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','protwo.settings')

import django
django.setup()

import random
from apptwo.models import user
from faker import Faker

fakegen=Faker()

# topics=['Search','Social','Marketplace','News','Games']
#
# def add_topic():
#     t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
#     t.save()
#     return t


def populate(N=5):

    for entry in range(N):
        fake_name=fakegen.name().split()
        fake_fname=fake_name[0]
        fake_lname=fake_name[1]
        fake_email=fakegen.email()
        web_pg=user.objects.get_or_create(Fname=fake_fname,Lname=fake_lname,Email=fake_email)[0]

if __name__ == '__main__':
    print("populating script...")
    populate(20)
    print("populating done!")
