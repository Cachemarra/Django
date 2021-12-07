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

To create the table we will run the command:
``python manage.py migrate``

Now you can check in your database admin if the table is created as you defined.

-----------------

## Creation of SuperUser to /admin

First, run ``python manage.py createsuperuser`` in command line. 
Add the credentials _Username_ , _email address_, _password_.

As this is for learning, it doesn't care if the password is weak and less of 8 chars

Now we can access to /admin.

We want to add the persons model, so we must go to admin.py in **pas** app and register
the model as ``admin.site.register(Person)``.

If you log in again in admin/ you will see the model.

As a recommendation, check all the options and things you can do in the Django administration.
You can try to add a new Person object. It will ask you the fields we defined early.

Doing that you'll see that the new person is added to your SQL table in Postgres.

You can personalized how to change the name showed in the Django administration by adding a
__str__ method in Persona class. Then, refresh the page and the new format will be showed.

Now it doesn't matter where you add a new person to the db, it will be showed everywhere!

--------------

## Creation of new class, Address

The new class will be added in Person class and must be created on models.py inside persons app.

In this ocassion, you must specify the ForeignKey as it is part of other table, this is part
of SQL tables management and specify what will happened if Address field is deleted.
This is how both tables are going to relationate.

As we create a new table we need to emigrate with ``python manage.py makemigrations``

As we changed things in Person database we can delete it and create a new one or make migrations one by one.

In this case we don't care about our registers so we can delete everything, but if we already had a full register
we need to solve every mistake and problems with the database using ``python manage.py migrate``

Remember to register the class in admin.py

Now if you create a new Person object you will see a new field: Address, when add a new address a window
will popup and you need to fill the data.

----------------

## Templates

With render method we can send beautiful images.
We're going to modify webapp/views.py Welcome to change the HttpResponse to render and add the filename.
we must create a 'templates' folder.

Inside we create a welcome.html file.



