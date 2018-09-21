# Flask on Docker with external PostgreSQL database

A simple Python Flask application running in a Docker container and connecting via SQLAlchemy to a PostgreSQL database.

The database connection information is specified via environment variables `DBHOST`, `DBPASS`, `DBUSER`, and `DBNAME`. This app always uses the default PostgreSQL port.

The application has been modified to match the database created there https://lerlacher.de/posts/2017-10-26-pwned-passwords.en.html
```
docker build -t docker-flask-sample .
docker run -it --env DBPASS="<PASSWORD>" --env DBHOST="<SERVER_HOST_NAME>" --env DBUSER="<USERNAME>" --env DBNAME="<DATABASE_NAME>" -p 5000:5000 docker-flask-sample
```
The app can be reached in your browser at `http://127.0.0.1:5000`.

