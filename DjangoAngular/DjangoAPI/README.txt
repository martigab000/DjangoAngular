1. make ure you hav the follwing installed
   Node Js
   Angular  COMMAND: install -g @angular/cli         LINK for help: https://angular.io/guide/setup-local 
   Python
   Django  pip install django
   Django rest_framework - pip install djangorestframework
   Django cors headers - pip install django-cors-headers 

2. I really recommend watching at least the first 10 miutes of the video, super helping with all the installs  
    and how everything works with the environment and the command propmt

3. To run the program you will need this command "python manage.py runserver" just run that in the command propmt and its running and is connected to postaman

4. for you to make request in post man you will need to use one of these urls depending on what youre doing 
http://127.0.0.1:8000/
http://127.0.0.1:8000/department/
http://127.0.0.1:8000/employees/

5. For the angular/Ui portion thi work you will need to install angular on your computer, see link i provided for help
"ng generate" app-name  this will create an angular app for you
you then need to cd into that app, because it creates a folder for it
only after you have cd then you can run the app with this command "ng serve --open"

How to quick setup angular after cloning the repository
   1. cd into folder "ui"
   2. run command "npm install -g @angular/cli"
   3. cd into "angular10"
   4. run "ng serve --open"
   5. if you get an Error "could not find the '@angular-devkit/build-angular:dev-server' builder's node pckage." or any error about a node package
   6. run "npm install"
   7. now "ng serve --open" will work.