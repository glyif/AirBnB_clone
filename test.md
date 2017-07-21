![Holberton logo](https://www.holbertonschool.com/assets/holberton-logo-1cc451260ca3cd297def53f2250a9794810667c7ca7b5fa5879a569a457bf16f.png)

# Your Document Title

## Author: Bobby Yang (Description)

## Paragraph Header
You can type any text information in this paragraph block. All the
Markdown (md) decorators can be use inside here in order to markup
your text, they will be keep as-is while being parsed.

## File Breakdown

### 1 - console.py


##### Class: HBNBCommand

```python
class HBNBCommand(cmd.Cmd):
```

HBNBCommand - class for HBNB cli  inherits from cmd.Cmd

##### Function: do_quit

```python
class HBNBCommand(cmd.Cmd):
	def do_quit(self, arg):
```

quit - quits from the cli

###### Params
- `@@self` self
- `@@arg` argument

##### Function: do_EOF

```python
class HBNBCommand(cmd.Cmd):
	def do_EOF(self, arg):
```

EOF - end of file

###### Params
- `@@self` self
- `@@arg` argument

##### Function: do_create

```python
class HBNBCommand(cmd.Cmd):
	def do_create(self, arg):
```

do_create - creates a class

###### Params
- `@@self` self
- `@@arg` argument

##### Function: do_show

```python
class HBNBCommand(cmd.Cmd):
	def do_show(self, arg):
```

do_show - prints the __str__ of a specific obj

###### Params
- `@@self` self
- `@@arg` argument

##### Function: do_destroy

```python
class HBNBCommand(cmd.Cmd):
	def do_destroy(self, arg):
```

do_destroy - delete/destroys an object

###### Params
- `@@self` self
- `@@arg` argument

##### Function: do_update

```python
class HBNBCommand(cmd.Cmd):
	def do_update(self, arg):
```

do_update - updates an object

###### Params
- `@@self` self
- `@@arg` argument

##### Function: do_all

```python
class HBNBCommand(cmd.Cmd):
	def do_all(self, arg):
```

do_all - prints all

###### Params
- `@@self` self
- `@@arg` arguments

##### Function: do_User

```python
class HBNBCommand(cmd.Cmd):
	def do_User(self, arg):
```

##### Function: emptyline

```python
class HBNBCommand(cmd.Cmd):
	def emptyline(self):
```

##### Function: input_validation

```python
class HBNBCommand(cmd.Cmd):
	def input_validation(args):
```

input_validation - validates input router  static method @args: list arguments

##### Function: class_validate

```python
class HBNBCommand(cmd.Cmd):
	def class_validate(args):
```

class_validate - validates a class arg  static method

###### Params
- `@@args` list of arguments

##### Function: instance_validate

```python
class HBNBCommand(cmd.Cmd):
	def instance_validate(args):
```

instance_validate - validates instance  staticmethod

###### Params
- `@@args` list of arguments

##### Function: update_validate

```python
class HBNBCommand(cmd.Cmd):
	def update_validate(args):
```

update_validate - validate update arguments

###### Params
- `@@args` arguments

##### Function: type_checker

```python
class HBNBCommand(cmd.Cmd):
	def type_checker(arg):
```

### 2 - tests/test_console.py


##### Class: TestConsole

```python
class TestConsole(unittest.TestCase):
```

##### Function: setUp

```python
def setUp(self):
```

standard setUp

##### Function: create

```python
def setUp(self):
	def create(self, server=None):
```

create

##### Function: test_exit

```python
def setUp(self):
	def test_exit(self):
```

test exit command

##### Function: _last_write

```python
def setUp(self):
	def _last_write(self, nr=None):
```

:return: last `n` output lines

### 3 - tests/test_models/test_city.py


##### Class: TestCity

```python
class TestCity(unittest.TestCase):
```

test model: city

##### Function: setUp

```python
class TestCity(unittest.TestCase):
	def setUp(self):
```

standard setUp()

##### Function: test_public_attr

```python
class TestCity(unittest.TestCase):
	def test_public_attr(self):
```

check if public attribute exists and if equal to empty string- state_id("", State.id), name("")

##### Function: test_strings

```python
class TestCity(unittest.TestCase):
	def test_strings(self):
```

assertEqual input for each attr

### 4 - tests/test_models/test_place.py


##### Class: TestPlace

```python
class TestPlace(unittest.TestCase):
```

test model: place

##### Function: setUp

```python
class TestPlace(unittest.TestCase):
	def setUp(self):
```

standard setUp()

##### Function: test_public_attr

```python
class TestPlace(unittest.TestCase):
	def test_public_attr(self):
```

check if public attribute exists and if equal to empty string, int, or float- city_id(""), user_id(""), name(""), description(""), number_rooms(0), number_bathrooms(0), max_guest(0), price_by_night(0), latitude(0.0), longitude(0.0), amenities([''])

##### Function: test_string_int_float

```python
class TestPlace(unittest.TestCase):
	def test_string_int_float(self):
```

assertEqual input for each attr

### 5 - tests/test_models/test_review.py


##### Class: TestReview

```python
class TestReview(unittest.TestCase):
```

test model: review

##### Function: setUp

```python
class TestReview(unittest.TestCase):
	def setUp(self):
```

standard setUp()

##### Function: test_public_attr

```python
class TestReview(unittest.TestCase):
	def test_public_attr(self):
```

check if public attribute exists and if equal to empty string- state_id("", State.id), name("")

##### Function: test_strings

```python
class TestReview(unittest.TestCase):
	def test_strings(self):
```

assertEqual input for each attr

### 6 - tests/test_models/test_base_model.py


##### Class: TestBaseModel

```python
class TestBaseModel(unittest.TestCase):
```

test model: base_model

##### Function: setUp

```python
class TestBaseModel(unittest.TestCase):
	def setUp(self):
```

standard setUp()

##### Function: test_name_number

```python
class TestBaseModel(unittest.TestCase):
	def test_name_number(self):
```

test name and number

##### Function: test_public_attr

```python
class TestBaseModel(unittest.TestCase):
	def test_public_attr(self):
```

id (uuid), created_at (datetime), updated_at (datetime)

##### Function: test_save

```python
class TestBaseModel(unittest.TestCase):
	def test_save(self):
```

save

##### Function: test_to_json

```python
class TestBaseModel(unittest.TestCase):
	def test_to_json(self):
```

__dict__ (instance + class name in the key __class__)

### 7 - tests/test_models/test_amenity.py


##### Class: TestAmenity

```python
class TestAmenity(unittest.TestCase):
```

test model: amenity

##### Function: setUp

```python
class TestAmenity(unittest.TestCase):
	def setUp(self):
```

standard setUp()

##### Function: test_public_attr

```python
class TestAmenity(unittest.TestCase):
	def test_public_attr(self):
```

check if public attribute exists and if equal to empty string- name("")

##### Function: test_string

```python
class TestAmenity(unittest.TestCase):
	def test_string(self):
```

assertEqual input for each attr

### 8 - tests/test_models/test_state.py


##### Class: TestState

```python
class TestState(unittest.TestCase):
```

test model: state

##### Function: setUp

```python
class TestState(unittest.TestCase):
	def setUp(self):
```

standard setUp()

##### Function: test_public_attr

```python
class TestState(unittest.TestCase):
	def test_public_attr(self):
```

check if public attribute exists and if equal to empty string- name("")

##### Function: test_string

```python
class TestState(unittest.TestCase):
	def test_string(self):
```

assertEqual input for each attr

### 9 - tests/test_models/test_user.py


##### Class: TestUser

```python
class TestUser(unittest.TestCase):
```

test model: user

##### Function: setUp

```python
class TestUser(unittest.TestCase):
	def setUp(self):
```

standard setUp()

##### Function: test_oublic_attr

```python
class TestUser(unittest.TestCase):
	def test_oublic_attr(self):
```

check if public attributes are exist and if equal to empty string- email(""), password(""), first_name(""), last_name("")

##### Function: test_strings

```python
class TestUser(unittest.TestCase):
	def test_strings(self):
```

assertEqual input for each attr

### 10 - models/city.py


##### Class: City

```python
class City(BaseModel):
```

##### Function: \_\_init\_\_

```python
def __init__(self, *args, **kwargs):
```

### 11 - models/user.py


##### Class: User

```python
class User(BaseModel):
```

##### Function: \_\_init\_\_

```python
def __init__(self, *args, **kwargs):
```

### 12 - models/state.py


##### Class: State

```python
class State(BaseModel):
```

##### Function: \_\_init\_\_

```python
def __init__(self, *args, **kwargs):
```

### 13 - models/base_model.py


##### Class: BaseModel

```python
class BaseModel:
```

##### Function: \_\_init\_\_

```python
def __init__(self, *args, **kwargs):
```

##### Function: \_\_str\_\_

```python
def __init__(self, *args, **kwargs):
	def __str__(self):
```

##### Function: save

```python
def __init__(self, *args, **kwargs):
	def save(self):
```

##### Function: to_json

```python
def __init__(self, *args, **kwargs):
	def to_json(self):
```

### 14 - models/review.py


##### Class: Review

```python
class Review(BaseModel):
```

##### Function: \_\_init\_\_

```python
def __init__(self, *args, **kwargs):
```

### 15 - models/place.py


##### Class: Place

```python
class Place(BaseModel):
```

##### Function: \_\_init\_\_

```python
def __init__(self, *args, **kwargs):
```

### 16 - models/amenity.py


##### Class: Amenity

```python
class Amenity(BaseModel):
```

##### Function: \_\_init\_\_

```python
def __init__(self, *args, **kwargs):
```

### 17 - models/engine/file_storage.py


##### Class: DateDecoder

```python
class DateDecoder(json.JSONEncoder):
```

##### Function: default

```python
def default(self, obj):
```

##### Class: FileStorage

```python
class FileStorage:
```

##### Function: \_\_init\_\_

```python
def __init__(self):
```

##### Function: all

```python
def __init__(self):
	def all(self):
```

##### Function: new

```python
def __init__(self):
	def new(self, obj):
```

##### Function: save

```python
def __init__(self):
	def save(self):
```

##### Function: reload

```python
def __init__(self):
	def reload(self):
```

## License
MIT
More descriptions of your license go here if any