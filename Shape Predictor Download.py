import requests

# URL of the file you want to download
url = 'https://github.com/davisking/dlib-models/raw/master/shape_predictor_68_face_landmarks.dat.bz2'

# Download the file
response = requests.get(url)
with open('shape_predictor_68_face_landmarks.dat.bz2', 'wb') as f:
    f.write(response.content)
