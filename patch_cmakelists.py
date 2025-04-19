# coding: utf-8

import sys


def replace_in_file(file_path, encoding, replacements):
    with open(file_path, 'r', encoding=encoding) as file:
        content = file.read()

    for old_text, new_text in replacements:
        content = content.replace(old_text, new_text)

    with open(file_path, 'w', encoding=encoding) as file:
        file.write(content)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:\n  python patch_cmakelists.py <cmakelists_file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    replacements = [
        (
            "set(LSL_ABI_VERSION 2)",
            """set(LSL_ABI_VERSION 2)

if(MSVC)
    foreach(flag_var
        CMAKE_CXX_FLAGS CMAKE_CXX_FLAGS_DEBUG CMAKE_CXX_FLAGS_RELEASE
        CMAKE_CXX_FLAGS_MINSIZEREL CMAKE_CXX_FLAGS_RELWITHDEBINFO)
        if(${flag_var} MATCHES "/MD")
            string(REGEX REPLACE "/MD" "/MT" ${flag_var} "${${flag_var}}")
        endif(${flag_var} MATCHES "/MD")
    endforeach(flag_var)
endif()
"""
        ),
        (
            "target_link_libraries(lsl PRIVATE lslobj lslboost)",
"""
if(MSVC AND NOT LSL_BUILD_STATIC)
    target_compile_options(lsl PRIVATE $<$<CONFIG:Release>:/Zi>)
    target_link_options(lsl PRIVATE "$<$<CONFIG:Release>:/DEBUG;/OPT:REF;/OPT:ICF>")
endif()

target_link_libraries(lsl PRIVATE lslobj lslboost)
""",
        ),
        (
            "include(cmake/LSLCMake.cmake)",
"""
if(MSVC AND NOT LSL_BUILD_STATIC)
    install(FILES $<TARGET_PDB_FILE:lsl>
        DESTINATION "${CMAKE_INSTALL_BINDIR}" OPTIONAL
    )
endif()

include(cmake/LSLCMake.cmake)""",
        ),
    ]

    try:
        replace_in_file(file_path, 'utf-8', replacements)

        print(f"Patching done successfully in '{file_path}'.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except IOError as e:
        print(f"Error: An I/O error occurred. Details: {e}")
