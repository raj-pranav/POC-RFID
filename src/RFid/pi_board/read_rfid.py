from pathlib import Path
import rdm6300
import time
import logging

# Read rfid from environment
# start -> with function call
# end   -> after a set timeout (30s)

log = logging.getLogger("RFID.Reader")

Total_tags_found = [] # to store all RFid value during current read
set_timeout = 30  # in second
start_time = time.time()

RFid_reader = rdm6300.Reader('/dev/ttyS0')

print("Start of RFid Read  >> Please wait ...")
while (time.time() <= (start_time+set_timeout)) :
    card = RFid_reader.read()
    if card:
        print(f"[{card.value}] read card {card}")
        Total_tags_found.append(card)
    else:
        print ("No Tags found !!")

