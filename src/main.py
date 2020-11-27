import os

import bottle

from api import api
from config.config import Config
from utils.cron_utils import CronTab

app = application = bottle.default_app()

SERVER_PORT = 8090

if __name__ == '__main__':
    config = Config()
    os.makedirs(config.get_output_directory(), exist_ok=True)
    cron_tab = CronTab(config)

    bottle.run(api.make_wsgi_app(config, cron_tab), host='0.0.0.0', port=config.get_server_port())
