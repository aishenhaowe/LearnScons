#include <stdio.h>
#include "add.h"
#include "test-lib.h"

int main(int argc, char **argv)
{
    test_lib_fun();

    printf("Test add, result:%d\n", add(1, 5));
    return 0;
}
