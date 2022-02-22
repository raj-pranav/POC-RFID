
import rdm6300
import time


# log = logging.getLogger("RFID.Reader")


def read_live_tags(timeout_s):
    
    Total_tags_found = []    # to store all RFid value during current read
    set_timeout = timeout_s  # in second
    start_time = time.time()
    
    RFid_reader = rdm6300.Reader('/dev/ttyS0')
    print(f"Start of RFid Read for [{set_timeout}s]... ")
    
    while (time.time() < (start_time+set_timeout)) :
        curr_card = RFid_reader.read(timeout = 3.0)
        Tag_id = str(curr_card.value)
        # print (f"Started at {start_time} and current time is {time.time()}")
        
        if Tag_id not in Total_tags_found:
            Total_tags_found.append(Tag_id)
            print (f"Current Tag id: {Tag_id}")
     
    
    return Total_tags_found

