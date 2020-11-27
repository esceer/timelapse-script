import os

from config.config import Config


class CronTab:
    def __init__(self, config: Config):
        timelapse_script_path = os.path.abspath('../../bin/run_timelapse.sh')
        output_directory_path = os.path.abspath(config.get_output_directory())
        self._cron_entry = f'{config.get_schedule_interval_regex()} {timelapse_script_path} {output_directory_path}'

    def setup_timelapse_cron_jobs(self):
        os.system(f'echo "{self._cron_entry}" | crontab -u pi -')

    @staticmethod
    def truncate_cron_jobs():
        os.system(f'echo "" | crontab -u pi -')
