cmake_minimum_required(VERSION 2.8.3)
project(me495_practices)

find_package(catkin REQUIRED COMPONENTS message_generation)

add_message_files(
  FILES
  OneInt.msg
)

add_service_files(
   FILES
   TwoResult.srv
)

# use the setup.py to install python modules
catkin_python_setup()

generate_messages()


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES practice
  CATKIN_DEPENDS message_runtime
#  DEPENDS system_lib
)

install(PROGRAMS
   nodes/add_numbers
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
   )

#############
## Testing ##
#############

## Add gtest based cpp test target and link libraries
# catkin_add_gtest(${PROJECT_NAME}-test test/test_practice.cpp)
# if(TARGET ${PROJECT_NAME}-test)
#   target_link_libraries(${PROJECT_NAME}-test ${PROJECT_NAME})
# endif()

## Add folders to be run by python nosetests
# catkin_add_nosetests(test)
