# Choatix-assignment
This is assigment to get the chance of interview in Chatix AI company.
This is Django project. It generates the all images parallelly from provided prompt using Stability AI.

## Setup and activate the virtual env
### python -m venv venv
### for mac os: source venv/bin/activate
### for windows: .\venv\Scripts\activate

## Setup backend
### Clone this repo
### go inside this repo
### install dependencies: pip install -r requirements.txt
### Add stability API access token and number of images to generate parallelly (for this assigment 3) in file home/.env
### run migrations if any: 
### python manage.py makemigrations
### python manage.py migrate
### run server: python manage.py runserver

### Make sure redis is running in background
### in another terminal, activate the same virtual env and go to the cloned repo and start celery worker using: celery -A chaotix worker --loglevel=info


## Test it:
### goto the local host http://127.0.0.1:8000/
### enter prompt and generate images
### Note 1: image generation takes 8 credit so if you are generating 3 images then make sure that Stability account have at least 24 credits
### Note 2: never commit .env file, here .env is attached without secret only for information
