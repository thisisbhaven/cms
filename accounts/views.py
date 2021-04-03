from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes

from accounts.models import Account
from accounts.serializers import RegistrationSerializer, AccountSerializer


class AccountList(APIView):
    def get(self, request, format=None):
        accounts = Account.objects.all()
        serializer = RegistrationSerializer(accounts, many=True)

        return Response(serializer.data)


@permission_classes([AllowAny, ])
class AccountRegister(APIView):
    def post(self, request, format=None):
        serializer = RegistrationSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['email'] = account.email
            data['username'] = account.username

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountDetail(APIView):
    def get_object(self, pk):
        try:
            return Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            raise Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        account = self.get_object(pk)
        serializer = AccountSerializer(account)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        account = self.get_object(pk)
        serializer = AccountSerializer(account, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        account = self.get_object(pk)
        account.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
