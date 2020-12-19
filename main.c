#include <stdio.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <fcntl.h>
#include <stdlib.h>

typedef struct file {
	char name[10];
	char *content;
} file;

typedef struct directory {
	char name[10];
	int childnum;
	struct file *child;
} directory;

struct myfs {
	int sectorsize;
};

int main(){
	int fd = open("./flag.png", 0);
	char *content = (char *)malloc(sizeof(char) * 100);
	file imgfile1 = {"flag.png", 0};
	directory rootdir = {"testdir", 0, &imgfile1};
	printf("name = %s\n",rootdir.name);
	printf("name = %s\n",rootdir.child->name);
	return 0;
}
