from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from polls.models import Question, Choice
from polls.serializers import QuestionSerializer, ChoiceSerializer, UserAttemptSerializer


# Create your views here.
def index(request):
    return HttpResponse("This is the starting Page")


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class QuestionAnswerSession(APIView):

    @staticmethod
    def _next_question(request, q_n: int):
        try:
            question = Question.objects.get(pk=q_n)
        except Question.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = QuestionSerializer(question, context={'request': request})
            return Response({"question": serializer.data})

    def get(self, request):
        next_qn = int(request.GET.get('question', 0)) + 1
        return self._next_question(request, next_qn)

    def post(self, request):
        next_qn = int(request.data.get("question", 0)) + 1

        serializer = UserAttemptSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return self._next_question(None, next_qn)
        return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)
