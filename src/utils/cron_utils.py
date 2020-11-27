import os


class CronTab:
    def __init__(self, schedule_interval_regex: str):
        timelapse_script_path = os.path.abspath('../bin/run_timelapse.sh')
        self._cron_entry = f'{schedule_interval_regex} {timelapse_script_path}'

    def setup_timelapse_cron_jobs(self):
        os.system(f'echo "{self._cron_entry}" | crontab -u pi -')

    @staticmethod
    def truncate_cron_jobs():
        os.system(f'echo "" | crontab -u pi -')
