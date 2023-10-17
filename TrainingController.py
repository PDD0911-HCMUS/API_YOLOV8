from ultralytics import YOLO
import ConfigTraining as cf

def ValidParam(param):
    modelName = modelName or 'yolov8m.pt'
    epochs = epochs or 5
    save = save or False
    device = device or 'cpu'
    optimize = optimize or 'auto'
    return param 

def TrainYOLOv8Controller(
):
    if(cf.YoloV8Train['data'] is None):
        return "data yaml is required !!!"
    # Load a model
    model = YOLO(cf.YoloV8TrainModel['model']) # pretrained YOLOv8n model
    print(cf.YoloV8Train.items())
    history = model.train(
        epochs= cf.YoloV8Train['epochs'],
        save= cf.YoloV8Train['save'],
        device= cf.YoloV8Train['device'],
        data= cf.YoloV8Train['data'],
        patience= cf.YoloV8Train['patience'],
        save_period = cf.YoloV8Train['save_period'],
        optimizer = cf.YoloV8Train['optimizer']
    )

    print("History Information: ", history)
    return "Train Done"