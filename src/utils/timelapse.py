import os
from datetime import datetime

import cv2


class TimelapseEngine:
    def __init__(self, output_directory: str):
        self._cap = cv2.VideoCapture(0)

        os.makedirs(output_directory, exist_ok=True)
        self._timelapse_directory = output_directory

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._cap.release()

    def save_image(self):
        target_image_path = self._generate_target_image_path()
        _, captured_image = self._cap.read()
        cv2.imwrite(target_image_path, captured_image)
        return os.path.split(target_image_path)

    def _generate_target_image_path(self) -> str:
        target_image_name = f'timelapse-{datetime.now().strftime("%Y%m%d%H%M%S")}.jpg'
        return os.path.join(self._timelapse_directory, target_image_name)


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print('Invalid arguments')
        print('Usage:')
        print('timelapse.py <timelapse_output_directory>')
        sys.exit(1)

    timelapse_directory = sys.argv[1]

    with TimelapseEngine(timelapse_directory) as timelapse_engine:
        timelapse_engine.save_image()
