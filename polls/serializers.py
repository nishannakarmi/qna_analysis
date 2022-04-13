from polls.models import Question, Choice, UserAttempt
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer


class QuestionSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'question_choices']


class ChoiceSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = "__all__"


class UserAttemptSerializer(ModelSerializer):
    class Meta:
        model = UserAttempt
        fields = "__all__"
