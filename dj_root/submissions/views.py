from django.shortcuts import render
from rest_framework import viewsets, serializers, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Submission

# Create your views here.


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ('id', 'name', 'data', 'comment')


class SubmissionViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = SubmissionSerializer

    def list(self, request, *args, **kwargs):
        queryset = Submission.objects.all()
        return Response(status=status.HTTP_200_OK, data=queryset)

    def create(self, request, *args, **kwargs):
        submission = Submission(
            name=request.data['name'],
            data=request.data['feedback_data'],
            comment=request.data['comment']
        )
        submission.save()

        submission_serialized = SubmissionSerializer(submission)
        return Response(status=status.HTTP_200_OK, data=submission_serialized.data)
