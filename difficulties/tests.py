from django.test import TestCase
from .models import Post, Comment

class PostModelTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title="Test Post",
            slug="test-post",
            author=None,  # You might want to create a User instance for testing
            content="This is a test post",
            status=0
        )

    def test_post_creation(self):
        self.assertTrue(isinstance(self.post, Post))
        self.assertEqual(str(self.post), "Test Post | written by None")
