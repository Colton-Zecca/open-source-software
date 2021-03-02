add_library(MathFunctions mysqrt.cxx)

# Remember INTERFACE means things that consumers require but the producer doesn't
# Since we've specified usage requirements for MathFunctions we can safely remove our uses of EXTRA_INCLUDES from the top-level CMakeLists.txt (I.e. The EXTRA_INCLUDES in if(USE_MYMATH) block and in target_include_directories(...))
target_include_directories(MathFunctions
          INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
          )
