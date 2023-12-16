poetry install
python manage.py makemigrations users
python manage.py makemigrations authorization
python manage.py makemigrations task_manager
python manage.py makemigrations statuses
python manage.py makemigrations labels
python manage.py makemigrations tasks
python manage.py migrate