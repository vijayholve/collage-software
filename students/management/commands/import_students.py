import pandas as pd
from django.core.management.base import BaseCommand
from students.models import Student ,ClassGroup
from faker import Faker
class Command(BaseCommand):
    help = 'Import students from an Excel file'
     
    def handle(self, *args, **kwargs):
        Fake=Faker()
        file_path = rf"C:\Users\Vijay\python pro\attendance\students\management\data\Copy of BCA_Science_24.25_BCA(1).xlsx"
        classgroup=ClassGroup.objects.get(name__name="BCA",year="SY")
        try:
            df = pd.read_excel(file_path)

            for _, row in df.iterrows():
                Student.objects.create(
                    roll_no=row['roll no'],
                    name=row['name'],
                    contact=Fake.phone_number() ,
                    classgroup=classgroup,
                )
                
            self.stdout.write(self.style.SUCCESS('Successfully imported student data'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error importing student data: {e}'))
