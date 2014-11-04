# .ycm_extra_conf.py for single file C/C++ programs (as a fallback default)
import os
import ycm_core
from clang_helpers import PrepareClangFlags

# Attention:
# File path (starting with / or .) will be expanded.
# Thus do not write things like '-i /path/to/somefile'.
# Besides, the expansion starts from this config file!

flags_c = [
'-Wall',
'-Wextra',
'-Werror',
'-Wno-variadic-macros',
'-fexceptions',
'-DNDEBUG',
'-DUSE_CLANG_COMPLETER',
'-x', 'c',
'-std=gnu11',
'-isystem', '/usr/local/include',
'-isystem', '/usr/lib/clang/3.4/include',
'-isystem', '/usr/include',
'-isystem', '/usr/include/llvm',
'-I', './cpp/ycm',
'-I', './cpp/ycm/ClangCompleter',
]

flags_cpp = [
'-Wall',
'-Wextra',
'-Werror',
#'-Wc++98-compat',
'-Wno-variadic-macros',
'-fexceptions',
'-DNDEBUG',
'-DUSE_CLANG_COMPLETER',
'-x', 'c++',
'-std=gnu++11',
'-stdlib=libstdc++',
'-isystem', '/usr/include/c++/4.8.2',
'-isystem', '/usr/include/c++/4.8.2/x86_64-unknown-linux-gnu',
'-isystem', '/usr/include/c++/4.8.2/backward',
'-isystem', '/usr/local/include',
'-isystem', '/usr/lib/clang/3.4/include',
'-isystem', '/usr/include',
'-isystem', '/usr/include/llvm',
'-isystem', './cpp/BoostParts',
'-I', './cpp/ycm',
'-I', './cpp/ycm/ClangCompleter',
]


def DirectoryOfThisScript():
  return os.path.dirname( os.path.abspath( __file__ ) )


def MakeRelativePathsInFlagsAbsolute( flags, working_directory ):
  if not working_directory:
    return flags
  new_flags = []
  make_next_absolute = False
  path_flags = [ '-isystem', '-I', '-iquote', '--sysroot=' ]
  for flag in flags:
    new_flag = flag

    if make_next_absolute:
      make_next_absolute = False
      if not flag.startswith( '/' ):
        new_flag = os.path.join( working_directory, flag )

    for path_flag in path_flags:
      if flag == path_flag:
        make_next_absolute = True
        break

      if flag.startswith( path_flag ):
        path = flag[ len( path_flag ): ]
        new_flag = path_flag + os.path.join( working_directory, path )
        break

    if new_flag:
      new_flags.append( new_flag )
  return new_flags


def FlagsForFile( filename ):
  extension = os.path.splitext( filename )[1]
  if extension == '.c':
    flags = flags_c
  else:
    flags = flags_cpp
  relative_to = DirectoryOfThisScript()
  final_flags = MakeRelativePathsInFlagsAbsolute( flags, relative_to )

  return {
    'flags': final_flags,
    'do_cache': True
  }
