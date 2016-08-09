# Python Startup Template

Here is repo to be cloned or downloaded, and acts as a starting base for any python projects

## Before using

### Install libraries

At command line make sure the following is run

```bash
$ brew install python
$ pip install nose
$ pip install rednose

```

Note: $ means command prompt
Note: This is based on MacOS

### Naming

- Instances of ```NAME``` change to appropriate title, usually ```app``` or ```lib```
- Instances of ```class_name``` change to match name of class in the file
- Change name of folder from ```test-setup``` to name of app

### Importing

- The testing frame work is ```unittest``` and comes preloaded
- For mocks use ```MagicMock```(to access look in class_name_tess.py)
- To import file where script is to be tested see example at top of class_name_tess.py

### Filling in setup.py

- Match replace similar names seen in name of files earlier ie replace ```packages``` and ```name``` values
- Fill as see fit

### Console

- In command line type ```python``` to have console like irb
- If prefer something similar to pry, ```pip install ipython``` and at commmand line type ```ipython```

### Adding detail to tests

- under ```def test_name````, write in single line ````"""Description of test"""```
- This will be shown in the test documentation when tests are run with ```-v``` flag

### Running tests

1.  Make sure in root directory
2.  For running single tests ```nosetests --rednose tests/class_name_test.py```
  - nosetests is the test runner
3. To run all tests ```nosetests --rednose```
4. To run with more information ```nosetests --rednose -v```
