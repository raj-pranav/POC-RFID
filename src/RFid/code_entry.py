from os import getcwd
from pathlib import Path
import logging

from RFid.logging_setup import setup_log
from RFid.pi_board.DB import update_db

# Path configuration
PROJECT_PATH = getcwd()
source_dir   = Path(PROJECT_PATH).parent

setup_log(source_dir)

# Logger for this module
log = logging.getLogger('RFID')

log.info(f'PROJECT Path : {PROJECT_PATH}')
log.info(f'Source Path  : {source_dir}')

# Read rfid from environment

# Call to Database
update_db(source_dir)

#
