execute_process(COMMAND "/home/susyreyesm/ros/ur3c_ws/build/ur3/ur_control/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/susyreyesm/ros/ur3c_ws/build/ur3/ur_control/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
