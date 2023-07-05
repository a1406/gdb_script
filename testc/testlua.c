#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#include <lualib.h>
#include <lauxlib.h>


int main(int argc, char *argv[])
{
	lua_State *L = luaL_newstate();
	if (L == NULL)
	{
		printf("create state failed!\n");
		exit(-1);
	}
	luaL_openlibs(L);

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
