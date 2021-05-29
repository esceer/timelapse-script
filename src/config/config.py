import configparser


class Config:
    def __init__(self):
        self._config_file_path = '../resources/tls.ini'
        self._config = self._parse_config_file()

    def get_server_port(self) -> str:
        return self._config['Server']['port']

    def get_output_directory(self) -> str:
        return self._config['Timelapse']['output-directory']

    def get_resolution_width(self) -> int:
        return int(self._config['Timelapse']['resolution-width'])

    def get_resolution_height(self) -> int:
        return int(self._config['Timelapse']['resolution-height'])

    def get_num_of_ramp_frames(self) -> int:
        return int(self._config['Timelapse']['number-of-ramp-frames'])

    def get_schedule_interval_regex(self) -> str:
        return self._config['Schedule']['interval-regex']

    def _parse_config_file(self) -> configparser.ConfigParser:
        config = configparser.ConfigParser()
        config.read(self._config_file_path)
        return config
