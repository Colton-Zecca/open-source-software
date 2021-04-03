cmake_minimum_required(VERSION 3.10)

project(main)
add_library(libstatic.a static/static.c)
add_library(libshared.so SHARED shared/shared.c)
# add_executable(main helper.c)
add_executable(main main.c)
target_link_libraries(main libstatic.a libshared.so)

target_include_directories(main PUBLIC
                           "${PROJECT_BINARY_DIR}"
                           )