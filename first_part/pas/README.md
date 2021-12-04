# Person Administrator Service

First Django project.

To see if Django is correctly working and also the first thing you should try you must 
execute the next command:

`python manage.py runserver`

Note how an sqlite file is created.

Then we're going to create an app to the general use of our website. We must be on the first 'pas' folder
and then run

`python manage.py startapp webapp`

A new folder called **webapp** will be created. It contains all the scripts necessary for the creation and develop of
flask projects.

-----------

The next step is register the new application **webappp** in  the sap folder which contain a ``settings.py`` script
and then add the name in the ``INSTALED_APPS`` list, keeping the comma (`,`)

---------------

From url file we can add routes and urls for our app, adding the ``/`` in the webbrowse address.

We are going to add a new path, 'welcome/' (the `/` is important!) and tell the script that
must call a 'welcome' function in views.

It is importantto note that now you won't have a main page and must add the /welcome/ in
your webbrowser.

You can change this by writing the above code in urls script.
`` path('/', welcome)``

-----------------

Now we are going to add a new path 'goodbye' and a function in views.

As it have the html extension, you should add it in the webrowser, but if you don't specify
the extention you could access without it.

Now we create a `contact` url with info.

----------------

## Working with Postgress

Instead using sqlite as many tutorials, we're going to use a real SQL Server, as SQLite
is mostly used as tests.

We create a database called pass_db. And now we open the settings.py script to add the
postgres db to the DATABASES dictionary.

Remember that psychopg2 must be installed via pip to be used.

The apps in 'settings' are automatically configurated to our database when runs the server.
at first, they will show as non configurated migrations, we can se a list writing:

``python manage.py showmigrations``

To apply the migrations we write
``python manage.py migrate``

After that, our sql database will have new tables created by Django and will be used
automatically by it.

---------------------

A Django project will have some apps so we are going to create a new webapp
called persons

Some files could be deleted, but we're gonna left it as default.

Remember that we should add our new app in the settings.py script in Installed_Apps


Once added our new app we go to persons/models to create a representation of our table which
consist in 4 rows:
- id (integer)
- name (character varying)
- last_name (character varying)
- mail (character varying)

This will be implemented as a model class extended of a father class models.Model

You can check the fields documentation in django to see all datatypes we can use to our
class.

once added all fields, we make migrations to generate a document that can convert
our class to a db table:
``python manage.py makemigrations``

Now we can see the code Django is going to use by open the ``file 0001_initial.py`` in migrations folder
inside our app.

To see the SQL command that is going to be executed we could run:
``python manage.py sqlmigrate persons 0001``



