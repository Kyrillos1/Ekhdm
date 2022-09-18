from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import DemomethodSerializer
from demomethods.models import Demomethod, Review, Tag


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET': '/api/books'},
        {'GET': '/api/books/id'},
        {'POST': '/api/books/id/vote'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
    ]
    return Response(routes)


@api_view(['GET'])
def getDemomethods(request):
    demomethods = Demomethod.objects.all()
    serializer = DemomethodSerializer(demomethods, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getDemomethod(request, pk):
    demomethod = Demomethod.objects.get(id=pk)
    serializer = DemomethodSerializer(demomethod, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def demomethodVote(request, pk):
    demomethod = Demomethod.objects.get(id=pk)
    user = request.user.profile
    data = request.data

    review, created = Review.objects.get_or_create(
        owner=user,
        demomethod=demomethod,
    )

    review.value = data['value']
    review.save()
    demomethod.getVoteCount

    serializer = DemomethodSerializer(demomethod, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def removeTag(request):
    tagId = request.data['tag']
    demomethodId = request.data['demomethod']

    demomethod = Demomethod.objects.get(id=demomethodId)
    tag = Tag.objects.get(id=tagId)

    demomethod.tags.remove(tag)

    return Response('Tag was deleted!')
