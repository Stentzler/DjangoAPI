from django.core.management.base import BaseCommand, CommandError
from custom_users.models import User
from addresses.models import Address


class Command(BaseCommand):
    help = "Create a superuser"

    user_data = {
        "username": "superuser",
        "rg": "999-999-999",
        "first_name": "super",
        "last_name": "user",
        "age": 00,
        "contacts": "super",
        "email": "superuser@gmail.com",
        "password": "1234",
    }

    address_data = {
        "zipcode": "123123",
        "district": "Centro",
        "state": "RS",
        "street": "Rua",
        "number": "123A",
    }

    def handle(self, *args, **options):
        address = Address.objects.create(**self.address_data)
        User.objects.create_superuser(**self.user_data, address=address)

        self.stdout.write(
            self.style.SUCCESS(
                f"Username:superuser // Password:1234  ---------- Successfully created ----------"
            )
        )
