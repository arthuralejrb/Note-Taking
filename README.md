# Note-Taking
Note-taking web app built with django!

## Setup
1. Clone repository:
  ```bash
  git clone https://github.com/arthuralejrb/NoteTaking.git
  cd NoteTaking
  ```
2. Create virtual enviroment:
  ```bash
  python -m venv venv
  source venv/bin/activate #Linux/Mac
  venv/Scripts/activate    #Windows
  ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4.Set up database:
  ```bash
  python manage.py migrate
  ```
5.Run it:
  ```bash
  python manage.py runserver
  ```
