# say if a folder exist
import os
dire="/Users/mp0644/PycharmProjects/bills-organizer/billanos"
if not os.path.exists(dire):
    os.makedirs(dire)