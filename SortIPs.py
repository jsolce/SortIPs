# Sorting a list of IPs from a file
# Assumed input has 1 IP per file, good data
# Jim Solce, 19 Nov 2019

import sys
import random

filename = ""

# Grab the filename. Also supp
if (len(sys.argv) == 2):
    filename = sys.argv[1]
else:
    print("Please enter a filename or use -g to generate a test file")
    sys.exit()

if filename == "-g":
    with open("./generatedIPs.txt", 'w') as file:
        cnt = 0
        while cnt < 1000:
            file.write(str(random.randint(1,255)) + '.' + str(random.randint(1,255)) + '.'
                       + str(random.randint(1,255)) + '.' + str(random.randint(1,255)) + '\n')
            cnt = cnt  + 1
    sys.exit()

# List to hold out IPs
ipList = []

# Open the file
with open(filename, 'r') as file:
    # Pull in the IP, drop the newline
    line = file.readline().strip()
    while line:
        # Split the IP into each octet
        ip = line.split('.')
        # Because there's only 4 octets, not trying anything fancy here
        # Nede to cast to ints for proper sorting
        ip[0] = int(ip[0])
        ip[1] = int(ip[1])
        ip[2] = int(ip[2])
        ip[3] = int(ip[3])
        ipList.append(ip)
        # Grab the next line and drop the newline
        line = file.readline().strip()

# Python's built in sorting
ipList.sort()

# Lastly, loop through and print this pretty.
for ip in ipList:
    print(str(ip[0]) + '.' + str(ip[1]) + '.' + str(ip[2]) + '.' + str(ip[3]));



