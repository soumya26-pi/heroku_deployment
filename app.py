from flask import Flask,request
from flask import Flask, request, jsonify
import numpy as np

import torch
import cv2
import time
import time
import numpy as np
model = torch.hub.load('ultralytics/yolov5', 'custom',path="yolov5s.onnx",force_reload=True)
classes = model.names
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print("\n\nDevice Used:",device)
print("-------------------------------------------")


def score_frame(frame):
        model.to(device)
        frame = [frame]
        results = model(frame)
        labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
        return labels, cord



app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/frame', methods=['POST'])
def predict():
    # if request.method=="POST":
    output=request.form.get("frame")
    result=score_frame(output)
    return jsonify({"frame":str(result)})
  




if __name__ == '__main__':
    app.run(debug=True)
