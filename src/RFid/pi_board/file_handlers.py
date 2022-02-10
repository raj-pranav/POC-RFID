from pathlib import Path
import logging

log = logging.getLogger('RFID.Tags')

def read_prev_data(location: Path):

    FILE_NAME = 'prev_state.txt'

    txt_file = Path(location) / FILE_NAME

    values = []
    with open(txt_file, 'r') as reader:
        next(reader) # skip the header row
        lines = [line.rstrip() for line in reader]
        
        for obj in lines:
            values.append(tuple(obj.split(',')))
            
    # print (values)
    return values


    
def read_tags_record(location: Path):

    FILE_NAME = 'tags_record_internal.txt'

    txt_file = Path(location) / FILE_NAME

    values = []
    with open(txt_file, 'r') as reader:
        next(reader) # skip the header row
        lines = [line.rstrip() for line in reader]
        
        for obj in lines:
            values.append(tuple(obj.split(',')))
            
    # print (values)
    return values


def read_curr_tags(location: Path):

    FILE_NAME = 'rfid_cache.txt'

    txt_file = Path(location) / FILE_NAME

    with open(txt_file, 'r') as reader:
        lines = [line.rstrip() for line in reader]
    
    log.info(f'{len(lines)} Tags found after Scanning: >> {lines}')
            
    # print (lines)
    return lines