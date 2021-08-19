# unrival_py

## Installation
After cloning the repository and navigating inside of it, run:
`pip3 install -r requirements.txt`

## Testing

unrival_py uses `pytest_bdd` for running automated tests based on Gherkin feature specifications.  These specs are available in `/tests/features`.

### Running Tests
From within the root directory, run:
`$ pytest` 

### Style Guide

#### conftest.py

Data required for tests should be returned by fixtures in the `conftest.py`.  The naming convention for these fixtures is as follows:

`<name_of_scenario>_<description_of_data>` 

This makes is simple to differentiate between, for instance, sets of parts (i.e. json lists of objects) from one scenario to the next.

This may produce long fixture names, but it can be difficult to find unique, descriptive, and concise names for fixtures.  Our convention sacrifices conciseness for consistency.
