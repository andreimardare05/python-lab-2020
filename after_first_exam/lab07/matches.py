import sys

def process_files(team1, team2, times):
    import os
    if not (os.path.exists(team1) and os.path.exists(team2) and os.path.exists(times)):
        return None

    fd_team1 = open(team1,"r")
    fd_team2 = open(team2,"r")
    fd_time = open(times,"r")

    first_list = []
    second_list = []
    times = []

    text = fd_team1.readline()
    while text:
        text = text.replace("\n","")
        first_list.append(text)
        text = fd_team1.readline()

    text = fd_team2.readline()
    while text:
        text = text.replace("\n","")
        second_list.append(text)
        text = fd_team2.readline()
    
    text = fd_time.readline()
    while text:
        text = text.replace("\n","")
        times.append(text)
        text = fd_time.readline()

    import random

    random.shuffle(times)
    random.shuffle(first_list)
    random.shuffle(second_list)

    return list(zip(first_list, second_list, times))

import sys
fd = open('output.txt',"w")

fd.write(str(process_files(sys.argv[1],sys.argv[2],sys.argv[3])).replace(",","\n"))