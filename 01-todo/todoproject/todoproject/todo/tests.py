from django.test import TestCase, Client
from django.urls import reverse
from .models import Todo
from datetime import date, timedelta

class TodoModelTest(TestCase):
    def test_create_todo(self):
        """Test creating a TODO item"""
        todo = Todo.objects.create(
            title="Test TODO",
            description="Test Description"
        )
        self.assertEqual(todo.title, "Test TODO")
        self.assertEqual(todo.resolved, False)
        
    def test_todo_str(self):
        """Test the string representation of TODO"""
        todo = Todo.objects.create(title="Test TODO")
        self.assertEqual(str(todo), "Test TODO")

class TodoViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_home_view(self):
        """Test the home view displays todos"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        
    def test_create_todo_view_get(self):
        """Test GET request to create todo view"""
        response = self.client.get(reverse('create_todo'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_todo.html')
        
    def test_create_todo_view_post(self):
        """Test POST request creates a todo"""
        response = self.client.post(reverse('create_todo'), {
            'title': 'New TODO',
            'description': 'Test description',
            'due_date': date.today() + timedelta(days=7)
        })
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertEqual(Todo.objects.count(), 1)
        todo = Todo.objects.first()
        self.assertEqual(todo.title, 'New TODO')
        
    def test_edit_todo_view(self):
        """Test editing a todo"""
        todo = Todo.objects.create(title="Original Title")
        response = self.client.post(
            reverse('edit_todo', args=[todo.pk]),
            {'title': 'Updated Title', 'description': 'Updated description'}
        )
        self.assertEqual(response.status_code, 302)
        todo.refresh_from_db()
        self.assertEqual(todo.title, 'Updated Title')
        
    def test_delete_todo_view(self):
        """Test deleting a todo"""
        todo = Todo.objects.create(title="To Delete")
        response = self.client.post(reverse('delete_todo', args=[todo.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Todo.objects.count(), 0)
        
    def test_toggle_resolved(self):
        """Test toggling resolved status"""
        todo = Todo.objects.create(title="Test TODO")
        self.assertFalse(todo.resolved)
        
        response = self.client.get(reverse('toggle_resolved', args=[todo.pk]))
        todo.refresh_from_db()
        self.assertTrue(todo.resolved)
        
        response = self.client.get(reverse('toggle_resolved', args=[todo.pk]))
        todo.refresh_from_db()
        self.assertFalse(todo.resolved)
