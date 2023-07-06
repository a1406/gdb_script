# pprinter.py
class print_lua(gdb.Command):

    # 3. docstring里面的文本是不是很眼熟？gdb会提取该类的__doc__属性作为对应命令的文档
    """Move breakpoint
    Usage: print_lua LUA_GLOBAL_VAR
    """

    def __init__(self):
        # 4. 在构造函数中注册该命令的名字
        super(self.__class__, self).__init__("print_lua", gdb.COMMAND_USER)

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
print_lua()

