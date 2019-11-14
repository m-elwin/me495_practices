# Python setup file used for installing a python catkin package.
# See http://docs.ros.org/melodic/api/catkin/html/user_guide/setup_dot_py.html
# For catkin to use this we have called python_catkin_setup() in CMakeLists.txt
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages = ['me495_practices'],
    # we don't use scripts to installs scripts since
    # for a ROS package we want the scripts to be installed
    # in the package directory and not in /usr/bin
    # Scripts are instead installed via CMakeLists.txt
    # scripts=['bin/myscript']
    package_dir={'' : 'src'}
)

setup(**d)
