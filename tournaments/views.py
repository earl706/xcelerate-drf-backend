from django.shortcuts import render

from .models import Tournament
from .serializers import TournamentSerializer

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response

# Create your views here.


class TournamentListView(APIView):
    queryset = Tournament
    serializer_class = TournamentSerializer
    authentication_class = [JWTAuthentication]
    permission_class = [IsAuthenticated]

    def post(self, request):
        try:
            tournament_event = TournamentSerializer(data=request.data)
            if tournament_event.is_valid():
                tournament_event.save()
                return Response(tournament_event.data, statu=200)
        except ValueError:
            return Response({"error": "Bad request, value error"}, status=400)
