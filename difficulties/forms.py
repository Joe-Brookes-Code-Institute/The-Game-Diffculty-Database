from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'body',
            'challenge',
            'enemy_health',
            'player_health',
            'resources_available',
            'extra_content',
            'exclusive_unlockables',
            'new_game_plus_only',
        ]
        
    # You can add additional fields that are not in the Comment model if needed
    ai_difficulty = forms.IntegerField(required=False, min_value=1, max_value=10, 
                                       help_text="Rate the AI difficulty from 1 to 10")
    trophies = forms.BooleanField(required=False, 
                                  help_text="Are there trophies/achievements for this difficulty?")
    unlockable_difficulty = forms.BooleanField(required=False, 
                                               help_text="Is this an unlockable difficulty?")
    switchable_mid_game = forms.BooleanField(required=False, 
                                             help_text="Can the difficulty be changed mid-game?")
    trophy_stacking = forms.BooleanField(required=False, 
                                         help_text="Do trophies/achievements stack across difficulties?")
    other = forms.CharField(required=False, widget=forms.Textarea, 
                            help_text="Any other comments about the difficulty?")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].label = "Your opinion"
        self.fields['challenge'].label = "Difficulty rating"