from cffi import FFI

ffibuilder = FFI()

with open('./tes_morts.h', 'r') as fd:
    buf = fd.readlines()[2:-1]  # stripping because does not support ifndef directives
    ffibuilder.cdef(''.join(buf))

lib = ffibuilder.dlopen('./libmangetesmorts.so')
print(dir(ffibuilder))
opt = ffibuilder.new('tes_morts *', {
    'a': 1,
    'b': 2,
    'nest': {'c': 'a'.encode('utf-8')}  # needs byte of length 1
})
print(opt, dir(opt))  # <cdata 'tes_morts *' owning 12 bytes> ['a', 'b', 'nest']>
print(opt.nest)  # <cdata 'nested &' 0x600000600070>
print(opt.nest.c)  # b'a'
opt_b = lib.edit_and_ret_pointer(opt)
print(opt_b.a, opt_b.b, opt_b.nest.c)  # 88 -41 b'o'
lib.edit(opt)  # no need to catch ret value
print(opt.a, opt.b, opt.nest.c)  # 99 -43 b'b'

ffibuilder.dlclose(lib)