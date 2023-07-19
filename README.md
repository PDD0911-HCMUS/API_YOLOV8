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
