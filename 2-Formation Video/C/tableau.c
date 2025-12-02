#include <stdio.h>
#include <stdlib.h>
#define taille_tab 5


/*
    un tableau est une structure de donne de stocker plusieurs variables du meme type.
*/

/*
    int tableau[5];       ei déclaration d'un tableau statique.
    int tableau[5] = {0}  ei toutes les cases vaux 0.
    int tableau[5] = {4}  ei le premier élément vaut 4, le reste 0.

    en generale les elements non introduits sont par default a zero, sinon c'est aléatoire si 
    on introduit aucun element  
*/

/*
    dans la création des fonctions le paramétre tableau on peut le définir 
     ->soit : int par[]
     ->soit : int *tab

    le C voit pas de différence syntaxique entre tab[i] et *(tab+i)
*/   

/*
    tableau sert tout simplement à l'adresse du tableau 
*/

/*
    le mot static dans une fonction garde la variable apres lappel de la fonction et ne la détruit pas.
*/

/*
    on peut creer un tableau a plusieurs dimensions

*/

void printTab(int tab[], int taille)
{
    for (int i=0; i<taille; i++)
    {
        printf("tab[%d] = %d\n", i, tab[i]);
    } 
}



const char *merci = "hello";

int main(void)
{   
    int tab2D [2][2] ={
                         {1,2},
                         {3,4}
                        };
    return 0;
}