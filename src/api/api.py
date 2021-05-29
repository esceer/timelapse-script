import os

from bottle import Bottle, static_file

from config.config import Config
from utils.cron_utils import CronTab
from utils.timelapse import TimelapseEngine


def make_wsgi_app(config: Config, cron_tab: CronTab):
    app = Bottle()

    @app.get('/timelapse/start')
    def schedule_timelapse_handler():
        cron_tab.setup_timelapse_cron_jobs()
        return 'Scheduled.'

    @app.get('/timelapse/stop')
    def unschedule_timelapse_handler():
        cron_tab.truncate_cron_jobs()
        return 'Unscheduled.'

    @app.get('/timelapse/snapshot')
    def take_picture_handler():
        with TimelapseEngine(config.get_output_directory(),
                             config.get_resolution_width(),
                             config.get_resolution_height(),
                             config.get_num_of_ramp_frames()) as timelapse_engine:
            directory_path, filename = timelapse_engine.save_image()
            return static_file(filename, root=os.path.abspath(directory_path))

    return app
