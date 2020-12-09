# webster's portfolio
# First of all you'll have to install the following
1. Git 
2. virtualenv
3. Python
4. Pip and/or Pipenv
5. Django

# Run On Your Machine?

1. Firstly, clone the repository using the git shell <br>
<code>$ git clone https://github.com/avosa/myportfolio.git</code> <br>
2. Goto the base directory of the project <br>
<code>myportfolio </code> <br>
3. Create a virtual environment and activate it. Creating using pipenv is easiest ie <code>$ pipenv shell</code><br>

You can also create the same using Pip with below steps <br>

<code>$ virtualenv django</code> <br>
<code>$ cd django</code> <br>
<code>$ cd .. </code> <br>
<code>$ venv\Scripts\activate</code> on Windows or <code>$ source bin/activate</code> on Linux and Mac <br>


4. Install the requirements for the project <br>
<code>$ pip3 install -r requirements.txt</code> on Linux or Mac and <code>$ pip install -r requirements.txt</code> on windows if your are using pip or simply <code>$ pipenv install </code> using pipenv <br>

5. Now start the localhost server<br>
<code>$ python3 manage.py runserver</code> on Linux or Mac and <code>$ python manage.py runserver</code> on Windows <br> <br>


