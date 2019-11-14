* Overview
This package is here to demonstrate a ros package setup that uses
sphinx for documentation, unittest for python unit testing, and
has a python package that is separate from its nodes.


* Python Package
- =src/me495_practices= is a python package
  - =doc_example.py= is an example of documentation in the code
  - =hardmath= has a function that adds two numbers

* Nodes
- add_numbers - Creates a service: =add_two= that adds two numbers using the =hardmath= package

* Tests
=test/add_two_test= - Uses =unittest= to perform ordinary python unit testing
=test/add_two_client_test.py= - A ros node that tests the =add_numbers= service
=client_test.test= - =rostest= file to launch =add_two_client_test.py= and an =add_numbers= node

* Documentation
- Build Sphinx Documentation using =rosdoc_lite .= from the root directory