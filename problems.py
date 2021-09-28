"""
You need to calculate how many characters are in all of Shakespeare's sonnets.
Don't worry, another programmer lent us a folder containing all of his sonnets as separate text files.
This is the "sonnets" folder found
But, for speed we need you to use threading to parallelize the computation. Thus, you should
create one thread for each sonnet to check how many characters are in it, and then figure out how to sum all
those characters.

Return the number of characters in all the sonnets from the below function.
Hint: Don't be clever when checking how many characters there are in a file, just call len(f.read()).
"""


def chars_in_sonnets() -> int:
    pass


"""
Don't trust weird executables you find online? Let's write our own version of netcat with a python function
Have a the function start a connection based on it's arguments, then send user input down the connection and
print any data it receives.

No tests for this one, try using it on an echo server or any other server you've written previously.
Hint: You'll probably need to create two threads, one for collecting and sending user input and one for
receiving and printing messages from the connection.
"""


def netcat(ipaddr: str, port: int):
    pass
