env/scripts/activate       

python manage.py runserver           

celery -A attendance.celery worker --pool=solo -l info

celery -A attendance beat --loglevel= 
