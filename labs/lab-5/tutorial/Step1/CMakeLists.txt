cmake_minimum_required(VERSION 3.10)

# set the project name and version
project(Tutorial VERSION 1.0)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# configure a header file to pass the version number to the source code
configure_file(TutorialConfig.h.in TutorialConfig.h)

# add the executable
add_executable(Tutorial tutorial.cxx)

# Allows the configured file above to be written into the binary tree, so we need to add that directory to the list of paths to search for include files 
target_include_directories(Tutorial PUBLIC
                            "${PROJECT_BINARY_DIR}"
                            )