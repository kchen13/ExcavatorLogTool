from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Open Gui for file selection
print('Select log file')
Tk().withdraw()
filename = askopenfilename()
print(filename)

# Create clean log which includes speed, accepted, rejected
clean = open(filename[:-4] + '_clean.log', "w+")
print(filename[:-4] + '_clean.log has been created.')

# Sub strings to search for in lines
statString = 'speed:'
acceptedString = 'accepted'
rejectedString = 'rejected'

# Initialize count and tallies
statCounts = 0
speedTally = 0
powerTally = 0
efficiencyTally = 0
rejectedTally = 0
acceptedTally = 0
pingTally = 0

with open(filename, 'r') as log:
    for line in log:
        add = False
        if statString in line:
            add = True
            statCounts += 1
            # Average Speed
            strSpeed = slice(56, 64)
            speedTally += float(line[strSpeed])
            # Average Power
            strPower = slice(78, 86)
            powerTally += float(line[strPower])
            # Average Efficiency
            strEfficiency = slice(103, 111)
            efficiencyTally += float(line[strEfficiency])
        if acceptedString in line:
            add = True
            # Accepted Ping in ms
            x = line.find("accepted (")
            acceptedTally += float(line[x + 10:-4])
            pingTally += 1
        if rejectedString in line:
            add = True
            rejectedTally += 1
        if add:
            clean.write(line)

    # Print Out
    print('Avg Speed: ', round(speedTally / statCounts, 2), ' MH/s')
    print('Avg Power: ', round(powerTally / statCounts, 2), ' W')
    print('Avg Efficiency:', round(efficiencyTally / statCounts, 2), 'kH/J')
    print('Avg Ping: ', round(acceptedTally / pingTally), 'ms')
    print('Total Rejected: ', rejectedTally)
