#include <stdio.h>
#include <stdlib.h>

#define max 20


typedef enum
{
    false,
    true
}Bool;

typedef struct PileStatique
{
    int sommet;
    int tab[max];
}PileStatique;


// Declaration des prototypes :
PileStatique initPile(void);
void afficherPile(PileStatique);

// Declaration des fonctions : 
PileStatique initPile(void)
{
    PileStatique p; 
    p.sommet = -1;
    return p;
}


void afficherPile(PileStatique p)
{
    while(p.sommet != -1)
    {
        printf("[%d]\n", p.tab[p.sommet]);
        p.sommet--;
    }
}


 



int main(void)
{
  
    PileStatique p_test = initPile();
    p_test = (PileStatique) {.sommet = 3, .tab[0] =0, .tab[1] = 1, .tab[2]=2, .tab[3]=3};
    afficherPile(p_test);

    return 0;
}