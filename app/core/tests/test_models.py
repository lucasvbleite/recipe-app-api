from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating user with email is successful"""
        email = "testando@emaildementira.com"
        password = "senha123!@#"

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """testa o email se eh normalized"""
        email = 'teste@EMAILDEMENTIRA.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """testa criar usuario sem email volta erro"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '12345')

    def test_create_new_superuser(self):
        """testa criar novo superuser"""
        user = get_user_model().objects.create_superuser(
            'testando@emaildementira.com',
            'teste123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
