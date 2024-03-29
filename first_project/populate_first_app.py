import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord,Topic,WebPage
from faker import Faker

fakegen=Faker()

topics=['Search','Social','Marketplace','News','Games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):

    for entry in range(N):
        t=add_topic()
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()
        web_pg=WebPage.objects.get_or_create(Topic=t,name=fake_name,url=fake_url)[0]
        acc_rec=AccessRecord.objects.get_or_create(name=web_pg,date=fake_date)[0]

if __name__ == '__main__':
    print("populating script...")
    populate(20)
    print("populating done!")
