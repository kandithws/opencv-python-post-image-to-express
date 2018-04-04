#!/usr/bin/env python2
# Using Python 2
import json
import cv2 # opencv3
from datetime import datetime
import requests

class CVMatFileStub:
    def __init__(self, mat_img, encoding='.jpg'):
        self._img = mat_img
        self._encoding = encoding

    def read(self):
        _, buffer = cv2.imencode(self._encoding, img)
        return buffer
    

def publish_json_with_image(data, image_path, url):
    files = {
        'json': (None, json.dumps(data), 'application/json'),
        'image': ('filename', open(image_path,'rb'), 'image/jpeg')
    }
    r = requests.post(url, files=files)
    print(r.content)

def publish_json_with_cv_mat(data, mat_img, url):
    files = {
        'json': (None, json.dumps(data), 'application/json'),
        'image': ('filename',CVMatFileStub(mat_img), 'image/jpeg')
    }
    r = requests.post(url, files=files)
    print(r.content)


if __name__ == '__main__':
    img = cv2.imread('example.jpg',cv2.IMREAD_COLOR)
    data = {'license_plate': '6PYV308', 'camera_id': '12345', 'local_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S') }
    # publish_json_with_image(data, 'example.jpg' ,'http://localhost:3000/api/publish_license')
    publish_json_with_cv_mat(data, img, 'http://localhost:3000/api/publish_license')
    print "Procedure Done!"

