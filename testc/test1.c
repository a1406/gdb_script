#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

typedef struct list_
{
	int data;
	struct list_ *next;
} list;

static list g_head;

int main(int argc, char *argv[])
{
	srandom(getpid());
    int list_num = 0;
	list_num = random() % 1000;
	list *pre_node = &g_head;

	for (int i = 0; i < list_num; ++i) {
		list *t = (list *)malloc(sizeof(list));
		pre_node->next = t;
		t->next = NULL;
		pre_node = t;
	}

	printf("list size = %d\n", list_num);

	return 0;
}
