from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with a email is successful."""
        email = "yahoo@gmail.com"
        password = "Testpass123"
        user = get_user_model().objects.create_user(email, password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test the email for new user is normalized."""
        email = "yahoo@GmAiL.CoM"
        user = get_user_model().objects.create_user(email, "Testpass123")
        self.assertEqual(user.email.split("@")[1], email.split("@")[1].lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error."""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "Testpass123")

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            "yahoo@gmail.com", "Testpass123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)