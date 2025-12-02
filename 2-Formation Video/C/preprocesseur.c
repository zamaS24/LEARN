/* ceci est un fichier de theorie c tout */

/*
    -> le preprocesseur un programme qui s'execute avant le compilateur 

    -> la directive define:
       define quelque chose comme une constante
       ex : #define tva 20 

    -> #ifndef __BIBLI__H__
       #define __BIBLI__H__

       #endif  
       ceci nous permet de proteger le fichier ei l'inclusion des fixhiers d'une maniere infinie

    -> #le define sert pas pour la compilation

    -> exemple : on peut faire
      #define afficher printf
      puis afficher fais ce quelle la fait la fonction printf
      #define coucou printf("coucou")       donc coucou; 

      #en gros le define fait que le remplacement !!

    -> constante prédifinie du langage c :
      __FILE__ nom du fichier
      __LINE__ ligne de fichier 
      __DATE__ date de compilation 
      __TIME__  heure de compilation 
*/