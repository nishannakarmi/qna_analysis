# User Behaviour Analysis through Series of QnA

## Installation Steps

- Install python 3.9.9 (Either install using virtualenv or in system python)
- Install python packages mentioned in requirements.txt, pip install -r requirements.txt
- Change the database related settings in the settings.py file
- Run the command, `python manage.py migrate` to apply database table changes
- Run the development server as `python manage.py runserver`
- Create a superuser to access django admin console as, `python manage.py createsuperuser`
- Optional, Create a new user through django admin console

## List of available APIs,
- api/qna:
  - Methods: GET/POST
    - GET
      - param:
        - next_question: [int]/optional
    - POST
      - param:
        - user: [int]/optional
        - question: [int] (Question ID)
        - answer: [int] (choice ID)
        
