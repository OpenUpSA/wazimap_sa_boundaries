# SA Boundaries Wazimap App

Wazimap app adds provicial boundaries to the database. This is needed point point in polygon searches, e.g. find all points in this province. This app was development together with Explorer and is dependent on it. In future this dependency might be removed. Additional boundaries (e.g. municipality, district, etc) will also be added.

## Installation

1. Clone the code into the python path (usually inside your Django project). 
2. Add sa_boundaries to your INSTALLED_APPS. 
3. Load the province data into your database, e.g. 
  3.1 gunzip fixtures/provinces.json.gz
  3.2 python manage.py loaddata fixtures/provinces.json

You may need to tweak these instructions to work with your setup
