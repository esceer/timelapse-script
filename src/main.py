import bottle
import os

from api import api
from config.config import Config
from utils.cron_utils import CronTab

app = application = bottle.default_app()

if __name__ == '__main__':
    config = Config()
    os.makedirs(config.get_output_directory(), exist_ok=True)
    cron_tab = CronTab(config.get_schedule_interval_regex(), config.get_output_directory(),
                       config.get_resolution_width(), config.get_resolution_height(), config.get_num_of_ramp_frames())

    bottle.run(api.make_wsgi_app(config, cron_tab), host='0.0.0.0', port=config.get_server_port())
