#include <stdio.h>
#include <stdlib.h>

struct node{
    int value;
    struct node * next;
};

void print_list(struct node * list);

int main()
{
    struct node * first = NULL;
    int number;

    while(1){
        printf("Insert a number (-1 to exit):");
        scanf("%d", &number);
        if(number == -1)
            break;

      temp = malloc(sizeof(struct node));
        temp->value = number;
        
        if(first == NULL){
            first = temp;
            first->next = NULL;
        }
        else{
            temp->next = first;
            first = temp;
        }

        return 0;
}

void print_list(struct node * list)
{
    struct node * current;
    printf("List is: ");

    current = list;
    while(current != NULL){
        printf("%d ", current->value);
        current = current->next;
    }
    printf("/n/n");
}

