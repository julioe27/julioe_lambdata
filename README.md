# julioe_lambdata

## Installation
````
pip install -i https://test.pypi.org/simple/ julioe-lambdata
````

## Usage
This package can allow you to split city, state, and zip code into three columns.
### Example
````
from julioe_lambdata.my_mod import split_addresses

y = "Newtown, California 12465"
print(split_addresses(y))
````
````
--> ['Newtown', 'California', '12465']
````
It also allows you to abbreviate a state name into
its abbreviation and vice versa.
### Example
````
from julioe_lambdata.my_mod import state_abbreviation

x = 'California'
print(state_abbreviation(x))
x = 'CA'
print(state_abbreviation(x))
````

````
--> CA
--> California
````
Licensed under the [MIT License](LICENSE)