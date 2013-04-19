import sys
from .dll import _bind
from ctypes import c_int, c_byte, c_ubyte, c_ushort, c_short, c_uint, \
    c_longlong, c_ulonglong, cdll, c_size_t, c_void_p, c_char_p

SDL_FALSE = 0
SDL_TRUE = 1

SDL_bool = c_int
Sint8 = c_byte
Uint8 = c_ubyte
Sint16 = c_short
Uint16 = c_ushort
Sint32 = c_int
Uint32 = c_uint
Sint64 = c_longlong
Uint64 = c_ulonglong

_libc = None
if sys.platform == "win32":
    _libc = cdll.msvcrt
else:
    _libc = cdll.LoadLibrary("libc.so")
SDL_malloc = _bind("SDL_malloc", [c_size_t], c_void_p, _libc.free)
SDL_calloc = _bind("SDL_calloc", [c_size_t, c_size_t], c_void_p, _libc.calloc)
SDL_realloc = _bind("SDL_realloc", [c_void_p, c_size_t], c_void_p, _libc.realloc)
SDL_free = _bind("SDL_free", [c_void_p], None, _libc.free)
SDL_getenv = _bind("SDL_getenv", [c_char_p], c_char_p, _libc.getenv)
SDL_setenv = _bind("SDL_setenv", [c_char_p, c_char_p, c_int], c_int)
SDL_abs = abs
SDL_min = min
SDL_max = max
SDL_memset = _bind("SDL_memset", [c_void_p, c_int, c_size_t], c_void_p, _libc.memset)
SDL_memcpy = _bind("SDL_memcpy", [c_void_p, c_void_p, c_size_t], c_void_p, _libc.memcpy)