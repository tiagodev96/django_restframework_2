import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from clients.models import Client


def create_clients(quantidade_de_pessoas):
    fake = Faker("pt_BR")
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        document = CPF()
        name = fake.name()
        email = "{}@{}".format(name.lower(), fake.free_email_domain())
        email = email.replace(" ", "")
        document = document.generate()
        phone = "{} 9{}-{}".format(
            random.randrange(10, 21),
            random.randrange(4000, 9999),
            random.randrange(4000, 9999),
        )
        is_active = random.choice([True, False])
        p = Client(
            name=name, email=email, document=document, phone=phone, is_active=is_active
        )
        p.save()


create_clients(50)
