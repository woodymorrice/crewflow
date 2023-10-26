from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view
from rest_framework import status
from main.models import BlogPost
from .serializers import BlogItemSerializer


@api_view(['GET'])
def getData(request):
    # Get the 'id' query parameter from the request
    id = request.query_params.get('id', None)
    title = request.query_params.get('title', None)
    content_contains = request.query_params.get('content_contains', None)


    if id:
        try:
            # Filter the data by 'id' and retrieve the specific BlogPost
            item = BlogPost.objects.get(id=id)
            serializer = BlogItemSerializer(item)
            return Response(serializer.data)
        except BlogPost.DoesNotExist:
            # Handle the case where the specified 'id' does not exist
            return Response({'message': 'BlogPost not found'}, status=404)
    elif title:
        # Filter the data by 'title' and retrieve all matching BlogPosts
        items = BlogPost.objects.filter(title=title)

        if items:
            serializer = BlogItemSerializer(items, many=True)
            return Response(serializer.data)
        else:
            # Handle the case where no matching items were found
            return Response({'message': 'No BlogPosts found with the specified title'}, status=404)

    elif content_contains:
        # Filter the data by 'content' field that contains the specified string
        items = BlogPost.objects.filter(content__contains=content_contains)
        if items:
            serializer = BlogItemSerializer(items, many=True)
            return Response(serializer.data)
        else:
            # Handle the case where no matching items were found
            return Response({'message': 'No BlogPosts found with the specified content'}, status=404)
    else:
        # Return all BlogPost objects if nothing is provided
        items = BlogPost.objects.all()
        serializer = BlogItemSerializer(items, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def addPost(request):
    serializer = BlogItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteData(request, id):
    try:
        item = BlogPost.objects.get(id=id)
    except BlogPost.DoesNotExist:
        return Response({'message': 'BlogPost not found'}, status=status.HTTP_404_NOT_FOUND)

    item.delete()
    return Response({'message': 'BlogPost deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

