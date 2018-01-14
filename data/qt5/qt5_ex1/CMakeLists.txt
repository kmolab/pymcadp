# cmake .. -G "MinGW Makefiles" -DCMAKE_BUILD_TYPE=Release

cmake_minimum_required(VERSION 3.10)

project (calculator)

# Find includes in corresponding build directories
set(CMAKE_INCLUDE_CURRENT_DIR ON)
# Instruct CMake to run moc automatically when needed.
set(CMAKE_AUTOMOC ON)

# Find the QtWidgets library
find_package(Qt5Widgets)

add_executable (calculator WIN32 main.cpp)
# Use the Widgets module from Qt 5.
target_link_libraries(calculator Qt5::Widgets)
