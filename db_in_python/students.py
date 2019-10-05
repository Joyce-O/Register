from peewee import *
# FOR EVERY DATABASE CREATION YOU MUST FIRST ESTABLISH A CONNECTION
db = SqliteDatabase('students.db') # we're connecting to sqlite here


# CREATE A TABLE (name must be singular) USING CLASS ABSTRACTION COS OF ORM
class Student(Model): # This class will inherit from peewee model class hence the (Model)
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default=0)

    class Meta: # This name is not necessarily a Meta in that sense but a class where you add some attributes
        database = db


# CREATE A DICT THAT WILL HOLD THE DATA TO BE INSERTED
students = [
    {'username': 'Jonah', 'points': 344},
    {'username': 'Minna', 'points': 219},
    {'username': 'Horeb', 'points': 876},
    {'username': 'Smith', 'points': 653},
    {'username': 'Ken', 'points': 671},
]

# ADD A FUNCTION THAT WILL GO THROUGH THE DICT AND ADD THEM TO THE DATABASE
# def add_students():
#     for student in students:
#         Student.create(username=student['username'], #Student.create from the model Student
#                        points=student['points'])

# THE ABOVE METHOD WILL THROW ERRORS WHEN YOU CALL THE METHOD TWICE COS OF THE UNIQUE CONSTRAINT ON USERNAME, SO USE THIS SECOND METHON INSTEAD
def add_students():
    for student in students:
        try:
            Student.create(username=student['username'],
                           points=student['points'])
        except IntegrityError:
            student_record = Student.get(username=student['username'])
            student_record.points = student['points']
            student_record.save()

# FUNCTION THAT GETS TOP STUDENTS
def top_student():
    student = Student.select().order_by(Student.points.desc()).get()
    return student

if __name__ == '__main__': # If our file is run directly and not imported run and create the table
    db.connect()
    db.create_tables([Student], safe=True) # This 'self' is like if table exist do nothing
    add_students() # Call the method here
    print("Our top student is: {0.username}", format(top_student())) # Print the result of the top student here

# NEW TERMS
# model - A code object that represents a database table
# SqliteDatabase - The class from Peewee that lets us connect to an SQLite database
# Model - The Peewee class that we extend to make a model
# CharField - A Peewee field that holds onto characters. It's a varchar in SQL terms
# max_length - The maximum number of characters in a CharField
# IntegerField - A Peewee field that holds an integer
# default - A default value for the field if one isn't provided
# unique - Whether the value in the field can be repeated in the table
# .connect() - A database method that connects to the database
# .create_tables() - A database method to create the tables for the specified models.
# safe - Whether or not to throw errors if the table(s) you're attempting to create already exist

# New Terms 2
# .create() - creates a new instance all at once
# .select() - finds records in a table
# .save() - updates an existing row in the database
# .get() - finds a single record in a table
# .delete_instance() - deletes a single record from the table
# .order_by() - specify how to sort the records
# if __name__ == '__main__' - a common pattern for making code only run when the script is run and not when it's imported
# db.close() - not a method we used, but often a good idea. Explicitly closes the connection to the database.
# .update() - also something we didn't use. Offers a way to update a record without .get() and .save(). Example: Student.update(points=student['points']).where(Student.username == student['username']).execute()