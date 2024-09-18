from django.db import models
from django.contrib.auth.models import User

# Define post statuses, like Draft or Published
STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    content = models.TextField(default="")
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

# Updated Comment model to work better for game-related feedback
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()  # This will be the user's opinion/feedback
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    # Game-specific challenge rating
    challenge = models.FloatField(default=3.0, help_text="Rate the difficulty from 1 to 5")

    # Game-specific feedback or submission fields
    enemy_health = models.IntegerField(default=100, help_text="Enemy health as a percentage")
    player_health = models.IntegerField(default=100, help_text="Player health as a percentage")
    resources_available = models.CharField(max_length=100, default="Normal", help_text="Describe resource availability (e.g., Abundant, Scarce)")

    # Additional game-specific features (e.g., difficulty extras)
    extra_content = models.BooleanField(default=False, help_text="Tick if this difficulty has extra content")
    exclusive_unlockables = models.BooleanField(default=False, help_text="Tick if there are exclusive unlockables")
    new_game_plus_only = models.BooleanField(default=False, help_text="Tick if this is a New Game Plus exclusive difficulty")

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title[:30]}..."
