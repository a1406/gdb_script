all: test1 testlua testlua2 testlua3 testlua4

LUA_SRC=/home/jack/gitroot/lua5.1/lua-5.1.5/src
LUA_SRC2=/home/jack/gitroot/lua5.3/lua-5.3.6/src
LUA_SRC3=/home/jack/gitroot/openresty/openresty-1.21.4.1/build/LuaJIT-2.1-20220411/src

JIT_C_FLAGS=-I/home/jack/gitroot/openresty/openresty-1.21.4.1/build/luajit-root/usr/local/openresty/luajit/include/luajit-2.1 -pipe  -O -W -Wall -Wpointer-arith -Wno-unused-parameter -g -O2 -DNDK_SET_VAR -DNDK_UPSTREAM_LIST -DNDK_SET_VAR -DNDK_SET_VAR -DNDK_SET_VAR -DNDK_SET_VAR
JIT_LD_FLAGS=-Wl,-rpath,/usr/local/openresty/luajit/lib -Wl,--require-defined=pcre_version -Wl,-E -Wl,-E -lcrypt -L/home/jack/gitroot/openresty/openresty-1.21.4.1/build/luajit-root/usr/local/openresty/luajit/lib -lluajit-5.1 -lm -ldl -lluajit-5.1 -lm -ldl -lpcre -lssl -lcrypto -lz -Wl,-E


test1: test1.c
	gcc -g -O0 -o test1 test1.c

testlua: testlua.c
	gcc -g -O0 -I${LUA_SRC}  -o testlua testlua.c ${LUA_SRC}/liblua.a -lm
testlua2: testlua.c
	gcc -g -O0 -I${LUA_SRC2}  -o testlua2 testlua.c ${LUA_SRC2}/liblua.a -lm
testlua3: testlua.c
	gcc ${JIT_C_FLAGS} -I${LUA_SRC3} -o testlua3 testlua.c ${JIT_LD_FLAGS} 

testlua4: testlua.c
	gcc -g -O0 -DUSE_JIT -I${LUA_SRC3}  -o testlua4 testlua.c ${LUA_SRC3}/libluajit.a -lm

clean:
	rm -f test1 testlua testlua2 testlua3 testlua4
