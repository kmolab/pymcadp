cmake_minimum_required(VERSION 2.8.11)
project(v_repExtSDL)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_MACOSX_RPATH 1)

set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -DDEBUG")

find_package(Boost REQUIRED regex)
find_package(SDL2 REQUIRED)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake/modules/")
find_package(VREP REQUIRED)

include_directories(${VREP_INCLUDE})
include_directories(${CMAKE_BINARY_DIR}/generated)
include_directories(${CMAKE_SOURCE_DIR}/external)
include_directories(${Boost_INCLUDE_DIRS})
include_directories(${SDL2_INCLUDE_DIRS})

vrep_generate_stubs(${CMAKE_BINARY_DIR}/generated XML_FILE ${CMAKE_SOURCE_DIR}/callbacks.xml LUA_FILE ${CMAKE_SOURCE_DIR}/simExtSDL.lua)

configure_file(${CMAKE_SOURCE_DIR}/config.h.in ${CMAKE_BINARY_DIR}/config.h)

set(SOURCES
    plugin.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/generated/stubs.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/external/v_repPlusPlus/Plugin.cpp
    ${VREP_EXPORTED_SOURCES}
)

set_property(SOURCE ${CMAKE_CURRENT_BINARY_DIR}/generated/stubs.cpp PROPERTY SKIP_AUTOMOC ON)

set(LIBRARIES
    ${Boost_LIBRARIES}
    ${SDL2_LIBRARIES}
    ${VREP_LIBRARIES}
)

add_library(v_repExtSDL SHARED ${SOURCES})
target_link_libraries(v_repExtSDL ${LIBRARIES})

install(TARGETS v_repExtSDL DESTINATION ${VREP_ROOT})

