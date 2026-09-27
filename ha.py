from faker import Faker

fake = Faker("ru_RU")

print("Случайное имя:", fake.name())
print("Случайный адрес:", fake.address())