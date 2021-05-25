
import PIL
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.abspath("./mountedversion/env.json")

def implicit():
    from google.cloud import storage

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client()

from PIL import Image

def detect_labels_uri(uri):
    """Detects labels in the file located in Google Cloud Storage or on the
    Web."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri
    print(uri)

    # newimage = Image.open(image)
    # newimage.show()
    # os.system(uri)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        print(label.description)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

detect_labels_uri('https://picsum.photos/200/300.jpg')
# print(detect_labels_uri)