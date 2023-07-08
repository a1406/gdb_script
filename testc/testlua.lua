function aaa(a, b)
    print('aaa')
    local t = bbb(a, b)
    return t
end
function bbb(a, b)
    print('bbb')
    local t = ccc(a, b)
    return t
end
function ccc(a, b)
    print('ccc')
    local t = ddd(a, b)
    return t
end
function ddd(a, b)
    int_c = mul(a, b)
    t = debug.traceback()
    print(t)
    return int_c
end


print("i am in testlua.lua")
TEST_GLOBAL_INT = 100
TEST_GLOBAL_CHAR = 'hello world'
int_a = 3
int_b = 5
aaa(int_a, int_b)

print("int_c = " .. int_c)
