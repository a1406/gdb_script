# pprinter.py
import ctypes

def get_value(v):
    if not v:
        return 'None'

    t = v['tt']
    if t == 3:
        return v['value']['n']
    if t == 1:
        return v['value']['b']
    if t == 4:
        return get_str_data(v).string()
    if t == 0:
        return 'Nil'
    return 'type: ' + t
    
def calc_str_hash(str_):
    h = len(str_)    
    l = h
    step = (l>>5)+1    
    l1 = l
    while l1 >= step:
        a = ctypes.c_uint32(h<<5).value
        b = ctypes.c_uint32(a + (h >> 2)).value
        c = ctypes.c_uint32(b + ord(str_[l1-1])).value
        h = h ^ c;
        # print("l1 = %s" % l1)
        # print("str = %s" % argv[0][l1-1])            
        # print("ord = %s" % ord(argv[0][l1-1]))
        # print("h = %s" % h)
            
        l1 = l1 - step
    return h

def get_str_data(str_):
    pointer = str_['value']['gc']
    p = pointer.cast(gdb.lookup_type('TString').pointer())
    p = p + 1
    p = p.cast(gdb.lookup_type('char').pointer())
    return p

def strlen(str_):
    if type(str_) == type('str'):
        return len(str_)
    index = 0
    while str_[index]:
        index = index + 1
    return index


def strcmp(str1, str2):
    if type(str1) == type(gdb.Value(0)):
        # str1 = str1.format_string(address=False)
        str1 = str1.string()
    if type(str2) == type(gdb.Value(0)):        
        str2 = str2.string()
    index = 0
    len1 = len(str1)

    # print("len[%s][%s], data[%s][%s]" % (len1, len(str2), str1, str2))

    if len1 != len(str2):
        # print('len1[%s] != len2[%s]' % (len1, len(str2)))
        return False

    while index < len1:
        if str(str1[index]) != str(str2[index]):
            # print('index %s: str1[%s] != str2[%s]' % (index, str1[index], str2[index]))              
            return False
        index = index + 1
    return True


def get_hash_value(t, h, k):
    if type(k) == type(gdb.Value(0)):
        k = k.string()
    hash = calc_str_hash(k)
    h = t['value']['gc'].dereference()['h']
    size_ = 1 << h['lsizenode']
    hash2 = hash & (size_ - 1)
    # print("size = %s" % size_)
    node = h['node'][hash2]
    # next_ = node['i_key']['nk']
    next_ = node
    k_ = get_str_data(node['i_key']['nk'])
    
    while True:
        if strcmp(k_, k):
            # get value
            v = node['i_val']
            return v
        node = node['i_key']['nk']['next']
        if not node:
            return None
        node = node.dereference()
        k_ = get_str_data(node['i_key']['nk'])        
    return None

    
class print_lua(gdb.Command):

    """Move breakpoint
    Usage: print_lua LUA_STATE LUA_GLOBAL_VAR
    """

    def __init__(self):
        super(self.__class__, self).__init__("print_lua", gdb.COMMAND_USER)

    def invoke(self, args, from_tty):
        argv = gdb.string_to_argv(args)
        if len(argv) != 2:
            raise gdb.GdbError('输入参数数目不对，help print_lua以获得用法')
        L = gdb.parse_and_eval(argv[0])
        hash = calc_str_hash(argv[1])
        t = L.dereference()['l_gt']
        h = t['value']['gc'].dereference()['h']
        size_ = 1 << h['lsizenode']
        hash2 = hash & (size_ - 1)
        # print("size = %s" % size_)
        node = h['node'][hash2]
        k_ = node['i_key']['nk']
        # tt = k_['tt']
        # # tt2 = k_['value']['gc'].dereference()['ts']
        # pointer = k_['value']['gc']
        # p = pointer.cast(gdb.lookup_type('TString').pointer())
        # p = p + 1
        # p = p.cast(gdb.lookup_type('char').pointer())
        # # p = k_['value'].reference()
        
        # p = get_str_data(k_)
        # print('p = %s' % p)

        v = get_hash_value(t, h, argv[1])
        print("v = %s" % get_value(v))

        
        # p = p + 24
        # print('p = %s' % p)
        
        # print('tt = %s' % tt)
        # print("final hash = %s" % hash)            

print_lua()


class print_str(gdb.Command):

    # 3. docstring里面的文本是不是很眼熟？gdb会提取该类的__doc__属性作为对应命令的文档
    """Move breakpoint
    Usage: print_lua LUA_STATE LUA_GLOBAL_VAR
    """

    def __init__(self):
        # 4. 在构造函数中注册该命令的名字
        super(self.__class__, self).__init__("print_str", gdb.COMMAND_USER)

    def invoke(self, args, from_tty):
        aaa = gdb.parse_and_eval('aaa')
        aaa = aaa.cast(gdb.lookup_type('char').pointer())

        bbb = gdb.parse_and_eval('bbb')
        bbb = bbb['str']
        bbb = bbb.cast(gdb.lookup_type('char').pointer())        
        # print('aaa.type = %s' % type('aaa'))
        # print('len = %s' % strlen(aaa))
        # print('aaa = %s' % aaa)
        # if aaa == '123456':
        #     print('aaa == 123456')
        # else:
        #     print('aaa != 123456')

        # bbb = gdb.parse_and_eval('bbb')
        # bbb_str = bbb['str']

        eq = strcmp(aaa, bbb)
        print('eq = %s' % eq)

        eq = strcmp(aaa, '123456')
        print('eq = %s' % eq)

        eq = strcmp(aaa, '1234567')
        print('eq = %s' % eq)
        
print_str()


