# Machine Learning Model Deployment with Docker

This repository contains the code and instructions for deploying a machine learning model on different compute environments using Docker. The solution demonstrates deploying a YOLOv8n model from Ultralytics for object detection.

## Steps

### 1. Model Inference
- The initial step involved creating an inference script (`detection.py`) to run object detection using the YOLOv8n model provided by Ultralytics. 
- The script takes an input image from the `test` folder and outputs the detected objects to the specified output path.

### 2. Adding Interface with Gradio
- To improve user interaction, I implemented a simple web interface using Gradio in `app.py`.
- Gradio provides a convenient way to create interfaces for machine learning models and allows users to interact with the model via a web browser.
- The interface can be accessed locally at `http://localhost:7860`.

### 3. Dockerization
- Dockerizing the application involved creating a `Dockerfile` in the root directory of the project.
- I chose the base image `python:3.10.12-slim` as it provides a lightweight Python environment.
- Additional dependencies required by the model and application, such as `ffmpeg` and `libsm6`, were installed using `apt-get`.
- The code and necessary files were copied into the Docker container, and the required Python packages were installed using `pip`.
- Port `7860`, used by Gradio, was exposed to allow external access.
- Environment variables were set to configure Gradio to listen on `0.0.0.0`.
- Finally, the command to start the Gradio server was specified as the default command to run when the container starts.

#### Dockerfile:
```dockerfile
FROM python:3.10.12-slim
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y gcc
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 7860
ENV GRADIO_SERVER_NAME="0.0.0.0"
CMD ["python", "app.py"]
```

### 4. Building the Docker Image
To build the Docker image, run the following command in the terminal:
```bash
docker build -t ml-model-deployment .
```

### 5. Running the Docker Container
To run the Docker container, execute the following command:
```bash
docker run -p 7860:7860 ml-model-deployment
```

### Test Data and Models
You can use image I provide on gradio or just input any image on gradio interface and set the Confidence and IoU threshold

### Testing the Solution 
[![Watch the video](https://img.youtube.com/vi/Dt5taTKFw8k/0.jpg)](https://youtu.be/Dt5taTKFw8k)

To verify the correctness and efficiency of the solution:

- Unit & Integration Testing: Test individual components and their integration to ensure functionality.
- Performance Testing: Evaluate inference time, resource utilization, and interface responsiveness.
- Input Variation: Validate solution with diverse inputs to cover various scenarios.

Achieving a 0.02-second inference time on Gradio indicates excellent performance, reflecting efficient processing and responsiveness.

To optimize the solution:

- Model & Code Optimization: Explore techniques to enhance YOLOv8 and code efficiency.
- Infrastructure Fine-tuning: Optimize Docker setup (CPU/GPU) to minimize overhead.

### Bonus Points
- The Docker image created in this solution can run the code on both CPU and GPU environments execution. However,this project still isn't optimized for GPU environments.
- Automation of deployment on a VM or remote server can be achieved using container orchestration tools like Kubernetes or Docker Swarm.
