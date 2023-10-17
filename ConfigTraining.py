'''
# model: path to model file (eg: yolov8n.pt, yolov8n.yaml)

# epochs: number of epochs to train for (eg: 1, 2, 3, ...)

# save: save train checkpoints and predict results (eg: True, False)

# device: device to run on (eg: cuda device=0 or device=0,1,2,3 or device=cpu)

# data: path to data file (eg: coco128.yaml)

# patience: epochs to wait for no observable improvement for early stopping of training (eg: 3, 5, 10, ...)

# save_period: save checkpoint every x epochs (disabled if < 1)

# optimizer: optimizer to use, choices=[SGD, Adam, Adamax, AdamW, NAdam, RAdam, RMSProp, auto]
'''


YoloV8TrainModel = dict(
    model= "yolov8m.pt"
)



YoloV8Train = dict(
    epochs= 2,
    save= True,
    device= 0,
    data= 'data.yaml',
    patience= 5,
    save_period = 10,
    optimizer= 'auto'
)

# YoloV8TrainJSON = {
#     "epochs": 2,
#     "save": "True",
#     "device": 0,
#     "optimize": "auto",
#     "data": "data.yaml",
#     "patience": "5",
#     "save_period": "10",
#     "optimizer": "auto"
# }