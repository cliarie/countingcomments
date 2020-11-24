##thread.py
# Class to represent a comment thread. Because comment thread is not fixed length, we want to use a more complex
# structure than just list.


class Thread():

    def __init__(self):
        self.selected = ""
        self.comments = []
        self.users = []
        self.times = []
        self.months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    def contains_time(self, s):
        for month in self.months:
            if s.find(month) >= 0 and s.find("20") >= 0:
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


    # Cleaning off some junk from the times
    def clean_dates(self):
        for i in range(len(self.times)):
            dot = self.times[i].find("•")
            if dot >=0:
                self.times[i] = self.times[i][:dot]
    # Processing function. Input, the relevant text string, split into array by newlines ("\n")
    # Using a pin, go through each of the elements of the array subject to certain search conditions.
    # For first entry of each thread, date shows up on top.
    def process_text(self, contents):
        pin = 0
        size = len(contents)
        name = contents[0]
        date = contents[1]
        if contents[2] == "SELECTED TEXT:":
            self.selected = contents[3]
            #starting pin on 4
            pin = 4
        else:
            pin = 2
        # Fish for the first comment, it could have multiple lines!
        # End codes: a string with Time, 'Reply•Resolve', 'Reply'
        comment = contents[pin]
        # Peek at the next object

        while contents[pin + 1] not in ["Reply•Resolve", "Reply"] and not self.contains_time(contents[pin + 1]):
            pin = pin + 1
            comment += contents[pin]
        self.update(name, date, comment)
        # Now we need a while loop because we do not know size and input is inconsistent
        if contents[-1] == "Reply or add others with @":
            contents = contents[:len(contents) -2]
        if contents[-1] != "Reply•Resolve":
            contents = contents[:len(contents) - 1]
        pin = pin + 1

        while pin < len(contents) -1 :
            pin = pin + 1
            name = contents[pin]
            comment = ""
            while contents[pin + 1] not in ["Reply•Resolve", "Reply"] and not self.contains_time(contents[pin + 1]):
                pin = pin + 1

                comment += contents[pin]
            pin = pin + 1
            date = contents[pin]
            #resolve and re-opening do not count
            if comment not in ['Marked as resolved', 'Re-opened']:
                self.update(name, date, comment)

        self.clean_dates()
