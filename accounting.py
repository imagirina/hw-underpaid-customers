MELON_COST = 1.00
expected = None

def  print_customer_payments(orders):
    payments = open(orders)
    for line in payments:
        line = line.rstrip()
        id, name, melons, paid = line.split('|')        
        expected = int(melons) * MELON_COST        
        if expected != float(paid):
            payment_status = "overpaid" if expected < float(paid) else "underpaid"                        
            # if expected < float(paid):
            #     print(name + " has overpaid for the melons.")
            # else:
            #     print(name + " has underpaid for the melons.") 
            #            
            print(name + " has " + payment_status + " for the melons.")
            
            print(name + " paid $" + paid + ", expected to pay $" + str(expected) + ".\n")          

    payments.close()

print_customer_payments('customer-orders.txt')
