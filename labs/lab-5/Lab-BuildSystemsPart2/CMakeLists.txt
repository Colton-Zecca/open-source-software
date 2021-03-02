cmake_minimum_required(VERSION 3.10)

project(ProgramStatic)
add_library(static_block.a source/block.c)
add_executable(ProgramStatic program.c)
target_link_libraries(ProgramStatic static_block.a)


project(ProgramShared)
add_library(shared_block.so SHARED source/block.c)
add_executable(ProgramShared program.c)
target_link_libraries(ProgramShared shared_block.so)
