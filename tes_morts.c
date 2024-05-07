#include "tes_morts.h"
#include <stdlib.h>

tes_morts *init() {
    tes_morts *blurp = malloc(sizeof(tes_morts));
    blurp->a = 1;
    blurp-> b = 2;
    blurp->nest.c = 'l';
    return blurp;
}

void edit(tes_morts *miam) {
    miam->a = 99;
    miam->b = -43;
    miam->nest.c = 'b';
}

tes_morts *edit_and_ret_pointer(tes_morts *miam) {
    miam->a = 88;
    miam->b = -41;
    miam->nest.c = 'o';
    return miam;
}