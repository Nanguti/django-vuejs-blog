"# django-vuejs-blog"

# Django-Vue.js Blog Project

This is a blog project built with Django on the backend and Vue.js with Composition API on the frontend. It utilizes Axios for API consumption and Vue Router for page navigation.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Nanguti/django-vuejs-blog.git
   ```

2. Navigate into the project directory:

   ```bash
   cd django-vuejs-blog
   ```

3. Install backend dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Install frontend dependencies:

   ```bash
   cd frontend
   npm install
   ```

## Usage

1. Start the Django backend server:

   ```bash
   python manage.py runserver
   ```

2. Start the Vue.js frontend server:
   ```bash
   cd frontend
   npm run serve
   ```
3. Access the application in your browser at http://localhost:8000.

## Folder Structure

    ```bash
    ├── backend/                # Django backend codebase
    │   ├── base/         # Django project settings and configurations
    │   ├── blog/               # Django blog directory
    │   └── manage.py           # Django management script
    └── frontend/               # Vue.js frontend codebase
        ├── public/             # Public assets and HTML template
        ├── src/                # Vue.js source code
        │   ├── assets/         # Vue.js assets (images, fonts, etc.)
        │   ├── components/     # Vue.js components
        │   ├── router/         # Vue Router configuration
        │   ├── views/          # Vue.js views
        │   ├── App.vue         # Root Vue component
        │   └── main.js         # Vue.js entry point
        ├── index.html          # Main HTML template
        ├── package.json        # npm package configuration
        ├── postcss.config.js   # PostCSS configuration
        ├── tailwind.config.js  # Tailwind CSS configuration
        ├── vite.config.js      # Vite.js configuration
        └── .gitignore          # Git ignore configuration file
    ```
