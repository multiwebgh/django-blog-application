# django-blog-application

A full-featured blog application built with Django that includes user authentication, profile management, blog post creation with comments and likes.

## Features

- **User Authentication**
  - User registration and login
  - User profile management
  - Profile photo upload
  - Custom user profiles

- **Blog Functionality**
  - Create, read, update, and delete blog posts
  - Blog post images
  - Comment system
  - View user's own posts
  - Responsive design with Bootstrap 5

## Technologies Used

- Python 3.13
- Django 6.0
- Django Bootstrap 5
- Pillow (Image processing)
- SQLite (Database)
- python-dotenv (Environment variables)

## Installation

### Prerequisites

- Python 3.13 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd "django-blog-application"
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv env
   ```

3. **Activate the virtual environment**
   - Windows (PowerShell):
     ```powershell
     .\env\Scripts\Activate.ps1
     ```
   - Windows (Command Prompt):
     ```cmd
     .\env\Scripts\activate.bat
     ```
   - macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install django django-bootstrap5 pillow python-dotenv
   ```

5. **Set up environment variables**
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Generate a new SECRET_KEY:
     ```bash
     python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
     ```
   - Update the `.env` file with your SECRET_KEY and other settings

6. **Run migrations**
   ```bash
   python manage.py migrate
   ```

7. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Open your browser and go to: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`



## Project Structure

```
django-blog-application/
├── authentication/          # User authentication app
│   ├── models.py           # User profile models
│   ├── views.py            # Authentication views
│   ├── forms.py            # User forms
│   └── urls.py             # Authentication URLs
├── blog/                   # Blog app
│   ├── models.py           # Blog and Comment models
│   ├── views.py            # Blog views
│   ├── forms.py            # Blog forms
│   └── urls.py             # Blog URLs
├── media/                  # User uploaded files
│   ├── blog_images/        # Blog post images
│   └── profile_photos/     # User profile photos
├── mystaticfiles/          # Static files (CSS, images)
├── template/               # HTML templates
│   ├── auth/               # Authentication templates
│   └── blog/               # Blog templates
├── project/                # Project settings
│   ├── settings.py         # Django settings
│   └── urls.py             # Main URL configuration
├── .env                    # Environment variables (not in git)
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore file
├── manage.py               # Django management script
└── README.md               # This file
```

## Usage

### Creating a Blog Post

1. Register an account or log in
2. Complete your profile setup
3. Navigate to "Create Post"
4. Fill in the title, content, and upload an image
5. Click "Submit" to publish your post

### Managing Your Profile

1. Log in to your account
2. Click on your profile
3. Update your profile information or photo
4. Save changes

### Commenting on Posts

1. Navigate to any blog post
2. Scroll to the comments section
3. Write your comment and submit

## Development

### Running Tests

```bash
python manage.py test
```

### Creating Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Collecting Static Files (for production)

```bash
python manage.py collectstatic
```

## Deployment

For production deployment:

1. Set `DEBUG=False` in your `.env` file
2. Update `ALLOWED_HOSTS` with your domain
3. Use a production database (PostgreSQL, MySQL)
4. Set up a web server (Nginx, Apache)
5. Use a WSGI server (Gunicorn, uWSGI)
6. Configure static files serving
7. Set up SSL certificate

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For questions or support, please open an issue in the repository.

## Acknowledgments

- Django Documentation
- Bootstrap 5
- Django Bootstrap 5 package
- All contributors and supporters
