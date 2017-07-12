from rest_framework import serializers
from rest_framework.generics import CreateAPIView

import utils


## Serializer
from client_authentication.models import APIClient


class ClientAccessTokenSerializer(serializers.Serializer):
    def create(self, data):
        """
        Handles the post data.
        """

        key = data.get('key')
        secret = data.get('secret')

        try:
            client = APIClient.objects.get(key=key, secret=secret)
            access_token, expires_on = utils.create_client_access_token(
                client.key, client.secret)

            data['access_token'] = access_token
            data['expires_on'] = expires_on

            return data
        except Exception as err:
            raise serializers.ValidationError(str(err))


## View
class GetClientAccessToken(CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = ClientAccessTokenSerializer