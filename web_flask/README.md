# 0x04. AirBnB clone - Web framework
#### This is a project that shows how dynamic web pages can be built with the Flask web application module


## How the tasks work:
### Note:
  + Web application must be listening on `0.0.0.0`, port `5000`.

+ [x] 0. Hello Flask!<br/>_**[0-hello_route.py](0-hello_route.py)**_ contains a script that starts a Flask web application.

+ [x] 1. HBNB<br/>_**[1-hbnb_route.py](1-hbnb_route.py)**_ contains a script that starts a Flask web application.

+ [x] 2. C is fun!<br/>_**[2-c_route.py](2-c_route.py)**_ contains a script that starts a Flask web application.
+ /: display “Hello HBNB!”
+ /hbnb: display “HBNB”
+ /c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )

+ [x] 3. Python is cool!<br/>_**[3-python_route.py](3-python_route.py)**_ contains a script that starts a Flask web application.

+ [x] 4. Is it a number?<br/>_**[4-number_route.py](4-number_route.py)**_ contains a script that starts a Flask web application.

+ [x] 5. Number template<br/>_**[5-number_template.py](5-number_template.py)**_ contains a script that starts a Flask web application.

+ [x] 6. Odd or even?<br/>_**[6-number_odd_or_even.py](6-number_odd_or_even.py)**_ contains a script that starts a Flask web application.

+ [x] 7. Improve engines
  + **INFO**: Before using Flask to display our HBNB data, you will need to update some part of our engine.
  + Update [`FileStorage`](../models/engine/file_storage.py):
    + Add a public method `def close(self):`: call `reload()` method for deserializing the JSON file to objects.
  + Update [`DBStorage`](../models/engine/db_storage.py):
    + Add a public method `def close(self):`: call `remove()` method on the private session attribute (`self.__session`) [tips](https://docs.sqlalchemy.org/en/13/orm/contextual.html) or `close()` on the class `Session` [tips](https://docs.sqlalchemy.org/en/13/orm/session_api.html).
  + Update [`State`](../models/state.py) - If it's not already present.
    + If your storage engine is not `DBStorage`, add a public getter method `cities` to return the list of `City` objects from storage linked to the current `State`.

+ [x] 8. List of states<br/>_**[7-states_list.py](7-states_list.py)**_ contains a script that starts a Flask web application.
  + You must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`.
  + After each request you must remove the current SQLAlchemy Session:
    + Declare a method to handle `@app.teardown_appcontext`.
    + Call in this method `storage.close()`.

+ [x] 9. Cities by states<br/>_**[8-cities_by_states.py](8-cities_by_states.py)**_ contains a script that starts a Flask web application.
  + You must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`.  + To load all cities of a `State`:
    + If your storage engine is `DBStorage`, you must use `cities` relationship.
    + Otherwise, use the public getter method `cities`.
  + After each request you must remove the current SQLAlchemy Session:
    + Declare a method to handle `@app.teardown_appcontext`.
    + Call in this method `storage.close()`.


+ [x] 10. States and State<br/>_**[9-states.py](9-states.py)**_ contains a script that starts a Flask web application.
  You must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`.
  To load all cities of a `State`:
    + If your storage engine is `DBStorage`, you must use `cities` relationship.
    + Otherwise, use the public getter method `cities`.
  + After each request you must remove the current SQLAlchemy Session:
    + Declare a method to handle `@app.teardown_appcontext`.
    + Call in this method `storage.close()`.

+ [x] 11. HBNB filters<br/>_**[10-hbnb_filters.py](10-hbnb_filters.py)**_ contains a script that starts a Flask web application.
  + You must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`.
  + To load all cities of a `State`:
    + If your storage engine is `DBStorage`, you must use `cities` relationship.
    + Otherwise, use the public getter method `cities`.
  + After each request you must remove the current SQLAlchemy Session:
    + Declare a method to handle `@app.teardown_appcontext`.
    + Call in this method `storage.close()`.
 

+ [x] 12. HBNB is alive!<br/>_**[100-hbnb.py](100-hbnb.py)**_ contains a script that starts a Flask web application.
  + You must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`.
  + To load all cities of a `State`:
    + If your storage engine is `DBStorage`, you must use `cities` relationship.
    + Otherwise, use the public getter method `cities`.
  + After each request you must remove the current SQLAlchemy Session:
    + Declare a method to handle `@app.teardown_appcontext`.
    + Call in this method `storage.close()`.