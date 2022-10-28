from rest_framework import viewsets, serializers, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Submission


# Create your views here.


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ('id', 'data', 'comment')


class SubmissionViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

    def create(self, request, *args, **kwargs):
        submission = Submission(
            data=request.data['feedback_data'],
            comment=request.data['comment']
        )
        submission.save()

        submission_serialized = SubmissionSerializer(submission)
        return Response(status=status.HTTP_200_OK, data=submission_serialized.data)
