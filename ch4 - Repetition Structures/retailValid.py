mark_up = 2.5
another = 'y'


while another == 'y' or another == 'Y':
    wholesale = float(input("Enter the item's" + " wholesale cost: $"))
    while wholesale < 0:
        print('ERROR: You have entered negative price')
        wholesale = float(input('Enter the correct'+' wholesale cost: $'))
    retail = wholesale * mark_up

    print('Retail price: $', format(retail, '.2f'), sep='')

    another = input('Do you have another item?' + ' (Enter y for yes): ')