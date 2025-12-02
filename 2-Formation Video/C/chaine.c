#include <stdio.h>
#include <string.h>

/*
    -> Une chaîne est un tableau de caractères

    -> '\0' est le dernier char dans une chaine de caracteres
    
    -> signed char mot = "bonjour";
       ou bien :
       signed char mot ={'b', 'o', 'n', 'j', 'o', 'u', 'r'};
    
    -> printf("%s", mot);

    -> ce qu'on a fait avec les tableaux marche avec un TABLEAU DE CHAINE DE CARACTERE

    -> scnaf("%s", mot);        par essai = elle prend pas la chaine apres un espace ' ' 
    -> printf("%ss", mot);
     
*/

/*
    la bibliotheque string.h

    ->strcpy(str1,str2); copy str2 into str1  //en info en generale la destination avant la source 

    ->strlen(str1, str2) : retourne la langeure d'une chaine,

    ->strcat(str1,str2) : concatiner deux chaines "fusioner x)" 
      syntaxe :  char *strcat(char *destination, const char *source)

    ->strcmp(str1,str2) comparer deux chaines lexicographiquement, genre dictionnaire , et elle retourne soit 
       0 ei egaux
       1 si str1>str2 et  -1 si str1<str2

    
    ->strstr(str1, str2) chercher une chiane dans une autre chaine, elle retourne NULL si elle existe pas 
        sinon un pinteur de la chaine t

    ->strchr(str1, char) : cherche première occurance du char, elle retourne le pinteur vers la chaine qui
        commence par char jusqu'à la fin de str1.

    -> sprintf(destination, source, tailleSource) :  ecrire dans une chaine directement
    -> char *strncat(char *dest, const char *src, size_t n) concatiner en fin de dest avec la chaine de longeur 1
*/
/*
    NOTES TRES IMPORTANTES :

    -> Arrays and strings are second-class citizens in C; they do not support the assignment operator once it is declared.

    -> avec scanf() on peut juste lire le premier mot avant white space:
       sol :
       -> fgets(name, sizeof(name), stdin); // read string // line
       on utilise pas puts a cause du buffer overflow.
       ->puts(str); affiche la chaine dans le nextline

    -> il faut jamias affecter une chaine a un char *str, car le str pointe vers le debut bloc saura pointé sur debut dautre bloc contient
       la chaine affecte !!!!!! utillise strcpy() !!!!

   -> "C" : est une chaine a deux blocs a un seul caractere.
   
   -> la fonction char *strncat(char *dest, const char *src, size_t n) concatiner en fin de dest avec la chaine de longeur 1 
      tip : pour passer un caractere on lui donne juste le pointeur vers le char et size_t =1
    
    -> initialiser une chine à la chaine vide <=> *str='\0';
*/
/*
    Observations : 

*/


int main(void)
{
   signed char mot[256];
   char *word = "hello everyone :)";

   printf("%s\n", word);
   printf("taille = %d\n", strlen(word));


   /* la manipulation des chaines des caracteres est tres interessante */
    return 0;
}




