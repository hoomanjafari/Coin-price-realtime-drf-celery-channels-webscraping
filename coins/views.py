import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .scraper import scrape

class CoinsPriceView(APIView):
    def get(self, request):
        coins = json.loads(scrape())
        if coins["message"]:
            if coins["message"] == "connection error":
                return Response({
                    "detail": coins.message, "status": coins.status
                }, status=status.HTTP_408_REQUEST_TIMEOUT)
            elif coins["message"] == "invalid url":
                return Response({
                    "detail": coins["message"], "error": coins["error"]
                }, status=status.HTTP_404_NOT_FOUND)
            elif coins["message"] == "network is weak":
                return Response({
                    "detail": coins["message"], "error":coins["error"]
                }, status=status.HTTP_400_BAD_REQUEST)
        return Response(coins, status=status.HTTP_200_OK)
