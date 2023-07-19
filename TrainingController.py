from ultralytics import YOLO

def ValidParam(param):
    modelName = modelName or 'yolov8m.pt'
    epochs = epochs or 5
    save = save or False
    device = device or 'cpu'
    optimize = optimize or 'auto'
    return param 

def TrainYOLOv8Controller(
        modelName,
        epochs,
        save,
        device,
        optimize,      
        dataYaml
):
    if(dataYaml is None):
        return "data yaml is required !!!"
    # Load a model
    model = YOLO(modelName) # pretrained YOLOv8n model

    history = model.train(
        data="data.yaml", 
        epochs=epochs, 
        save=save, 
        device=device, 
        optimize=True
    )

    print("History Information: ", history)
    return "Train Done"