from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Notes
from .serializers import NoteSerializer
# Create your views here.
@api_view(['GET'])
def getApi(request):
    notes = Notes.objects.all()
    # print(notes,'hi')
    serializer = NoteSerializer(notes,many=True)
    # print(serializer.data,'ok=ok=ok')
    return Response(serializer.data)
    # return Response(['hi','hello'])


@api_view(['GET', 'POST'])
def home(request):
    return Response("welcome home")


@api_view(['POST'])
def addNote(request):
    print(request.data)
    id = request.data.get("id")
    title = request.data.get('name')
    note = request.data.get('message')
    print(id,title,note)
    Notes(id=id,title=title,note=note).save()
    print(title)
    return Response("data saved successfully")

@api_view(['PUT'])
def deleteNote(request):
    print(request.data)
    id = request.data.get('id')
    record = Notes.objects.get(id=id)
    record.delete()
    return Response('Item Deleted Successfully!.. ')

@api_view(['PUT'])
def updateNote(request):
    print(request.data)
    if request.data != None:
        id = request.data.get('id')
        updatedNote = request.data.get('updatedNote')
        record = Notes.objects.get(id=id)
        record.note = updatedNote
        record.save()


    return Response('Item Updated Sucessfully...')
