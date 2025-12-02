#include <stdio.h>
#include <stdlib.h>
/*
    ->fopen(<fichier>, <mode_ouverture>) : r (lecture seule, fichier doit exister)
                                           w (ecriture seule)
                                           a (ajout fin fichier)
                                           r+(lecture/ecriture, doit exister)
                                           w+(lecture/ecriture, supprime contenu)
                                           a+(ajout lecture/ecriture, fin de fichier)
    ->fclose(<fichier>) : fermer le fichier
    ->feof(<fichier>) : tester la fin d'un fichier 

    [LECTURE]
    ->fgetc(<fichier>) : lire un caractere
    ->fgets(<chaine>, <taille_chaine>, <fichier>) :


    [ECRITURE]
*/
/*
    -> FILE est une structure fichier dans le langage c
    -> EOF est le caratere de fin de fichier ou en cas de erreur de lecture
       EOF = -1
*/
int main(void)
{
    FILE *fic = fopen("fichierText.txt","r"); // le mode d'ouvertir 
    int lettre;
    signed char texte [256];
    
    FILE *Fichier = fopen("C:/Users/monms/Desktop/tous/goals.txt", "r");

    printf("\nPrinting the character : \n"); 
    lettre = fgetc(fic);
    printf("%c\n", lettre); 

    while(!feof(Fichier))
    {   //while ( lettre != EOF)
        lettre = fgetc(Fichier); 
        printf("%c", lettre); 
    }//*/

    fgets(texte, 255, fic);
    printf("\nPrinting the String right now :\n%s\n", texte);
     

    if(fic == NULL)  // Le cas ou le fichier ne s'ouvre pas. 
    exit(-1);


    fclose(fic);
    return 0;
}