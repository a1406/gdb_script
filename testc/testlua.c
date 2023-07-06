#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#include <lualib.h>
#include <lauxlib.h>


int api_mul(lua_State* lua)
{
    lua_settop(lua, 2); // set the size of the stack to 2 and crop useless args

    int num = lua_tointeger(lua, 1);
    int num2 = lua_tointeger(lua, 2);
    
    lua_pushinteger(lua, num * num2);

	lua_getglobal(lua, "TEST_GLOBAL_INT");
	int v = lua_tointeger(lua, -1);
	printf("TEST_GLOBAL_INT = %d\n", v);

	lua_getglobal(lua, "TEST_GLOBAL_CHAR");	
	const char *s = lua_tostring(lua, -1);
	printf("TEST_GLOBAL_CHAR = %s\n", s);
	
	lua_pop(lua, 2);
    return 1;
}

struct test_bbb
{
	int type;
	char *str;
};

void test_print_str()
{
	char *aaa = "123456";
	struct test_bbb bbb;
	bbb.str = strdup("123456");
	printf("aaa = %s, bbb = %s\n", aaa, bbb.str);
}

int main(int argc, char *argv[])
{
	test_print_str();
	lua_State *L = luaL_newstate();
	if (L == NULL)
	{
		printf("create state failed!\n");
		exit(-1);
	}
	luaL_openlibs(L);
	lua_register(L, "mul", api_mul);
	
	int ret = luaL_loadfile (L, "testlua.lua");
	if (ret != 0)
	{
		printf("cannot load lua script! %d\n", ret);
		exit(-1);
	}
	
	ret = lua_pcall(L, 0, LUA_MULTRET, 0);
	if (ret != 0)
	{
		printf("cannot run lua script! %d\n", ret);
		exit(-1);
	}

	lua_close(L);
	return 0;
}
