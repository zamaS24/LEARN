#include <stdio.h>
#include <stdlib.h>
#include <string.h> 

typedef int* Tab;
typedef Tab* Mat;

// declaration des prototypes
Tab creerTab(int);
Mat creerMat(int, int);
void displayMat(Mat, int, int);
void test(void);
// declaration des fonctions
Tab creerTab(int nbr_colonnes)
{
    Tab tab = malloc(sizeof(int)*nbr_colonnes);
    if(tab == NULL)
    {
        printf("Erreur allocation dynamiue !\n");
        exit(-1);
    }
    
    return tab;
}

Mat creerMat(int nbr_lignes, int nbr_colonnes)
{
    Mat mat = malloc(sizeof(Tab)*nbr_lignes);
    if (mat == NULL)
    {
        printf("Erreur allocation dynamique !\n");
        exit(-1);
    }

    for(int i=0; i<nbr_lignes; i++)
     mat[i] = creerTab(nbr_colonnes);

    return mat;
}

void displayMat(Mat mat, int lignes, int colonnes)
{
    for(int i=0; i<lignes; i++)
        for(int j=0; j<colonnes; j++)
            printf("mat[%d][%d] = %d\n", i, j, mat[i][j]);
}

void test(void)
{
    for(int i=0; i<10; i++)
        for(int j=0; j<5; j++)
            printf("[%d][%d]\n", i, j);
}

int main(void)
{   
    /*
        mat[lignes][colonnes]; ceco est memeilleure sentiment de tous les temps non ? 
    */
    int nbr_lignes = 5;
    int nbr_colonnes = 5;
    Mat mat = creerMat(nbr_lignes,nbr_colonnes);

    //afficher la matrice 
    displayMat(mat, nbr_lignes, nbr_colonnes);


    
    return 0;
}


