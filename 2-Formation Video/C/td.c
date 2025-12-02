#include <stdio.h>

// Déclaration des prototypes :
int recMul(int,int);

// Déclarations des fonctions : 
int recMul(int a, int b)
{
    /*  
        Enoncé :
         si B est pair          A ∗ B = (A ∗ 2) ∗ (B/2)
         si B est impair        A ∗ B = A ∗ (B − 1) + A
         et dans tous les cas   A ∗ 0 = 0
    */

    if(b == 0)
     return 0;

    if(b%2 == 0)
     return  recMul((a*2), (b/2));

    if(b%2 == 1) 
     return a + recMul(a,(b-1));    
}


int main(void)
{
    int a,b;

    printf("Donner A : ");  scanf("%d", &a);
    printf("Donner B : ");  scanf("%d", &b);

    printf("Recmul(%d,%d) = %d\n", a, b, recMul(a,b));

    printf("A*B = %d\n", a*b);
    return 0;
}


