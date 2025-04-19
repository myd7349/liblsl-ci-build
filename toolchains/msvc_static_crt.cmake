cmake_policy(GET CMP0091 cmp0091_status)
message(STATUS "CMP0091 status: ${cmp0091_status}")

cmake_policy(SET CMP0091 NEW)

set(CMAKE_MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>" CACHE STRING "" FORCE)
