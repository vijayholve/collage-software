from faker import Faker 
from students.models import Books 
from .data import books_data

fake=Faker() 
def Book_fake_data():
    for name in books_data:
        Books.objects.create(
            name=name,
            author=fake.name(),
            publication_year=fake.year(),
        ) 
        
