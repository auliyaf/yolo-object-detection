import PIL.Image as Image
import gradio as gr
import time

from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def predict_image(img, conf_threshold, iou_threshold):
    start_time = time.time()
    results = model.predict(
        source=img,
        conf=conf_threshold,
        iou=iou_threshold,
        show_labels=True,
        show_conf=True,
        imgsz=640,
    )
    end_time = time.time()
    inference_time = end_time - start_time
    print("Inference time:", inference_time, "seconds")

    for r in results:
        im_array = r.plot()
        im = Image.fromarray(im_array[..., ::-1])

    return im

iface = gr.Interface(
    fn=predict_image,
    inputs=[
        gr.Image(type="pil", label="Upload Image"),
        gr.Slider(minimum=0, maximum=1, value=0.25, label="Confidence threshold"),
        gr.Slider(minimum=0, maximum=1, value=0.45, label="IoU threshold")
    ],
    outputs=gr.Image(type="pil", label="Result"),
    title="Ultralytics Gradio",
    description="Upload images for inference. The Ultralytics YOLOv8n model is used by default.",
    examples=[
        ["test/1.jpg", 0.25, 0.45]
    ]
)

if __name__ == '__main__':
    iface.launch()