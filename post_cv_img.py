#!/usr/bin/env python2
# Using Python 2
import json
import cv2 # opencv3
from datetime import datetime
import requests

class CVMatFile:
    def __init__(self, mat_img, encoding='.jpg'):
        self._img = mat_img
        self._encoding = encoding

    def read(self):
        _, buffer = cv2.imencode(self._encoding, self._img)
        return buffer

def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in 
    this function because it is programmed to be pretty 
    printed and may differ from the actual request.
    """
    print('{}\n{}\n{}\n\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))

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
        'image': ('filename', CVMatFile(mat_img), 'image/jpeg')
    }
    r = requests.post(url, files=files)
    print(r.content)

# To Rails basic http auth
def publish_json_with_cv_mat_with_auth(data, mat_img, url, api_key):
    files = {
        'json': (None, json.dumps(data), 'application/json'),
        'image': ('filename', CVMatFile(mat_img), 'image/jpeg')
    }
    req = requests.Request('POST', url, files = files).prepare()
    req.headers['Authorization'] = 'Token token=' + api_key
    s = requests.Session()
    s.send(req)

if __name__ == '__main__':
    img_mat = cv2.imread('example.jpg',cv2.IMREAD_COLOR)
    data = {'license_plate': 'W400M', 'camera_id': '12345', 'local_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S') }
    # publish_json_with_cv_mat(data, img_mat ,'http://localhost:3000/api/publish_license')
    publish_json_with_cv_mat_with_auth(data, img_mat, 'http://localhost:3000/api/publish_license', '123fasdf')
    print "Procedure Done!"

