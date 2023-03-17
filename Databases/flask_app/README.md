# Manga Database Management App

## Background
Got bronchitis, made this.
It's a Flask application (i.e. a local website, zero JavaScript) which manages a PostgreSQL database of manga (or really any type of comic book).
I don't have a huge collection, but I do have a fair few. Excel is great, but... leaves something to be desired. Lo, HTML, Python, and SQL!

## Running it yourself
To run it yourself, you'll need Flask, Flask_bcrypt, Flask_login, Flask_wtf (yes, apparently so), wtforms, PostgreSQL, Python and
Psycopg2. Install and run everything through the Linux Subsystem if you're on Windows (not necessary, but easier).
The following tutorial to get it running was initially written by Pax, a TA on the course Udvikling af Informationssystemer.
Mac-users will just write "psql" instead of "psql -U postgres", apparently. Idk, don't own one.

To initialise the database:
Go to the flask_app folder. $ indicates a command.
(Windows only:) $ sudo service postgresql start 
$ psql -U postgres
$ CREATE DATABASE mangadb;
$ ALTER USER postgres PASSWORD '123'; -- Adjust this to whatever you want, just be sure to also adjust __init__.py.
$ \q
$ cd manga
$ psql -U postgres -d manga
$ \i schema.sql
(Optionally) To enter some default values that I designed, type
$ \i schema_ins.sql
$ \q

Now to run the application itself. In the same terminal, go back up to the flask_app folder, and then:
$ python3 run.py

If this does not work, try:
$ export FLASK_APP=run.py
$ export FLASK_ENV=development
$ export FLASK_RUN_PORT=5000   (or any other port number)
$ flask run
If you close Flask (but not the terminal), you need only type the final line in the future.

Finally, go to your browser and type in 127.0.0.1:5000 and you should see the "web"site. Enjoy.

## Notes
Allow me to under-sell and so hopefully one day over-deliver:
The Flask-specific code is essentially all boiler-plate, lifted from Flask tutorials and/or what was
given to us already-written by our TA/professor at the beginning of the course UIS - Udvikling af Informationssystemer/
Development of Information Systems (it's been renamed now and split into two, as I understand).

The application code also bears a resemblance to the barebones version of MinSundhedsplatform that my group and I made for the course
in order to showcase some prototypes for improvements. Thus, I feel it would be hubris to take full credit for everything, as
it was inspired by what we made together. What we made was far more interesting and feature-complete, and I don't think there's any
particularly impressive code here anyway, but better safe (and honest) than sorry. Also much of it is HTML, which... isn't even technically
code, is it? But still, it too was inspired by what we wrote together.