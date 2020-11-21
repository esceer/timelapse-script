import os
import sys


class TimelapseEngine:
    def __init__(self, output_directory: str):
        import cv2
        self._cap = cv2.VideoCapture(0)
        self._save_image_func = cv2.imwrite

        from datetime import datetime
        self._get_now = datetime.now

        os.makedirs(output_directory, exist_ok=True)
        self._timelapse_directory = output_directory

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._cap.release()

    def save_image(self):
        _, captured_image = self._cap.read()
        self._save_image_func(self._get_image_file_name(), captured_image)

    def _get_image_file_name(self) -> str:
        target_image_name = f'timelapse-{self._get_now().strftime("%Y%m%d%H%M%S")}.jpg'
        return os.path.join(self._timelapse_directory, target_image_name)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Invalid arguments')
        print('Usage:')
        print('timelapse.py <timelapse_output_directory>')
        sys.exit(1)

    timelapse_directory = sys.argv[1]

    with TimelapseEngine(timelapse_directory) as timelapse_engine:
        timelapse_engine.save_image()
