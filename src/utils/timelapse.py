import os
from datetime import datetime

import cv2


class TimelapseEngine:
    def __init__(self, output_directory: str, resolution_width: int = 1920, resolution_height: int = 1088):
        self._cap = cv2.VideoCapture(0)
        self.set_resolution(resolution_width, resolution_height)

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

    def set_resolution(self, width: int, height: int):
        # The resolution must be power of 32 in order to preserve color balance
        # otherwise it gets blueish. Related stack overflow thread:
        # https://stackoverflow.com/questions/60989671/white-blue-balance-error-in-high-resolution-with-opencv-and-picamera-v2
        self._cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self._cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def _generate_target_image_path(self) -> str:
        target_image_name = f'timelapse-{datetime.now().strftime("%Y%m%d%H%M%S")}.jpg'
        return os.path.join(self._timelapse_directory, target_image_name)


if __name__ == '__main__':
    import sys

    if len(sys.argv) not in (2, 4):
        print('Invalid arguments')
        print('Usage:')
        print('timelapse.py <timelapse_output_directory> [<resolution_width> <resolution_height>]')
        sys.exit(1)

    timelapse_directory = sys.argv[1]

    with TimelapseEngine(timelapse_directory) as timelapse_engine:
        if len(sys.argv) is 4:
            res_width = int(sys.argv[2])
            res_height = int(sys.argv[3])
            timelapse_engine.set_resolution(res_width, res_height)
        timelapse_engine.save_image()
