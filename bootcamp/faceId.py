import requests
import io
import sys
import os
import uuid
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

key = '346d220ffb134f7799e990e819b43951'
endPoint = 'https://cristianpalta.cognitiveservices.azure.com/'

face_client = FaceClient(endPoint, CognitiveServicesCredentials(key))

print("Estoy conectado")

simple_face_image_url = 'https://twitter.com/CristianPalta1/photo.'
simple_image_name = os.path.basename(simple_face_image_url)
detected_faces = face_client.face.detect_with_url(url= simple_face_image_url)

if not detected_faces:
    raise Exception('No enconre caras :(')
print('Encontre caras y su Id es: ', simple_image_name)



# for face in similar_face:
#     first_image_face_ID = face.face_id
#python faceId.py