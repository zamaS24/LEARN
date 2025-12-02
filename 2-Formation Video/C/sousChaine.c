/********************************************************************************/
/*                                                                              */
/* On assume que l'utilisateur nous fournit :                                   */
/*                                          -> chaines de longeurs <= 50        */
/*                                                                              */
/*                                                                              */
/********************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Définition d'un booléen : 
typedef enum 
{
    false,
    true
}Bool;

// Déclaration des prototypes :
char* creerChaine(int);
Bool sousChaine(char *, char*);
void programme(void);


// Déclaration des fonctions :
char* creerChaine(int longeur)
{
    char *chaine = malloc(sizeof(char)*(longeur+1));
    *chaine ='\0';

    return chaine;
}

Bool sousChaine(char *chaine1, char *chaine2)
{
    int cmp=1; 
    for(int i=0; i<strlen(chaine1); i++)
    {
        if(chaine2[0] == chaine1[i])
        {
            if (strlen(chaine2) > strlen(chaine1)- i)
            return false;  // pas la peine de verifier car y a même pas l'espace pour qu'elle soit existe dans chaine1.

            for(int j=1; j<strlen(chaine2); j++)
            {
                if (chaine2[j] == chaine1[i+j])
                 cmp++;
            } 

            if(cmp == strlen(chaine2))
            return true;
        }
    }

    return false;
}

void programme(void)
{
    char *buffer = creerChaine(50);
    printf("Entreer les deux chaines, attention les deux chaines doivent y etre de longeur <=50!\n");

    printf("Entrere chaine1 : ");
    scanf("%s", buffer);
    char *chaine1 = creerChaine(strlen(buffer));
    strcpy(chaine1, buffer);

    printf("Entrer chaine2 : ");
    scanf("%s", buffer);
    char *chaine2 = creerChaine(strlen(buffer));
    strcpy(chaine2, buffer);

    if(sousChaine(chaine1, chaine2))
     printf("chaine2 incluse dans chaine1 !\n");
    else
     printf("chaine2 non incluse dans chaine1\n");
}

int main(void)
{

    programme();
    return 0;
}