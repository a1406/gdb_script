all: test1 testlua

test1: test1.c
	gcc -g -O0 -o test1 test1.c

testlua: testlua.c
	gcc -g -O0 -o testlua testlua.c -llua

clean:
	rm -f test1 testlua
