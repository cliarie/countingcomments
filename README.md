# CountingComments (beta)

This tool parses raw text input from a Google doc file and performs comprehension of comments and replies, and queries relevant data. Useful for getting simple statistics about comments (participants, frequency, content, etc.).

In beta (errors possible!). Open source project.

I have implemented this with a flask backend. http://countcomments.pythonanywhere.com/

## Basic Usage
**Instructions specific for Mac OS X. Windows integration coming soon...

This tool takes in as input a ".txt" file of the Google Doc "comment log" functionality. To access the "comment log", click the "Comment" symbol on the top right corner of the screen (on the left of the blue SHARE button), and copy paste the entire window's contents into an empty text editor, such as Notepad or TextEdit. Save this file, for example, as "content.txt". A sample ".txt" file is included in this folder ("mcdonald.txt").

Once the text file is saved (remember where it is), perform the following steps:

1. Point to the following link: https://github.com/bg459/countingcomments/archive/master.zip. You can also open it in a new tab in your browser. A download should start, called "countingcomments.zip".

2. Open "countingcomments.zip" by clicking it. It should open a folder up. The folder should have a few files in it; make sure there is "runner.py", and "thread.py". 

3. Move the text file (mcdonald.txt or whatever you named it) into the new folder (countingcomments-master)

4. Open Terminal. Easiest way to do this is to Press ⌘(Cmd) + Space, typing "Terminal", and pressing enter. A terminal window should open.

5. Make sure you have python. Mac OS comes with Python, but it's good to be sure. In terminal, type `python --version` and the output should look something like `Python 3.x.x`. Any version 3 Python should work, if the numbers start with 2, that's also probably fine (but I'll need to check).

6. In Terminal window, type the following commands, in succession, pressing 'Enter' after each command.

```
cd ~/Downloads/countingcomments-master
python runner.py --file [FILE_NAME]
```
FILE_NAME is placeholder for the file. So for example, if my comments are copied into "mcdonald.txt", I would run `python runner.py --file mcdonald.txt` to analyze it. 

This should output each student who commented/replied, including the number of comments/replies the each made, sorted alphabetically. This is the default behavior. There are more specific, advanced use cases; however, every program call must contain "--file" and an existing file, or else the program will throw an error. 

## Advanced Usage

Different behaviors from the script can be triggered by using options. Each option will be followed with an example of the use case, on the sample text file "mcdonald.txt". 

**--names**: lists all the students who commented or replied, in alphabetical order by last name

`python runner.py --file mcdonald.txt --names`

**--stats** (default): shows all students in alphabetical order, with number comments and number of replies

`python runner.py --file mcdonald.txt --stats`

**--verbose [FILE_NAME]**: shows all students in alphabetical order, with each comment's time stamp listed. Comment contents not shown. Asks for name of a text file to write to. File must be provided, the script will only edit local files if given permission with [FILE_NAME]

`python runner.py --file mcdonald.txt --verbose newfile`
will save the output into "newfile", creating it if it does not previously exist.

**--full [FILE NAME]**: Writes all the comments, with all relevant information to a file. (Similar to what shows up in Google docs) File name must be provided, a new file will be created if it doesn't exist. 

`python runner.py --file mcdonald.txt --full newfile`
## Notes

### What exactly is counted? 

I filter out certain types of messages that show up in the comment box. Everything is a "comment" to this program unless: 

1) It is a suggestion (Add, Delete, etc. )

2) It is Resolved and NOT Re-opened. 

I filter out certain replies that show up in the comment box. Everything is a "reply" to this program unless:

1) It is a comment (obviously)

2) It is a reply to a suggestion.

3) It is a reply to something Resolved and NOT Re-opened.

4) The act of resolving or re-opening is not a reply, even if the comment is eventually Re-opened. 

### On multiple options

Only option will be run at a time, and if multiple are entered only the first will be considered. So, for example, the command 

`python runner.py --file mcdonald.txt --stats --verbose newfile`

is equivalent to 

`python runner.py --file mcdonald.txt --stats`

as far as the program is concerned.

## Suggestions/Comments?

I want this to be as useful as possible, so I can expand capabilities or adjust the functionalites when desired. Of course if there is a bug or unexpected behavior please let me know and I'll fix it. 

You can reach me at bguo + 'at' + caltech.edu







