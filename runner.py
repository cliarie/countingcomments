
import sys
import argparse
from thread import Thread
import time

# Helper: checks if a string is a time string
def contains_time(s):
    if s.find(":") >= 0 and (s.find("AM")>=0 or s.find("PM") >=0):
        return True
    return False

# Given a list of names, sort alpahbetically by last name.
# Assertion, names have 2+ words and "last name" is the very last word of the name.
def sort_alphabetical(l):
    l.sort(key = lambda s: s.split()[-1])
    return l

def read_path(path):
    threads = []
    contents = []
    with open(path, "r") as input:
        lines = input.readlines()
        markers = []
        lines = [x.replace("\n", "") for x in lines if x.find("\n")>=0]
        for i in range(len(lines)-1):
            if lines[i+1].find(lines[i]) >=0:
                lines[i+1] = lines[i+1].replace(lines[i], "")
                if contains_time(lines[i+1]):
                    lines[i+1] = lines[i+1]
                    markers.append(i)

    markers.append(len(lines))
    # will strike if EXACT match
    strikes = ["Suggestion accepted", "Suggestion rejected", "Add space", "Made a suggestion", "Marked as resolved"]
    # will strike if INCLUDES match
    inclusion_strikes = ["Delete:", "Add:", "Replace:"]
    for i in range( len(markers)-1):
        valid = True
        entry = lines[markers[i]:markers[i+1]]
        # Marked as resolved is ok, if there is also "re-opened"
        for e in entry:
            if e in strikes:
                valid = False

            for i in inclusion_strikes:
                if e.find(i) >=0:
                    valid = False
            # Dealing with the 'marked as resolved' case. If it is re-opened, we need to toggle it back to being 'valid'
            if e == "Re-opened":
                valid = True
        if valid:
            threads.append([x for x in entry if x != ""])


    return threads

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required = True, help = "location of the file")
    parser.add_argument('--names', action = 'store_true', help = "Lists all the names of students who commented, in alphabetical order by last name")
    parser.add_argument('--stats', action = 'store_true', help = "Shows all students in alphabetical order, with number of comments and number of replies")
    parser.add_argument('--verbose', metavar = "output", type = str, help = "Shows all students in alphabetical order, with sequenced list of each reply. \
                                                                            No reply contents. Writes it to an output file.")
    parser.add_argument('--cleaned', metavar = "output", type = str, help = "Writes to output file of the comments on the google doc, cleaned up from automated\
                                                                            messages")
    args = parser.parse_args()


    master = []
    threads = read_path(args.file)
    for i in range(len(threads)):
        t = Thread()
        t.process_text(threads[i])
        master.append(t)

    # Debug
    for thread in master:
        names = thread.get_users()
        comms = thread.get_comments()
    if args.names:
        names = []
        for thread in master:
            names = names + thread.get_users()
        names = list(set(names))
        print("Total " + str(len(names)) + " unique participants")
        print(sort_alphabetical(names))

    elif args.stats:
        names  = []
        for thread in master:
            names = names + thread.get_users()
        names = list(set(names))
        names = sort_alphabetical(names)
        comments = [0] * len(names)
        replies = [0] * len(names)
        # Loop through threads
        for thread in master:
            users = thread.get_users()
            for i in range(len(users)):
                if i == 0:
                    loc = names.index(users[i])
                    comments[loc] = comments[loc] + 1
                else:
                    loc = names.index(users[i])
                    replies[loc] = replies[loc] + 1
        print("Statistics of all students, with number of comments and replies.")
        print ('%-40s%-30s%-30s' % ("Name", "Number of Comments", "Number of Replies"))

        for i in range(len(names)):
            print ('%-40s%-30i%-30i' % (str(names[i]), comments[i], replies[i]))

    elif args.verbose:
        writer = open(args.verbose, "w")
        writer.write("List of all timestamps of comments for each student. Students sorted alphabetically and timestamps"\
                     + "sorted in reverse chronology.\n")
        names  = []
        for thread in master:
            names = names + thread.get_users()
        names = list(set(names))

        for name in names:
            times = []
            writer.write("NAME: " + name + "\n")
            for thread in master:
                if name in thread.get_users():
                    times = times + thread.get_time_for_name(name)
            ## Need to sort these before reporting
            temp = times.copy()
            for i in range(len(times)):
                if times[i].find(" (") >=0:
                    k = times[i].find(" (")
                    temp[i] = temp[i][:k]

            temp.sort(key = lambda x: time.strptime(x, "%I:%M %p %b %d"), reverse = True)
            for t in temp:
                writer.write(t + "\n")
        print("Output written to file " + args.verbose + ".")

    else:
        names  = []
        for thread in master:
            names = names + thread.get_users()
        names = list(set(names))
        names = sort_alphabetical(names)
        comments = [0] * len(names)
        replies = [0] * len(names)
        # Loop through threads
        for thread in master:
            users = thread.get_users()
            for i in range(len(users)):
                if i == 0:
                    loc = names.index(users[i])
                    comments[loc] = comments[loc] + 1
                else:
                    replies[loc] = replies[loc] + 1
        print("Statistics of all students, with number of comments and replies.")
        print ('%-40s%-30s%-30s' % ("Name", "Number of Comments", "Number of Replies"))

        for i in range(len(names)):
            print ('%-40s%-30i%-30i' % (str(names[i]), comments[i], replies[i]))

if __name__ == '__main__':
    main()