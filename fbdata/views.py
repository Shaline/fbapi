# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView, Response

from .serializers import UserListJsonSerializer, UserListCsvSerializer


class AddLabelJson(APIView):
    serializer_class = UserListJsonSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data)
