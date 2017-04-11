# Dojo Office Space Allocator

Dojo Office Space Allocator is an application that is used at the dojo at Andela to randomly allocate Office Spaces and Living
spaces to Andela Fellows and Staff. A new Andela Fellow is assigned an Office Space and an optional Living space. An Andela staff
member is assigned only an Office Space.

## Getting started

### Prerequisites

The requirements are defined in the requirements file

```
requirements.txt
```

### Installing

Install python on your system

```
sudo apt install python
```

Clone the repository using the url:

```
git clone https://github.com/JayKay24/Office_Space_Allocation.git
```

## Running the tests

Open your python interpreter along with tests.py

```
python tests.py
```

Change directory into the application folder

```
$cd Office_Space_Allocation
```

## Usage

Dojo Office Space Allocation system utilizes the docopt argument parser

```
"""
Usage:
      create_room <room_type> <room_name>
      add_person <person_name> <fname> <lname> [wants_accommodation]
      print_room <room_name>
      print_allocations [-o=filename]
      print_unallocated [-o=filename]
      reallocate_person <person_identifier> <new_room_name>
      load_people
      save_state [--db=sqlite_database]
      load_state <sqlite_database>

Options:
      -o, --output Save to a txt file
      -i, --interactive Interactive mode
      -h, --help Show this screen and exit
"""
```

These tests test for OOP concepts in classes implemented under the MVC Framework

## Built Using

Dojo Office Space Allocation system is built using the following tools:

* Python version 3.5
* Docopt version 0.6.1

## Authors

* **James Kinyua Njuguna**

## Acknowledgements

* Hat tip to my team of budding software developers at Cohort 17
