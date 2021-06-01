from claas.src.config import Configurable


class Config(Configurable):
    def __init__(self, config_file: str = None):
        self.log_dir = None
        self.default_log = None
        self.search = None
        self.images = None
        self.output_dir = None
        self.exceptions = {}
        super().__init__(config_file)
