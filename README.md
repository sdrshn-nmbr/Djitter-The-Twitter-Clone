<h1 style="text-align:center">
  <img src="https://github.com/sdrshn-nmbr/Djitter-The-Twitter-Clone/blob/main/static/images/logo.png" alt="GitHub Logo" style="width:5%;">
  Djitter
</h1>

Djitter is a Twitter clone web application built with Django. Users can post "chirps", look at other users' recent activity, and learn more about anything and everything!

## Features

- **User Accounts**
  - Register, login, logout
  - Profile page with 'Chirps' and recent activity

- **Chirps**
  - Post updates and search others' chirps
  - Delete AND edit djits

- **Im Feeling Chirpy!**
  - Takes user to a random 'Chirp' for a rabbit hole adventure!

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sdrshn-nmbr/Djitter-The-Twitter-Clone.git
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   Create a `.env` file and add environment variables for Django secret key, database configuration, etc.

5. **Run migrations:**
   ```bash
   python manage.py makemigrations
   ```
   ```bash
   python manage.py migrate
   ```

6. **Start the dev server:**
   ```bash
   python manage.py runserver
   ```

7. **Open your browser to `http://localhost:8000`**

## Technologies

- Django
- Django REST Framework
- Bootstrap

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Acknowledgements

Inspired by Twitter.
