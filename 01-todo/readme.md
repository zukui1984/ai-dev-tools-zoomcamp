A simple TODO application built with Django as part of the AI-Assisted Development homework.

## Features

- Create, edit, and delete TODOs
- Assign due dates to tasks
- Mark TODOs as resolved
- Clean and intuitive interface

## Installation

1. Install Django:
```python
pip install django
```

2. Clone the repository:
```python
git clone <your-repo-url>
cd todoproject
```

3. Run migrations:
```python
python manage.py makemigrations
python manage.py migrate
```

4. Create a superuser (optional, for admin access):
```python
python manage.py createsuperuser
```

5. Run the development server:
```python
python manage.py runserver
```

6. Open your browser and navigate to `http://127.0.0.1:8000/`

## Application Screenshots

### Home Page - TODO List
<img width="361" alt="TODO List View" src="https://github.com/user-attachments/assets/75c228c1-c0de-461a-a31f-a4a21fe71481" />

*Main page showing all TODO items with their status*

### Create New TODO
<img width="546" alt="Create TODO Form" src="https://github.com/user-attachments/assets/5d740b5d-a6f7-4d68-9b9a-7f75720f0c9c" />

*Form to create a new TODO with title, description, and due date*

### Edit TODO
<img width="534" alt="Edit TODO Form" src="https://github.com/user-attachments/assets/5a6180a0-7850-4968-9a61-b07a5c1c1461" />

*Edit existing TODO items*

### Delete Confirmation
<img width="524" alt="Delete Confirmation" src="https://github.com/user-attachments/assets/9c35faf6-d08a-4a0f-9d2f-147660f19b65" />

*Confirmation page before deleting a TODO*

