from rest_framework.decorators import api_view
from rest_framework.response import Response
from project.models import Offer
from .serializers import OfferSerializer
from project.api import serializers



##  Routes that display the all offers or specific offer data  ##
@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/offers',
        'GET /api/offers/:id'
    ]
    return Response(routes)


@api_view(['GET'])
def getOffers(request):
    offers = Offer.objects.all()
    serializer = OfferSerializer(offers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getOffer(request, pk):
    offer = Offer.objects.get(id=pk)
    serializer = OfferSerializer(offer, many=False)
    return Response(serializer.data)