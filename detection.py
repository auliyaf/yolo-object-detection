import cv2
from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

# Define path to the image file
source = 'test/1.jpg'

# Run inference on the source
results = model(source)  # list of Results objects

# Load the image
image = cv2.imread(source)

# Iterate over the detected results
for result in results:
    # Iterate over each detection in the result
    for box, conf, cls in zip(result.boxes.xyxy, result.boxes.conf, result.boxes.cls):
        # Convert box coordinates to integers
        box = [int(coord) for coord in box]
        
        # Draw bounding box rectangle
        cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
        
        # Put text showing class and confidence score
        text = f'{model.names[int(cls)]}: {conf:.2f}'
        cv2.putText(image, text, (box[0], box[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Save the annotated image to a file
output_path = 'output/annotated_image.jpg'
cv2.imwrite(output_path, image)

print(f"Annotated image saved to '{output_path}'.")
