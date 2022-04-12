from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text[:90]


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    correct_choice = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class UserAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, blank=True)
    answer = models.ForeignKey(Choice, on_delete=models.SET_NULL, null=True, blank=True)
    attempted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} has answered: {self.answer.choice_text}, which is: {self.answer.correct_choice}" \
               f" for question: {self.question}"

    class Meta:
        unique_together = ['user', 'question', 'answer']
