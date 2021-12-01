# The Shrinker!

## Functionality

- Users can enter a url into an input box on the home page
- If a User tries to access the website via a path stored in the attached database, they will get rerouted to the URL it relates to
- If a User tries to access the website with a path not have in the attached database, they will get rerouted to the homepage where they can create a new short URL

## Installation & Usage

### Installation

- Clone repo and cd into project folder
- Run pipenv shell to create the virtual environment
- Run pipenv install to install the required packages

### Usage

- Run the app with 'python manage.py runserver' then navigate to localhost:8000
- Home page will load from there with the url shortner that will render the shortened link once a url is submitted 
- Each link is then available at localhost:8000/shrinker/<--generated token-->

