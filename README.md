# AirBnB clone

![AirBnB clone images](https://i.imgur.com/78Nj81H.png)

## First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

* put in place a parent class (called BaseModel) to take care of the initialization, serialization and * deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine


## What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object


## More Info

### Execution

Your shell should work like this in interactive mode:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) 
$
```

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) create User
67fd7b94-e22f-4ae5-901f-5fbdf3f57034
(hbnb) show User 67fd7b94-e22f-4ae5-901f-5fbdf3f57034
[User] (67fd7b94-e22f-4ae5-901f-5fbdf3f57034) {'id': '67fd7b94-e22f-4ae5-901f-5fbdf3f57034', 'created_at': datetime.datetime(2020, 7, 2, 3, 37, 29, 103113), 'updated_at': datetime.datetime(2020, 7, 2, 3, 37, 29, 103153)}
(hbnb) all
["[User] (d46de648-6a1b-41d1-b157-412f3444d021) {'id': 'd46de648-6a1b-41d1-b157-412f3444d021', 'created_at': datetime.datetime(2020, 7, 2, 3, 36, 44, 409077), 'updated_at': datetime.datetime(2020, 7, 2, 3, 36, 44, 409107)}", "[User] (67fd7b94-e22f-4ae5-901f-5fbdf3f57034) {'id': '67fd7b94-e22f-4ae5-901f-5fbdf3f57034', 'created_at': datetime.datetime(2020, 7, 2, 3, 37, 29, 103113), 'updated_at': datetime.datetime(2020, 7, 2, 3, 37, 29, 103153)}"]
(hbnb) update User 67fd7b94-e22f-4ae5-901f-5fbdf3f57034 greeting "Hello"
(hbnb) show User 67fd7b94-e22f-4ae5-901f-5fbdf3f57034
[User] (67fd7b94-e22f-4ae5-901f-5fbdf3f57034) {'created_at': datetime.datetime(2020, 7, 2, 3, 37, 29, 103113), 'greeting': 'Hello', 'id': '67fd7b94-e22f-4ae5-901f-5fbdf3f57034', 'updated_at': datetime.datetime(2020, 7, 2, 3, 39, 16, 797322)}
(hbnb) quit
```

![Architecture](https://i.imgur.com/xhDYcWv.png)

## Authors

→ [Andersen Castañeda ](https://github.com/AndersenCastaneda)
→ [Abdel Mejia](https://github.com/Bhalut)
