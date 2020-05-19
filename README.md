# Company Notes Service

## Introduction 
pyramid - elasticsearch - mongodb project demonstrating full-text search on startup companies

## Setup Instructions
* Ensure Docker Desktop is installed
* Obtain the crunshbase 2013 [database snapshot] \*
* Save and Unzip snapshot to a convenient **local folder** (ex: `~/Downloads`)
* Download this project
* Cd into project root: `$ cd ~/Desktop/pyramid_elasticsearch_mongodb`
* Open `docker-compose.yml` for editing and modify source path `docker-compose.yml:mysql-service/volumes` to match the location of `crunchbase_2013_snapshot_20131212` folder on your system
* Build and run docker images: `$ docker-compose up --build --detach`
* In your favourite command shell, hop on the running pyramid_app container: `$ docker exec -it pyramid_app /bin/sh`
* At the container prompt (ex: `#`), cd into project utils: `$ cd /app/pyramid_app/utils` \**
* Do `$ chmod 777 sql_es_import.py` and run the import `$ ./sql_es_import.py`; You will see a message confirming the number of imported records
* Cd back to project root (`cd /app/pyramid_app/`) then run available tests: `$ python -m unittest -v`
* Browse to home page to verify service is running: `http://localhost`; You will be automatically redirected to the search page
* In the search field, type a company name (ex: `microsoft`) and click `Enter` to see all full-text matches
* Click on any of the matching results to see the company's profile and events

Thank you for using *Company Notes Service*!

\* A free registration may be required <br>
\** `$ cd utils` works too <br>

[database snapshot]: https://data.crunchbase.com/docs/getting-started?utm_campaign=none&utm_source=none&utm_medium=email&utm_content=data_accept_basic
