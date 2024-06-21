from flask import Flask, render_template, send_from_directory
import os
import threading
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    # List images in static folder
    images = os.listdir('yolov5/runs/detect')
    return render_template('index.html', images=images)

@app.route('./yolov5/runs/detect/<path:filename>')
def static_files(filename):
    return send_from_directory('yolov5/runs/detect', filename)

def run_detection():
    # Run detect.py with specified parameters
    subprocess.run(['python3', 'yolov5/detect.py', '--weights', 'close_stairs.pt', '--img', '416', '--conf', '0.73', '--source', 'videos/20240130_154336.mp4' ])

if __name__ == '__main__':
    detection_thread = threading.Thread(target=run_detection)
    detection_thread.start()
    app.run(host='0.0.0.0', port=5000)