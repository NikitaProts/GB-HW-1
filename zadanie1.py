my_int = 1
my_float = 1.1
my_complex = complex(5, 6)
my_str = 'string'
spisok = list('Мой список')
my_tuple = tuple('Мой кортеж')
my_set = set('Множество')
my_frozenset = frozenset('Не изменяемое множество')
my_dict = dict(key_1='val_1', key_2='val_2')
var_bool = True
my_bytearray = bytearray(b"some text")
my_bytes = bytes([10, 20, 30, 40])
my_none = None

all_types_list = []
all_types_list.extend(
    (my_int,
     my_float,
     my_complex,
     my_str,
     spisok,
     my_tuple,
     my_set,
     my_frozenset,
     my_dict,
     var_bool,
     my_bytearray,
     my_bytes,
     my_none))
for i in all_types_list:
    print(type(i))
