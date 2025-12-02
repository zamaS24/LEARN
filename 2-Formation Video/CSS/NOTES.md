
> # *Notes prises durant le suivi de la formation CSS de la chaîne fomation vidéo*  

> **SOMMAIRE**
> - [Introduction Design](#introduction-design)
> - [Styliser Text 1/2](#styliser-text-1/2)

---
<br>  

## **Introduction Design** 

**Un commentaire**  
` /* Ceci est un commentaire */`  

Un sélécteur prend un élément particulier de la page pour lui appliquer un style

~~~ css
    
    selecteur { /* Ceci est un commentaire */` 
    property: value; 
    }

    #id { /* id est unique, class est partagé */
    }

    .class{
    }

    selecteur#id {/* ceci veut dire les deux, le selecteur avec id */          
    }

    selecteur1 selecteur2#id {
        /* des qu'on trouve le selecteur1 dans le selecteur2 */
    }

    balise[att="val"]{

    }
~~~
---
<br>  

## **STYLISER TEXT 1/2**   
+ __`font-style`__ : normal, italic, ...etc  
+ __`font-variant`__ : small-caps  __*ceci rend le tout en majuscule. Et les majuscules deviennent plus grandes*__  
+ __`font-weight`__ :  bold, lighter, ...etc  __*Exemple: changer le font weight de h1 vers normal*__  
+ __`font-size`__ : 16px, 70%...etc __*la taille de la police pixel, pourcentage*__

    + __`em`__ et __`ex`__ : __*dans font-size de plus de pixels et pourcentage on peut utiliser em et ex, 1em veut dire 100% la taille de l'élément parent*__  
    + **Quelques attributs résérvés**  
        - `xx-small tres petit`
        - `x-small` 
        - `medium`
        - `large`
        - `x-large`
        - `xx-large`

+ __`line-heaight`__ : 
+ __`font-family`__ :


### **factorisation des attributs**
ON peut faire genre   


`code blocks here right `


## Flex Box

Tout d'abord dans container il faut mettre display flex dans tout le debut

~~~css
.container{
    display:flex;
}
~~~ 
