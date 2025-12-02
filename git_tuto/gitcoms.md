# List of git commands and how to use it

### What's git ?
```
Git c'est pour la gestion de versions, il n'est pas destiné seulement pour les developpeurs. 
```

### Basic configuration
Voir le fichier `.gitconfig` dans users/monms
```
git config --global user.name "omarihamza"
git config --global user.email "omarihamza2000@gmail.com"
```

<br>  

## Basic commands
```
>$ git init 
>$ git add <nomfichier>
>$ git commit -m "Le message qu'on veut ecrire".
>$ git add --all * : préparer à sauvegarder tous les fichiers 
>$ git commit -a -m "mon message"  : ajouter le fichier en questions et le commiter. 
>$ git mv <fichier> <nouveau>   : déplacer renomer le fichier. 
>$ git rm <fichier> : supprimer le fichier. 
```

## \$ git log 
```
C'est pour voir l'historique 
    >$ git log 
    >$ git log <branch-name>
    >$ git log --graph
    >$ git log -- <file>
```


> :bulb: **INFO**   
> some informations  