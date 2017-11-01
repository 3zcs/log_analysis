## Instlation 
You should have python and postgreSQL On your machine.<br />
then download newsdata.sql from udacity and run this command `psql -d news -f newsdata.sql` to add it to your database as `news` table <br />
Fork this files using terminal <br />
`$ git clone https://github.com/3zcs/log_analysis.git`<br />
Then enter your folder <br />
`$ cd log_analysis`<br />
Install `psycopg2` module `pip install psycopg2`<br />

## Run project 
Run this command in terminal and the analysis will be printed `$ python report.py`<br />

## project structure
**report.py** Script file connect and print analysis of log database <br />
