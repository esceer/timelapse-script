import os


class CronTab:
    def __init__(self, schedule_interval_regex: str, output_directory: str,
                 resolution_width: int, resolution_height: int, number_of_ramp_frames: int):
        timelapse_script_path = os.path.abspath('../bin/run_timelapse.sh')
        parameters = f'{output_directory} {resolution_width} {resolution_height} {number_of_ramp_frames}'
        self._cron_entry = f'{schedule_interval_regex} {timelapse_script_path} {parameters}'

    def setup_timelapse_cron_jobs(self):
        os.system(f'echo "{self._cron_entry}" | crontab -u pi -')

    @staticmethod
    def truncate_cron_jobs():
        os.system(f'echo "" | crontab -u pi -')
