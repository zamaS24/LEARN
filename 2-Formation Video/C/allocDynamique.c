#include <stdio.h>
#include <stdlib.h>

/*
    -> malloc()                         : alloue dynamiquement une zone mémoire
    -> sizeof(type)                     : retourne la taille en octet du type
    -> exit(1)                          : sortir du programme et ne retourne rien.
    -> free(<donne alloue>)             : libère la mémoire alloué dynamiquement 
    -> calloc(<donne>, <taille en octe>): alloue et initialise tout a zero
    -> realloc(<donne>,<nouv_taille>)   : reallouer de la taille en un allouement deja fait 
*/

int main(void)
{
    int nbr;
    int *etudiant;

    printf("Donner le nombre d'etudiants \n");
    scanf("%d", &nbr);

    etudiant = malloc(sizeof(int)*nbr);

    etudiant = realloc(etudiant, sizeof(int)*(nbr+5));
    free(etudiant);


    
    return 0;
}