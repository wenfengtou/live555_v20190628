#include <execinfo.h>
#include <stdio.h>

#define MAX_DEPTH 20

static void print_stackframe(void);