# CountingComments (beta)

This tool parses raw text input from a Google doc file and performs comprehension of comments and replies, and queries relevant data. Useful for getting simple statistics about comments (participants, frequency, content, etc.).

Currently undergoing beta phase. Open source project.

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
FILE_NAME is placeholder for the file. So for example, if my comments are copied into "mcdonald.txt", I would run `python runner.py --file content.txt` to analyze it. 

This should output each student who commented/replied, including the number of comments/replies the each made, sorted alphabetically. This is the default behavior. There are more specific, advanced use cases; however, every program call must contain "--file" and an existing file, or else the program will throw an error. 

## Advanced Usage

Different behaviors from the script can be triggered by using options. Each option will be followed with an example of the use case, on the sample text file "mcdonald.txt".

**--names**: lists all the students who commented or replied, in alphabetical order by last name
`python runner.py --file mcdonald.txt --names`

**--stats**: shows all students in alphabetical order, with number comments and number of replies
`python runner.py --file mcdonald.txt --stats`

**--verbose**: shows all students in alphabetical order, with each comment's time stamp listed. Comment contents not shown. Asks for name of a text file to write to, otherwise writes to "output.txt". 
`python runner.py --file mcdonald.txt --verbose newfile`
will save the output into "newfile", creating it if it does not previously exist. The command
`python runner.py --file mcdonald.txt --verbose`
will save the output into "output.txt", which is the default destination if nothing is given.











