import logging
import os

logging.basicConfig(format="%(levelname)s %(asctime)s %(name)s:%(message)s\n")


def get_child(*args, **kwargs):
    logger = logging.getLogger('Project')
    file_handle = logging.FileHandler('./logs/project.log')
    log_level_str = os.environ.get('LOG_LEVEL', 'info').upper()
    log_level = getattr(logging, log_level_str)
    logger.debug(f"util.log log_level == {log_level_str} ({log_level})")
    logger.addHandler(file_handle)

    out = logger.getChild(*args, **kwargs)
    out.setLevel(log_level)

    out.debug(f"calling logging.setLevel() to log_level == {log_level}")

    return out


main_logger = get_child('application')