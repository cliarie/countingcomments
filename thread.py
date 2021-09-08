##thread.py
# Class to represent a comment thread. Because comment thread is not fixed length, we want to use a more complex
# structure than just list.

# USING TIME/DATE TO TO FIND START END
# new suggestion format: name, name, time + date, suggestion, your name
# new comment format: "Selected text", "|", selected text, name, name, time + date, comment,..., your name

class Thread():

    def __init__(self):
        self.selected = ""
        self.comments = []
        self.users = []
        self.times = []

    def contains_time(self, s):
        if s.find(":") >= 0 and (s.find("AM") >= 0 or s.find("PM") >= 0):
            return True
        return False

    def isEmpty(self):
        return self.comments == 0

    # Update function. Just making the code cleaner
    def update(self, name, date, comment):
        self.users.append(name)
        self.times.append(date)
        self.comments.append(comment)

    def get_times(self):
        return self.times

    def get_comments(self):
        return self.comments
    def get_users(self):
        return self.users
    def get_selected(self):
        return self.selected
    def get_time_for_name(self, name):
        total = []
        # 1 for comment, 0 for reply
        comment = []
        for i in range(len(self.users)):
            if self.users[i] == name:
                if i == 0:
                    comment.append(1)
                else:
                    comment.append(0)
                total.append(self.times[i])
        return total, comment

    # To string for printing
    def to_string(self):
        print(self.selected)
        print(self.users)
        print(self.comments)
        print(self.times)

    # Processing function. Input, the relevant text string, split into array by newlines ("\n")
    # Using a pin, go through each of the elements of the array subject to certain search conditions.
    # For first entry of each thread, date shows up on top.
    def process_text(self, contents):
        pin = 0
        name = contents[0]
        date = contents[1]
        pin = 2

        # Fish for the first comment, it could have multiple lines! (NEW: ONLY 1 LINE)
        # End codes: line after string with time + date
        comment = contents[pin]
        # Peek at the next object
        while pin + 2 < len(contents) and not self.contains_time(contents[pin + 2]):
            pin = pin + 1
            comment += contents[pin]
        self.update(name, date, comment)
        # Now we need a while loop because we do not know size and input is inconsistent
        # if contents[-1] == "Reply or add others with @":
        #     contents = contents[:len(contents) -2]
        while pin + 3 < len(contents) :
            pin += 1
            if not self.contains_time(contents[pin]):
                continue
            date = contents[pin]
            name = contents[pin - 1]
            comment = contents[pin+1]

            while pin + 2 < len(contents) and not self.contains_time(contents[pin + 2]):
                pin += 1
                comment += contents[pin]
            #resolve and re-opening do not count
            if comment not in ['Marked as resolved', 'Re-opened']:
                self.update(name, date, comment)