from rest_framework import viewsets
from disco_optico.serializers import ImageSerializer
from disco_optico.models import Image
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
# from firebase_admin import credentials, initialize_app, storage
import pyrebase

class ImageViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        firebaseConfig = {
            "apiKey": "AIzaSyA8g3WsotiCGR4fN1J54YiKLfLmEQHCtEg",
            "authDomain": "lasalle-2f485.firebaseapp.com",
            "databaseURL": "https://lasalle-2f485-default-rtdb.firebaseio.com",
            "projectId": "lasalle-2f485",
            "storageBucket": "lasalle-2f485.appspot.com",
            "serviceAccount": "firebase/serviceAccountKey.json"
        }

        firebase_storage = pyrebase.initialize_app(firebaseConfig)
        storage = firebase_storage.storage()

        storage.child("posts/35KCzS53lbfN541EdKWh/test").put("firebase/corazon.png")

        return Response(serializer.data['name'], status=status.HTTP_201_CREATED)