<?php
    /*Comment this later 
-ON go to php for windows 
-ON telecharge le thread safe
-Extraire et mettre dans c et changer le nom  <nom version>
-faire les modificaations: Php ne fonctionnera pas tout seul, il s'agit de 
l'interpreteur, il s'agit de mettre de lire les fichiers php et executer
par contre comme on utilise un serveur http en particulier on doit charger
le moduele php. 
donc on fait les modifications: 
    -aller dans le doosier php 
    - le production vs developement : 
        production visible par public et afficher pas les arreurs pour que les pirates ne exploites pas les erreurs
        developement pour developement genre en localhost. 
        -modifer php.ini-development vers php.ini
    - On deplace le fichier php.ini (ctr x) on le met dans le repertoire de apache
-Il nous faut aussi la DLL
    -> aller dans php8 puis recuperer le fichier php8ts.dll 
    ->on va le copier 

-> maintenant editer le apach 
    ->dossier apach 
    -> dosiier conf 
    -> httpd.conf 
    ->aller en fin de fichier et ajouter: 
        -># PHP 8 
          AddHandler application/x-httpd-php .php
          AddType application/x-httpd-php .php .html
          LoadModule php_module "c:/php-8.1.4/php8apache2_4.dll"
          PHPiniDir "c:/php-8.1.4"
          */ 