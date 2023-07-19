# API_YOLOV8

## This is tutorial for setting up and using API of YOLOv8

NOTE: Please install **Python** with version >= 3.8 (3.8.10 is recommendation) and **Postman** for executing API.

## Setup Source Code

Please install all Librabries by command: `pip install -r requirements.txt`.

Then run source by command: `python app.py`.

If console is displayed like the image below. It's mean that setup source code successfully.

![image](https://github.com/PDD0911-HCMUS/API_YOLOV8/assets/70840713/f6413cca-5abd-4e0d-9f69-d501c9994f1c)

## Detection Task

URL: `http://127.0.0.1:5000/Detect_YOLOV8_Controller`

Method: `POST`

### Step-1
Please setup Postman like the image below. At the `Key` please choose type is `File`.

![image](https://github.com/PDD0911-HCMUS/API_YOLOV8/assets/70840713/7efba676-19c8-4b36-8a4b-d23763e1bbb7)

### Step-2

Upload the image by press on `Select Files` at the `Value` (Please look at image in step-1). Then press `Send` button to execute API, it will take a several time.

![image](https://github.com/PDD0911-HCMUS/API_YOLOV8/assets/70840713/77d01b3e-73de-4931-9090-497a68994732)

> **Response Example**

```
{
  "result": [
        {
            "Coordinates": [
                102,
                246,
                178,
                406
            ],
            "ObjectType": "vase",
            "Probability": 0.9
        },
    [
}
```

> **Response Data**

| Field | Description |
|--------------|-------|
| result | a list of all objects that detected by API|
| Coordinates | Coordinates of an object |
| ObjectType| Name class of object |
| Probability | Probability of object|

## Training Task

> **Prepare Data**

These are the steps that you need to follow to create each of the datasets:

- Decide on and encode classes of objects you want to teach your model to detect. For example, if you want to detect only cats and dogs, then you can state that "0" is cat and "1" is dog.
- Create a folder for your dataset and two subfolders in it: "images" and "labels".
- Add the images to the "images" subfolder. The more images you collect, the better for training.
- For each image, create an annotation text file in the "labels" subfolder. Annotation text files should have the same names as image files and the ".txt" extensions. In the annotation files you should add records about each object that exist on the appropriate image in the following format:

`{object_class_id} {x_center} {y_center} {width} {height}`

The final folder structure can look like (please ignore file `labels.cache`).

![image](https://github.com/PDD0911-HCMUS/API_YOLOV8/assets/70840713/54dd2381-323a-458f-9913-424e0d230018)

Finally, you need to create a dataset descriptor YAML-file that points to the created datasets and describes the object classes in them. This is a sample of this file for the data created above:

```
datasets_dir: /media/pdd/PDD/API_YOLOV8/datasets
weights_dir: weights
runs_dir: runs
uuid: 19f4b7bdcb6de76c106d3753782f8d8cc0eb21b16998e748572382f5d626ba28
sync: true
api_key: ''
settings_version: 0.0.3
```
You can use this GoogleDrive to get example data with the format has been created after unzip.

**Note: change the content in file  `data.yaml` like the content above**

https://drive.google.com/file/d/1PNktsghBqIJVgxa-34FqO3yODNJbH3B0/view

Please setup the tree folder like image below.

![image](https://github.com/PDD0911-HCMUS/API_YOLOV8/assets/70840713/173ae7f7-43d2-4cf2-9aba-0d2ffb1cfda7)

> **Postman Config**

URL: `http://127.0.0.1:5000/Training_YOLOV8_Controller`

Method: `POST`

![image](https://github.com/PDD0911-HCMUS/API_YOLOV8/assets/70840713/01c8ba05-c0cc-46ff-a388-0cdce87f09e5)


> **Example request**

```
{
    "modelName": "yolov8m.pt",
    "epochs": 2,
    "save": "False",
    "device": 0,
    "optimize": "auto",
    "dataYaml": "data.yaml"
}
```

> **Parameters**

| Field | Description |
|--------------|-------|
| modelName | Model pretrain |
| epochs | Number of epochs |
| save| Save model |
| device | Device for training (CPU or GPU) |
| optimize | Optimization of model |
| dataYaml | path to file `data.yaml` |

> **Execute API**

Please press `Send` button to execute API, it will take a several time.

Choose option `3` and wait for processing of training task complet.

![image](https://github.com/PDD0911-HCMUS/API_YOLOV8/assets/70840713/2f207d0b-3020-498a-8812-d034b9374df2)

Atfer training task pleae take attion to the line `Results saved to runs/detect/trainXX`. That is direction saving the model.

![image](https://github.com/PDD0911-HCMUS/API_YOLOV8/assets/70840713/47d77810-8bc3-4347-9fe4-75c097c21afd)

The respone data of API after executed.

![image](https://github.com/PDD0911-HCMUS/API_YOLOV8/assets/70840713/466f0ce4-04c0-48cf-85b4-80573f7cbebb)


