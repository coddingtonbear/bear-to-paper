import argparse
from getpass import getpass
import logging
import sys
from typing import List, Text

from .migrator import Migrator


def main(args: List[Text] = None):
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument('documents', nargs='+')
    parser.add_argument(
        '--upload-folder',
        default='Note Assets'
    )
    parser.add_argument(
        '--log-level',
        default='INFO'
    )
    options = parser.parse_args(args)

    root_logger = logging.getLogger('bear_to_paper')
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.getLevelName(options.log_level))
    root_logger.addHandler(stream_handler)
    root_logger.setLevel(logging.getLevelName(options.log_level))

    access_token = getpass(prompt="Dropbox Access Token: ")

    migrator = Migrator(options.documents, access_token, options.upload_folder)
    migrator.migrate()
