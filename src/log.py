import logging
import logging.handlers
import os
import config
 
handler = logging.handlers.WatchedFileHandler(
    os.environ.get("LOGFILE", config.log))
# formatter = logging.Formatter(logging.BASIC_FORMAT)
formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)
root = logging.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", config.log_level))
root.addHandler(handler)