# WSGI stands for "Web Server Gateway Interface"
# It's a standard Python interface for web applications
# This file is used by production servers like Gunicorn to run your Flask app
# When you run flask run or use Gunicorn, it loads this file to start your application
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()