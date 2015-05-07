# .ycm_extra_conf.py for single file C/C++ programs (as a fallback default)
import os

# Attention:
# File path (starting with / or .) will be expanded.
# Thus do not write things like '-i /path/to/somefile'.
# Besides, the expansion starts from this config file!

flags_c = [
    '-Wall',
    '-Wextra',
    '-Werror',
    '-Wno-variadic-macros',
    '-DNDEBUG',
    '-x', 'c',
    '-std=gnu11',
    '-isystem', '/usr/local/include',
    '-isystem', '/usr/include',
]

flags_cpp = [
    '-Wall',
    '-Wextra',
    '-Werror',
    '-Wno-variadic-macros',
    '-fexceptions',
    '-DNDEBUG',
    '-x', 'c++',
    '-std=gnu++11',
    '-stdlib=libstdc++',
    '-isystem', '/usr/include/c++/4.9.2',
    '-isystem', '/usr/include/c++/4.9.2/x86_64-unknown-linux-gnu',
    '-isystem', '/usr/include/c++/4.9.2/backward',
    '-isystem', '/usr/local/include',
    '-isystem', '/usr/include',
]


def DirectoryOfThisScript():
    return os.path.dirname(os.path.abspath(__file__))


def MakeRelativePathsInFlagsAbsolute(flags, working_directory):
    if not working_directory:
        return flags
    new_flags = []
    make_next_absolute = False
    path_flags = ['-isystem', '-I', '-iquote', '--sysroot=', '-include']
    for flag in flags:
        new_flag = flag

        if make_next_absolute:
            make_next_absolute = False
            if not flag.startswith('/'):
                new_flag = os.path.join(working_directory, flag)

        for path_flag in path_flags:
            if flag == path_flag:
                make_next_absolute = True
                break
            if flag.startswith(path_flag):
                path = flag[len(path_flag):]
                new_flag = path_flag + os.path.join(working_directory, path)
                break

        if new_flag:
            new_flags.append(new_flag)

    return new_flags


def FlagsForFile(filename):
    extension = os.path.splitext(filename)[1]
    if extension == '.c' or \
            extension == '.h' and os.path.exists(filename[:-2] + '.c'):
        flags = flags_c
    else:
        flags = flags_cpp

    relative_to = DirectoryOfThisScript()
    final_flags = MakeRelativePathsInFlagsAbsolute(flags, relative_to)
    return {
        'flags': final_flags,
        'do_cache': True
    }
