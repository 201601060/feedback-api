from django.contrib.auth import authenticate
from rest_framework import viewsets, serializers, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import UserLoginForm
from .models import Submission


# Create your views here.

class Login(APIView):

    def post(self, request):
        user_login_form = UserLoginForm(request.data)
        if user_login_form.is_valid():
            email = user_login_form.cleaned_data['email']
            password = user_login_form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user:
                token = Token.objects.get_or_create(user=user)[0]
                return Response(status=status.HTTP_200_OK,
                                data={'success': True, 'Token': token.key})
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED, data={'success': False})
        else:
            error_dict = dict(user_login_form.errors.items())
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'success': False, 'message': error_dict})


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
