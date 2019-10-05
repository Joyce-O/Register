# Use this to run...  DO chmod +x diary.py then do ./diary.py. THIS WHEN YOU DON"T WANT TO TYPE python3 filename.py

#!/usr/bin/env python3  
from collections import OrderedDict # BEHAVES LIKE SWITCH STATEMENT
import datetime
import sys # sys - a Python module that contains functionality for interacting with the system
# sys.stdin - a Python object that represents the standard #input stream. In most cases, this will be the keyboard

from peewee import *

db = SqliteDatabase("diary.db")

class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)
    

    class Meta:
        database = db

def initialize():
    '''Create the database and the tabl if the don't exist'''
    db.connect()
    db.create_tables([Entry], safe=True)

def menu_loop():
    '''Show the menu'''
    choice = None # None is like saying choice;

    while choice != 'q':
        print('Enter "q" to quit.')
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))# __doc__ is the doc string in each of the functions we represented in the OrderDict
        choice = input('Action: ').lower().strip()

        if choice in menu:
            menu[choice]()

def add_entry():
    '''Add an entry'''
    print("Enter your entry, Press ctr+d when finished.") # ctr+d signifies end of line
    data = sys.stdin.read().strip()

    if data:
        if input('Save entry? [Yn ').lower() != 'n':
            Entry.create(content=data)
            print("Saved successfully!")

def view_entries():
    '''View previous entries'''
    entries = Entry.select().order_by(Entry.timestamp.desc())

    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')

def delete_entry(entry):
    '''Delete an entry'''


menu = OrderedDict([ # The OderedDict is almost like normal dict except that it remembers the order the entries where put
   ('a', add_entry),
   ('v', view_entries) 
])

if __name__ == '__main__':
    initialize()
    menu_loop()


