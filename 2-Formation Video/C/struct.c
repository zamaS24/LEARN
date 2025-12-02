#include <stdio.h>
#include <string.h>

struct homme
{
    signed char name[256];
    int age;
    char section;
};
/*
    Rassembler un ensemble de donnés 
*/
/*
    struct name
    {
        datatype1 ... name;
        ...
    };
    struct name str1 = {datatyê1, ...}


    typedef c'est de définir un nouveau type à partir d'un type déja connu(struct, int , ...etc)

    (*monPointeur).unChamp <=> monPointeur->unChamp
*/

/*
    enumeration : 
    enum {0,1,...etc}
*/

/*
union : comme struct sauf les differents types de donnes partage toute lespace memoire alloue par struct 
*/

/*
    Notes tres importantes:
     -> on peut passer struct comme entree a une fonction 
     -> on peut retourner struct comme sortie dune fonction
     -> une variable struct est une grande variable qui contiest des differents types
     
     -> adresse de str de type structname = adresse premier element de type1

     -> affectation :
         struct strname str;
         str = (strname){.att1 = val1, .att2 = val2, etc};  //attention aux parenthèses
         the adresse of str doesnt change
     
*/

typedef enum 
{
    false,
    true
}bool;

int main(void)
{
    struct homme *p; 

    //directement il faut le voir qu'on peut pas modifier directement dans une chaine de caractere ok !
    strcpy((*p).name, "homme haha"); 
    (*p).age  = 15;
    (*p).section ='B';

   /* p->age = 16; <=> (*p).age = 16;*/



    return 0;
}