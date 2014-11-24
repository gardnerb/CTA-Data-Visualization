CTA-Data-Visualization
======================
For this example to work, you will need to have Bottle (http://bottlepy.org/docs/dev/index.html)
and Peewee (https://github.com/coleifer/peewee) installed. I suggest using a virtualenv and 
running 'pip install bottle peewee'

You will also have to create a mysql user 'ctauser' and a mysql database 'cta', with 'ctauser' granted all permissions to 'cta'

To setup the database, run "python db_setup.py" and then "python pull_data.py"
To run the visualization, you will have to change the ROOT_PATH in maptest.py and then run "python maptest.py" and navigate your browser to http://localhost:8040/map.
