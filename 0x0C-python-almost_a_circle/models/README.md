# Models

- [base.py](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0C-python-almost_a_circle/models/base.py) - Class `Base`:
  - Private class attribute `__nb_objects = 0`
  - Class constructor: `def __init__(self, id=None):`
     - If `id` is not `None`, the public instance `id` with the argument value is assigned, the `id` is an integer
     - Otherwise `__nb_objects` is incremented and the new value is assigned to the public instance attribute `id`
  - Static method `def to_json_string(list_dictionaries):` that returns the JSON representation of `list_dictionaries`:
    - `list_dictionaries` is a list of dictionaries
    - If `list_dictionaries` is `None` or empty, returns the string `"[]"`
    - Otherwise returns the JSON string representation of `list_dictionaries`
  - Class method `def save_to_file(cls, list_objs):` that writes the JSON representation of `list_objs` to a file:
    - `list_objs` is a list of instances who inherits of `Base` - example: list of `Rectangle` or list of `Square` instances
    - If `list_objs` is `None`, saves an empty list
    - The filename is: `<Class name>.json` - example: `Rectangle.json`
    - The static method `to_json_string` (created before) is used
    - If the file already exists, it will be overwritten
  - Static method `def from_jon_string(json_string):` that returns the list of JSON string representation `json_string`
    - `json_string` is a string representing a list of dictionaries
    - If `json_string` is `None` or empty, returns an empty list
    - Otherwise, returns the list represented by `json_string`

- [rectangle.py](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0C-python-almost_a_circle/models/rectangle.py) - 

- [square.py](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0C-python-almost_a_circle/models/square.py) -
