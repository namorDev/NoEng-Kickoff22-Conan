cmake_minimum_required (VERSION 3.12.0)

project(Producer)

# Using the "cmake" generator
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_library(${PROJECT_NAME} src/hello.cpp)
target_link_libraries(${PROJECT_NAME} PUBLIC ${CONAN_LIBS})