from abc import ABCMeta


class AppContextAbc:

    __metaclass__ = ABCMeta

    def __init__(self, ui_config, **kwargs):
        self.ui_config = ui_config
        self.user_input_events = {}
        self.update_data = {}

    def set_update_data(self, data_key, data):
        self.update_data[data_key] = data


