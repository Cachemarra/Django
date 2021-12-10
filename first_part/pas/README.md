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

It is important note that now you won't have a main page and must add the /welcome/ in
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

We can create dinamic content with templates using dictionaries in the welcome function and parsing
to the return render.

In the HTML file we need use ``{{}}`` to add variables. The var names must be the same as in the
dictionary.

Now we are going to mix webapp and persons.

First in Views we create a new path called home where we create a person object. As it is child
of models.Model it has an inherith method called objects. we're gonna use it to count persons in the
database.

Then, we add a 'welcome.html' file in templates and called the number_persons variable. Finally, we add 
the route /home to urlpatterns in urls.py in pas folder.

Once checked we will add a view of all persons in the database rendering directly to our home page

This will be achieved by adding a variable persons in welcome function in this way:
``persons = Person.objects.all()``
Django will send us objects of Person class, in background Django will query the db for the info and
transform it to Person objects.

Lastly we add that variable to our dictionary. Now, we have to modify the html file to show the persons.
We go to our html file and create a new div with an unordered list inside. Inside the unordered list, we
use a function for each to create list items containing the elements. The way of creation of a for each is using
double braces with percentage symbol. This is no python but Django render html syntax. The code is the next:
 
``
    <div>
        <ul>
            {% for person in persons %}
                <li> Person: {{person.id}} </li>
            {% endfor %}
        </ul>
    </div>
``

If you want more info you could add it as you'll do in python, e.g. ``{{person.name}}``

--------------

## Adding options

We're gonna  add:

- Link to see details of selected person.
- Link to create a new person.
- Another link to modify.
- Delete a person.

To do the first we must add the link reference in our html, to do that we use ``<a href=''>`` snipet.
as we want a dinamic url, we use double braces to get the person id. The full command will be something like this:
``<a href="person_details/{{person.id}}">See details</a>``

Next we need to define the path of *person_details* in urls.py If we add '<int:id>' we're telling Django to
define the url of the primary key. Then we tell the program that a function will be called, the name will be _personDetails_ and will be
defined  in views.py on persons folder.

The function will have, besides request, *id* which will be pased thanks to <int:id>. We will get the details
using ``Person.objects.get(pk=id)```and then, return a render request to a html that will be created.

We create our *templates* folder in persons app and then create a subfolder called persons, finally, create our html file. You can create your html page
as you want, but try to use ```{{person.id}}, {{person.name}}, {{person.last_name}}, {{person.mail}}```
In my case, each one has in his own div and create a 'return' option which return us to '/home'.

But what will happen if u ask for a person that doesn't exists?
A ugly error will show. We are going to modify the code in views.py to show a 404 in this cases.
To do that we must change the way we ask for that info. We are gonna use get_object_or_404 function, which do everything for us.

Now, if we ask for a person.id that doesn't exists, a 404 page will be show. Note: We are using Debug mode, so if you deactivate it, a 
different 404 page will be shown.

--------------------

For the creation of new persons we're gonna create a new html in the templates/persons folder the name will be 'new'.

We wish to ask for info, so we will use a form and a post request, so the info won't be showed on the url.
Djando help us creating forms that contains all the parameters of our methods, so we are going to create that model.
First, in our html code we open a <form></form> braces and write the future object in it: {{personForm}}.
The model will be defined in persons/views.py

First we create an object called PersonForm and using the function ``modelform_factory(Person, exclude=[])``.
That new class variable will be used in the new function: newPerson. And lastly, we return the render.

Now we create the url for creation of new persons in urls.py and add a href in home html pointing to new_person.html

We can wrap {{personForm}} in <table> to improve the view.

Now, we add a button to submit the new person to our database. This can be done with <button>.
Once added the button, if we try to send data, we will see that we need a token, the CSRF verification will fail.
This is easyly done with ``{% csrf_token %}``. Note: CSRF -> Cross-Site Request Forgery.

Now we need to catch the data in the server!

-----------------------------

As we state before, we want to validate the post petition on newPerson, so we add a check 
to see if the info is parsed as a POST petition.
If not, that means that is the first time the person access to the page so we render the normal page.

In the POST method we create a Person object with the info we get through the data from the POST.
Then, a validation must be done with the method ``personForm.is_valid()``. if it is, then we save it.
If not, we redirect to the home page. To do so we add ``name='index'`` in the home path and add
``return redirect('index')`` in the formPerson.isvalid check.

**NOTE** You can use 'index' in the html href too by using {% url 'name' %}

-------------------------------

Our form was creating by modelform_factory function, but what we have to do if we want to create our own?
First, we must create a new python file in persons folder, it will be called forms.py.

The new file will import ModelForm and have a class that extends from ModelForm.

with fields we are saying that we're gonna use every field of Person class.
with widgets we add the data type in html format.
Much of the data is obtained from django documentation, I strongly recomend check it out

Doing that we can change the code in views, changing the modelform_factory for our own PersonForm method.

-----------

## Edit a person.

We first add the option in our home html as a <a href>. We also do some refactory in our code to show
better our content.

We add the new path in the urls.py and create a new methodin the persons/view called editPerson.
We're gonna copy all the code used in newPerson, as it will be almost the same as django knows if the id
is new or an existing one.
The difference is in the 'else', where we will receive the id in the url, so we need to add the <int:id> in the path and in the
new method.

In the else, we ask for the person by his id and then, we recover the data in PersonForm by the id. Remember that the model
is a Person class.
we create a new html file in templates/persons. we can copy all the html code from new.html.
We just change the title and h1.

If you try to modify a person yo will see that is not modifyed but added a new register with the changes.
To overcome that problem you must add the instance=person in the personForm inside the POST IF. In that way,
django will know what is the person you want to modify.

------------

## Delete a person

Now you should know what to do.

1. Add a new link in hour home html file for deleting a person. P.S. you must add a <th> too.
2. Add the path in urls.
3. Create the deletePerson method in persons/view.py P.S. you can copy the code of edit person.

Now you don't need the request POST method, you can just as for the id and use the .delete() method from class.
Then just redirect to home.

Once created try the metod creating someone new and then, delete it.

-----

## Ordering 

To sort by ID is easy as going to webapp/views and adding the **.order_by()** method instead of **.all()**

That is: ``persons = Person.objects.order_by('id')``