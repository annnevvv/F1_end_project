from django.db import models

# Create your models here.

class Quiz(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.TextField()
    correct_choice = models.ForeignKey('Choice', null=True, blank=True, on_delete=models.SET_NULL, related_name='correct_answer')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=250)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text

class UserResponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.Model)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f"User response: {self.question.question_text} - Choice: {self.choice.choice_text}"

