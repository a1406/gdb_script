all: test1 testlua

LUA_SRC=/home/jack/gitroot/lua5.1/lua-5.1.5/src

test1: test1.c
	gcc -g -O0 -o test1 test1.c

testlua: testlua.c
	gcc -g -O0 -I${LUA_SRC}  -o testlua testlua.c ${LUA_SRC}/liblua.a -lm

clean:
	rm -f test1 testlua
