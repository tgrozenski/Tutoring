#include<stdio.h>
#include<stdlib.h>

typedef struct {
    char * name;
    int num_tickets;
    int time_arrival;
    int num_line;
} Customer;

// function to make a customer using dynamic memory allocation
Customer * make_customer(char * name, int num_tickets, int time_arrival, int num_line){
    if (1 > sizeof(name)|| sizeof(name) > 15 ) {
        puts("Name must be between 1 and 15 characters");
        return NULL;
    }
    if (num_tickets < 1 && time_arrival < 1 && num_line < 1){
        puts("Invalid input");
        return NULL;
    }
    //allocate memory for a Customer
    Customer * customer  = (Customer *)malloc(sizeof(Customer));
    customer->name = name;
    customer->num_tickets = num_tickets;
    customer->time_arrival = time_arrival;
    customer->num_line = num_line;

    return customer;
}

// function to print customer
void customer_info(Customer * customer){
    printf("%s left the counter at time %d from line %d.", customer->name, customer->time_arrival, customer->num_line);
}