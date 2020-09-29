import os

import random
import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

django.setup()

from first_app.models import AccessRecord, Topic, Webpage

fake_gen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(n=5):

    for entry in range(n):

        # get the topic for the entry
        top = add_topic()

        # Create the fake data for that entry
        fake_url = fake_gen.url()
        fake_date = fake_gen.date()
        fake_name = fake_gen.company()

        # Create the new webpage entry
        web_pg = Webpage.objects.get_or_create(
            topic=top, url=fake_url, name=fake_name)[0]

        # create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(
            name=web_pg, date=fake_date)


if __name__ == '__main__':
    print("populating in scripts")
    populate(20)
    print("Populating complete")
