from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.pt') # pretrained YOLOv8n model

# Define path to the image file
# source = '000000004265.jpg'



# box = result.boxes[0]

# print("Object type:", box.cls)
# print("Coordinates:", box.xyxy)
# print("Probability:", box.conf)

# print(25 * '=')

# print("Object type:",box.cls[0])
# print("Coordinates:",box.xyxy[0])
# print("Probability:",box.conf[0])

# print(25 * '=')

# cords = box.xyxy[0].tolist()
# class_id = box.cls[0].item()
# conf = box.conf[0].item()
# print("Object type:", class_id)
# print("Coordinates:", cords)
# print("Probability:", conf)

# print(25 * '=')

# cords = box.xyxy[0].tolist()
# cords = [round(x) for x in cords]
# class_id = result.names[box.cls[0].item()]
# conf = round(box.conf[0].item(), 2)
# print("Object type:", class_id)
# print("Coordinates:", cords)
# print("Probability:", conf)

def Detect_YOLOV8_Controller(source):
  try:
    results = model.predict(source)
    result = results[0]
    responseYOLOv8 = []
    for box in result.boxes:
      class_id = result.names[box.cls[0].item()]
      cords = box.xyxy[0].tolist()
      cords = [round(x) for x in cords]
      conf = round(box.conf[0].item(), 2)
      print("Object type:", class_id)
      print("Coordinates:", cords)
      print("Probability:", conf)
      print("---")

      res = {
        "ObjectType": class_id,
        "Coordinates": cords,
        "Probability": conf
      }

      responseYOLOv8.append(res)

    return responseYOLOv8
  except Exception as e:
    print(e)