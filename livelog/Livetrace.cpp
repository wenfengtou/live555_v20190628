#include "Livetrace.hh"

static void print_stackframe(void) {
     void * buffer[MAX_DEPTH];
     int depth = backtrace(buffer, MAX_DEPTH);
     char ** func_names = backtrace_symbols(buffer, depth);
     for (int i=0; i<depth; i++)
     {
         printf("Depth: %d, func name: %s\n", i, func_names[i]);
     }
}