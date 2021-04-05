import os
import sys
import logging
import logging.handlers
from pathlib import Path


class LoggerMgr(logging.Logger):
    def __init__(self, filename=None, open_file_log=True, file_log_level=logging.DEBUG,
                 open_stream_log=True, stream_log_level=logging.DEBUG, simple_mode=True):

        super(LoggerMgr, self).__init__('LogMgr')

        self.sep = " "
        self.max_bytes = 1024000 * 20
        self.max_count = 10

        self.default_log_path = "./logs/"

        self.open_file_log = open_file_log
        self.open_stream_log = open_stream_log

        self.file_log_level = file_log_level
        self.stream_log_level = stream_log_level

        self.simple_mode = simple_mode

        if filename is None:
            if not os.path.exists(self.default_log_path):
                os.mkdir(self.default_log_path)
            filename = self.default_log_path + os.path.basename(__file__).split(".")[0] + '.log'
        elif not os.path.exists(os.path.dirname(filename)):
            Path(os.path.dirname(filename)).mkdir(parents=True, exist_ok=True)
        self.filename = filename

        format_str = self.get_simple_format() if self.simple_mode else self.get_detail_format()
        formatter = logging.Formatter(format_str)

        if self.open_file_log:
            fh = logging.handlers.RotatingFileHandler(
                self.filename, maxBytes=self.max_bytes, backupCount=self.max_count, encoding="utf-8")
            fh.setLevel(self.file_log_level)
            fh.setFormatter(formatter)
            self.addHandler(fh)

        if self.open_stream_log:
            ch = logging.StreamHandler(sys.stdout)
            ch.setLevel(self.stream_log_level)
            ch.setFormatter(formatter)
            self.addHandler(ch)

    def get_simple_format(self):
        format_list = ['[%(asctime)s]', '[%(filename)s:%(lineno)d]', '[%(levelname)s]', '%(message)s']
        return self.sep.join(format_list)

    def get_detail_format(self):
        format_list = ['[%(asctime)s]', '[%(filename)s:%(lineno)d]',
                       '[process:%(process)s thread:%(thread)s]',
                       '[%(levelname)s]', '%(message)s']
        return self.sep.join(format_list)

    def set_basic_config(self, sep=" ", max_bytes=1024000 * 20, max_count=10, simple_mode=True):
        self.sep = sep
        self.max_bytes = max_bytes
        self.max_count = max_count
        self.simple_mode = simple_mode

    def set_file_config(self, open_file_log=True, file_log_level=logging.DEBUG):
        self.open_file_log = open_file_log
        self.file_log_level = file_log_level

    def set_stream_config(self, open_stream_log=True, stream_log_level=logging.DEBUG):
        self.open_stream_log = open_stream_log
        self.stream_log_level = stream_log_level


if __name__ == "__main__":
    log = LoggerMgr()
    log.info("hello logger")
