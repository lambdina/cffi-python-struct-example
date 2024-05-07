#ifndef TES_MORTS_H
#define TES_MORTS_H

typedef struct nested_s {
    char c;
} nested;

typedef struct tes_morts_s {

    int a;
    int b;
    nested nest;

} tes_morts;

tes_morts *init();
tes_morts *edit_and_ret_pointer(tes_morts *miam);
void edit(tes_morts *miam);

#endif