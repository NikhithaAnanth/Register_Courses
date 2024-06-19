# Register_Courses
A simple Django project that shows implementation of forms to take input and data is saved in Django's SQLite. The admin access is also available.
# Project Creation
django-admin startproject courses
# App Creation 
django-admin startapp newforms
#
*   create new files- forms.py, urls.py in app
*   make files for html and css
*   refer code

# Making Migrations
python manage.py makemigrations
python manage.py migrate
# Creating Super-User (admin)
python manage.py createsuperuser
*   enter the following details
  
![image](https://github.com/NikhithaAnanth/Register_Courses/assets/171590975/f5de610b-6d6a-4d8a-b9b7-c3656d8f0933)

# Run
python manage.py runserver
# Expected Outputs
*   /newforms

![image](https://github.com/NikhithaAnanth/Register_Courses/assets/171590975/82512dcd-b00c-4e96-90ea-432cc458ceab)

*   /admin

![image](https://github.com/NikhithaAnanth/Register_Courses/assets/171590975/c70b743f-cb6b-4fff-8822-b0d6f34fc424)

*   dbsqlite viewer

![image](https://github.com/NikhithaAnanth/Register_Courses/assets/171590975/eb57b2b0-eed7-4b8c-aa52-e65aa4f7bfbc)

