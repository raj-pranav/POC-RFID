
import rdm6300
import time

# Read rfid from environment
# start -> with function call
# end   -> after a set timeout (30s)

# log = logging.getLogger("RFID.Reader")

Total_tags_found = [] # to store all RFid value during current read
set_timeout = 20  # in second
start_time = time.time()

RFid_reader = rdm6300.Reader('/dev/ttyS0')

print(f"Start of RFid Read for [{set_timeout}s]... ")
while (time.time() <= (start_time+set_timeout)) :
    curr_card = RFid_reader.read()
    Tag_id = curr_card.value
    
    if Tag_id not in Total_tags_found:
        Total_tags_found.append(Tag_id)
        print (f"Current Tag id: {Tag_id}")

print (f"Total {len(Total_tags_found)} Tags found >> {Total_tags_found}")

