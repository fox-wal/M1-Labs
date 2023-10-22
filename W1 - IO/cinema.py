print("Welcome to the cinema!\n")

totalCost = 0

# Popcorn
choice = input('Would you like some popcorn? [Y/N]\n')
if choice.upper() == 'Y':
    choice = int(input('''What type of popcorn would you like? [Enter the item number]
    [0] Sweet - £3.99
    [1] Salted - £4.25
    [2] Sweet and salted - £4.30\n'''))
    if choice == 0:
        totalCost += 399
    elif choice == 1:
        totalCost += 425
    else:
        totalCost += 430

# Showing
choice = input('Have you purchased tickets already? [Y/N]\n')
if choice.upper() == 'N':
    choice = int(input('''Which showing would you like tickets for? [Enter showing number]
    [0] Beauty and the Beast          20:41    £27.50
    [1] Lionheart                     22:13    £12.30
    [2] Dune                          23:09    £14.75
    [3] Pixies                        01:30    £18.90
    [4] Frankie the teenage vampire   03:27    £13.89
    [5] Dune                          04:52    £11:75\n'''))

    numberOfTickets = int(input('How many tickets would you like?\n'))

    ticketCost = 0

    if choice == 0:
        ticketCost = 2750
    elif choice == 1:
        ticketCost = 1230
    elif choice == 2:
        ticketCost = 1475
    elif choice == 3:
        ticketCost = 1890
    elif choice == 4:
        ticketCost = 1389
    else:
        ticketCost = 1175

    totalCost += ticketCost * numberOfTickets

# Output total
if totalCost != 0:
    print('\nThat\'ll be £', totalCost // 100, '.', totalCost % 100, ', please.\n*Card beeps*\nThank you!', sep='')
print('Enjoy the film!')