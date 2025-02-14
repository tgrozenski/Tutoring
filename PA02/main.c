#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include"Customer.h"


int main() {
    Customer * customer = make_customer("HUDSON", 3, 150, 1);
    customer_info(customer);
}