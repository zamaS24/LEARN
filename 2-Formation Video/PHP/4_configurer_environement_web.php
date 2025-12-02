<?php
/*
    -Le fichier de configuration c'est dans apache>conf>httpd.conf 
    - Options indexes
    - indexex c'est lister le fichier de repertoire s'il en trouve pas de fichier d'index. 
        genre en html on met index.html 
        en php en met index.php

    - ! Tres important WOW si on veut pas que les gens puissent lister le contenu on doit enlever l'option indexes

    mettre . AllowOverride All

    -directory index index.html 
    veut dire des qu'il trouve un fichier index.html il l'execute directement. 
    ajouter index.php

    -faire proprement les choses: 
    mettre le apache et php folders dans un folder que vous nommez MyWAMP
    modifier : 
                Define SRVROOT "c:/MyWAMP/Apache24"
                LoadModule php_module "c:/MyWAMP/php-8.1.4/php8apache2_4.dll"
                PHPiniDir "c:/MyWAMP/php-8.1.4"
                PHPiniDir "c:/MyWAMP/php-8.1.4"

    
    -faire des choses un peux plus propre, on peut utiliser le jeu de balise 
    transformer ce qu'il y a en dessous de # PHP 8 à ça 
        - LoadModule php_module "c:/MyWAMP/php-8.1.4/php8apache2_4.dll"

            <FilesMatch "\.php$">
                SetHandler application/x-httpd-php .php
            <FilesMatch>

            <IfModule php_module>
                PHPiniDir "c:/MyWAMP/php-8.1.4"
            </IfModule>

            <IfModule mime_module>
                 AddType application/x-httpd-php .php .html
            </IfModule>

    -Maintenant on y va a php.ini qui se trouve dans apache 
        -scroll jusqu'a error_reporting = E_ALL 
        on est dans mode developpeurs donc comme ça on va tout afficher les erreurs. Pour avoir un code php tres correcte ...etc 
        

*/