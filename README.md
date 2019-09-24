# Register
Register is an online registration site where applicants come to register

## Technologies Used
* [django.js](https://www.djangoproject.com/) - A python framework
* [postgres](https://www.postgresql.org/) - Database managemant tool


### Installation

1. Install  [postgres](https://www.postgresql.org/)
```
Download and install postgresql
```

2. Clone this repository using
```
git clone https://github.com/Joyce-O/Register.git
```
3. Open the repository in terminal and Install dependencies by running:
```
# installing dependencies from file
$ pip install -r requeriments.txt
```
4. cd applicants/ and run
```
python manage.py runserver 0.0.0.0:5000
```
5. create a table by running
```
python manage.py migrate
```
Note: Ensure that you create a .env file in the root directory and copy paste .env.sample parameters to it and replace with your on credentials.

6. Make a post request to [`localhost:5000/api/v1/register/`](localhost:5000/api/v1/register) on postman to register an applicant

    
## Author
* Joyce Obi
