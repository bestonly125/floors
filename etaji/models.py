from django.db import models

class Apartment(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    square_footage = models.FloatField()
    number_of_rooms = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.address}, {self.city}"

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Transaction(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    seller = models.ForeignKey(Person, related_name='transactions_as_seller', on_delete=models.CASCADE)
    buyer = models.ForeignKey(Person, related_name='transactions_as_buyer', on_delete=models.CASCADE)
    transaction_date = models.DateField()
    sale_price = models.FloatField()

    def __str__(self):
        return f"Transaction {self.id}: {self.apartment} - {self.sale_price}"

class Agency(models.Model):
    agency_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.agency_name

class Agent(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.person} ({self.license_number})"
