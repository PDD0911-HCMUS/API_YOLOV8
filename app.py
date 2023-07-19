import numpy as np
from flask import Flask, request
import io as ioIm
import numpy as np
import skimage.transform as trans
from PIL import Image
from flask_cors import CORS
from ObjectDetectionController import Detect_YOLOV8_Controller
from TrainingController import TrainYOLOv8Controller

app = Flask(__name__)
app.config["DEBUG"] = True
# app.config['CORS_HEADERS'] = 'Content-Type'
app.config["ENV"] = "production"
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/Detect_YOLOV8_Controller', methods=['POST'])
def Detect_YOLOv8_Controller():
    try:
        file = request.files['image']
        image_bytes = file.read()
        img = np.array(Image.open(ioIm.BytesIO(image_bytes)))

        print('ok load image')

        responseYOLOv8 = Detect_YOLOV8_Controller(img)

        print('ok responseYOLOv8')

        return {'result': responseYOLOv8}
    
    except Exception as e:
        return {'result': e}


@app.route('/Training_YOLOV8_Controller', methods=['POST'])
def Training_YOLOv8_Controller():
    param = request.get_json()
    print(param)
    modelName = param["modelName"]
    epochs = param["epochs"]
    save = param["save"]
    device = param["device"]
    optimize = param["optimize"]      
    dataYaml = param["dataYaml"]

    if save == 'True':
        save = True
    else:
        save = False

    responseYOLOv8 = TrainYOLOv8Controller(
                        modelName,
                        epochs,
                        save,
                        device,
                        optimize,      
                        dataYaml)

    return {'result': responseYOLOv8}
    
if __name__ == '__main__':
    with app.app_context():
        app.run()