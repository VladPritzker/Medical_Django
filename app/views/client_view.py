from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models.clients import Client
from app.serializers.client_serializer import ClientSerializer
from django.shortcuts import get_object_or_404
import logging

logger = logging.getLogger(__name__)

class ClientRegisterView(APIView):
    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Client registered successfully: {request.data.get('email')}")
            return Response({'message': 'Client registered successfully!'}, status=status.HTTP_201_CREATED)
        logger.error(f"Client registration failed: {serializer.errors}")
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ClientListView(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ClientDetailView(APIView):
    def get(self, request, client_id):
        client = get_object_or_404(Client, pk=client_id)
        serializer = ClientSerializer(client)
        return Response(serializer.data, status=status.HTTP_200_OK)
