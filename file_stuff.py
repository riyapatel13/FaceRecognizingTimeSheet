from datetime import datetime
import json

target = "Ruchi"

# beg = datetime.datetime.now()
with open("timesheet.txt", "r") as text:
    # read file
    lines = text.readlines()
    entry = {}
    # read backwards because thats the last time file would have been edited
    for line in reversed(lines):
        print("line: ",line)

        # convert to JSON object
        entry = None
        try:
            entry = json.loads(line)
            print(entry)
        except:
            continue
        
        # first read time sheet and check if person is in timesheet at all
        if entry != None:
            if entry['person'] == target:
            # if in time sheet, check if person is in timesheet at all signing in or out
                if 'time out' in entry.keys():
                    # if out exists, then sign in
                    # new_entry(target, time)
                    pass
                else:
                    # if there is an in without an out, then sign out and calculate difference
                    # update_entry(target, time)
                    time_in_str = entry['time in']
                    time_in_obj = datetime.strptime(time_in_str, "%Y-%m-%d %H:%M:%S.%f")

                    time_out_obj = datetime.now()
                    entry['time out'] = str(time_out_obj)
                    entry['time diff'] = str(time_out_obj - time_in_obj)
                    with open("timesheet.txt", "a") as write_file:
                        write_file.write(json.dumps(entry))
                        write_file.write("\n")

                    break
            
        
    # person not in timesheet - sign in
    # new_entry(target, time)

# end = datetime.datetime.now()
# print("diff: ", end-beg)