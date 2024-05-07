# cffi-python-struct-example
Example of using CFFI Python library and getting and editing nested structures pointers

Need to have cffi python lib installed, with :
```commandline
pip3 install cffi
```
-- For MAC, can't do it with pipx you'll need to setup a virtualenv.

## Data Structures

### tes_morts.h
```C
typedef struct nested_s {
    char c;
} nested;

typedef struct tes_morts_s {

    int a;
    int b;
    nested nest;

} tes_morts;

tes_morts *init();
tes_morts *edit_and_ret_pointer(tes_morts *miam);
void edit(tes_morts *miam);
```

### tes_morts.c
```C
#include "tes_morts.h"

...

void edit(tes_morts *miam) {
    miam->a = 99;
    miam->b = -43;
    miam->nest.c = 'b';
}

tes_morts *edit_and_ret_pointer(tes_morts *miam) {
    miam->a = 88;
    miam->b = -41;
    miam->nest.c = 'o';
    return miam;
}
```
## Testing

1. First you need to compile as a shared library
2. Then just execute the `test_cffi.py` located in the current folder.

```commandline
gcc -I tes_morts.h -shared -o libmangetesmorts.so -fPIC tes_morts.c
```
```python
(venv) blurp blurp % python3 test_cffi.py
['BCharA', 'BVoidP', 'CData', 'CType', 'NULL', 'RTLD_GLOBAL', 'RTLD_LAZY', 'RTLD_LOCAL', 'RTLD_NODELETE', 'RTLD_NOLOAD', 'RTLD_NOW', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_apply_embedding_fix', '_apply_windows_unicode', '_backend', '_cached_btypes', '_cdef', '_cdef_version', '_cdefsources', '_embedding', '_function_caches', '_get_cached_btype', '_get_errno', '_included_ffis', '_init_once_cache', '_libraries', '_lock', '_new_types', '_parsed_types', '_parser', '_pointer_to', '_set_errno', '_typecache', '_typeof', '_typeof_locked', '_typeoffsetof', '_windows_unicode', 'addressof', 'alignof', 'buffer', 'callback', 'cast', 'cdef', 'compile', 'def_extern', 'distutils_extension', 'dlclose', 'dlopen', 'embedding_api', 'embedding_init_code', 'emit_c_code', 'emit_python_code', 'errno', 'from_buffer', 'from_handle', 'gc', 'getctype', 'getwinerror', 'include', 'init_once', 'list_types', 'memmove', 'new', 'new_allocator', 'new_handle', 'offsetof', 'release', 'set_source', 'set_source_pkgconfig', 'set_unicode', 'sizeof', 'string', 'typeof', 'unpack', 'verify']
<cdata 'tes_morts *' owning 12 bytes> ['a', 'b', 'nest']
<cdata 'nested &' 0x600003248030>
b'a'
88 -41 b'o'
99 -43 b'b'
```

you welcome habibi