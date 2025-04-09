# ToDo App

This is a simple ToDo application built using Django. The app allows users to create, update, delete, and toggle the completion status of tasks.

## Features

- Add new tasks with a title, description, due date, and due time.
- Edit existing tasks.
- Mark tasks as completed or incomplete.
- Delete tasks.
- View all tasks in a user-friendly interface.

## Project Structure

backend/ ├── app/ │ ├── admin.py │ ├── apps.py │ ├── forms.py │ ├── migrations/ │ │ ├── 0001_initial.py │ │ └── __init__.py │ ├── models.py │ ├── static/ │ │ └── style.css │ ├── templates/ │ │ ├── index.html │ │ └── taskform.html │ ├── tests.py │ ├── urls.py │ ├── views.py │ └── __init__.py ├── db.sqlite3 ├── manage.py ├── project/ │ ├── asgi.py │ ├── settings.py │ ├── urls.py │ ├── wsgi.py │ └── __init__.py

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd backend

   ```

Create a virtual environment and activate it:

Install the required dependencies:

Run migrations to set up the database:

Start the development server:

Open your browser and navigate to http://127.0.0.1:8000/ to access the app.

## Usage

Homepage: Displays the list of tasks.
Add Task: Click the "Add new Task" button to create a new task.
Edit Task: Click the edit icon next to a task to update its details.
Toggle Completion: Click the check icon to mark a task as completed or incomplete.
Delete Task: Click the trash icon to delete a task.
**Models**
**Task**
**title**: A short title for the task (max length: 30).
**description**: A detailed description of the task (optional).
**due_date**: The due date for the task.
**due_time**: The due time for the task.
**completed**: A boolean indicating whether the task is completed.
**Templates**
**index.html**: Displays the list of tasks.
**taskform.html**: Form for creating or editing tasks.
**Static Files**
**style.css**: Contains the styling for the app.
**Admin Panel**
Access the admin panel at http://127.0.0.1:8000/admin/. Use the Django admin interface to manage tasks.

## License

This project is licensed under the MIT License.

## Acknowledgments

Built with Django.
Icons provided by Boxicons.
