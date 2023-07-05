# pprinter.py
class list_size(gdb.Command):

    # 3. docstring里面的文本是不是很眼熟？gdb会提取该类的__doc__属性作为对应命令的文档
    """Move breakpoint
    Usage: list_size LIST_HEAD
    Example:
        (gdb) list_size g_head
    """

    def __init__(self):
        # 4. 在构造函数中注册该命令的名字
        super(self.__class__, self).__init__("list_size", gdb.COMMAND_USER)

    # 5. 在invoke方法中实现该自定义命令具体的功能
    # args表示该命令后面所衔接的参数，这里通过string_to_argv转换成数组
    def invoke(self, args, from_tty):
        argv = gdb.string_to_argv(args)
        if len(argv) != 1:
            raise gdb.GdbError('输入参数数目不对，help list_size以获得用法')
        # 6. 使用gdb.execute来执行具体的命令
        # gdb.execute('delete ' + argv[0])
        # gdb.execute('break ' + argv[1])
        i = 0
        head_ = gdb.parse_and_eval(argv[0])
        next_ = head_['next']
        while next_:
            i = i + 1
            next_ = next_.dereference()['next']

        print("count: %s" % i)
        # print("count: %d\n" % (i))
        # result = 'count: ' + str(i)
        # gdb.execute('p '  + result)
        

# 7. 向gdb会话注册该自定义命令
list_size()

# class ListPrinter:
#     def __init__(self, val):
#         "构造函数接收一个表示被打印的Buffer的gdb.Value"
#         self.val = val

#     def to_string(self):
#         """必选。输出打印的结果。
#         由于gdb会在调用to_string后调用children，这里我们只输出当前的使用程度。
#         具体的数据留在children函数中输出。
#         """
#         i = 0
#         next_ = self.val['next']
#         while next_:
#             i = i + 1
#             next_ = next_.val['next']

#         return "count: %d\n" % (i)

#     # def _iterate(self, pointer, size, encoding):
#     #     # 根据encoding决定pointer的类型
#     #     typestrs = ['int8_t', 'int16_t', 'int32_t', 'int64_t']
#     #     pointer = pointer.cast(gdb.lookup_type(typestrs[encoding]).pointer())
#     #     for i in range(size):
#     #         elem = pointer.dereference()
#     #         pointer = pointer + 1
#     #         yield ('[%d]' % i, elem)

#     # def children(self):
#     #     """可选。在to_string后被调用，可用于打印复杂的成员。
#     #     要求返回一个迭代器，该迭代器每次迭代返回（名字，值）形式的元组。
#     #     打印出来的效果类似于“名字 = 值”。
#     #     """
#     #     return self._iterate(self.val['data'],
#     #                          int(self.val['used']), int(self.val['encoding']))

#     # def display_hint(self):
#     #     """可选。影响输出的样式。
#     #     可选值：array/map/string。
#     #     返回array表示按类似于vector的方式打印。其它选项同理。
#     #     """
#     #     return 'array'

# def lookup_list(val):
#     """val是一个gdb.Value的实例，通过type属性来获取它的类型。
#     如果类型为Buffer，那么就使用自定义的BufferPrinter。
#     """
#     if str(val.type) == 'list_':
#         return ListPrinter(val)
#     return None

# gdb.pretty_printers.append(lookup_list)    
