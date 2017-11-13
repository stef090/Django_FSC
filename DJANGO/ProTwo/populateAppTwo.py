import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

## FAKER
from AppTwo.models import User
from faker import Faker
import random

fakegen = Faker()


def populate(number=10):

    for num in range(number):

        fake_name = fakegen.first_name()
        fake_surname = fakegen.last_name()
        fake_email = fakegen.email()

        user = User.objects.get_or_create(name=fake_name,
                                  surname=fake_surname,
                                  email=fake_email)[0]

if __name__=='__main__':
    print("Populating users!")
    populate()
    print("Population complete!")
