#Function for swap nibble 
def swap_nibbles(number):
    # 0x0F is lower bit 00001111 perform AND operation with number and shift left
    # 0xF0 is upper bit 11110000 perform AND operation with number and shift right
    return (number & 0x0F)<<4 | (number & 0xF0)>>4 

#main
while True:
    try:
        number=int(input("Enter the number"))
        #invoke swap_nibbles method
        swapping_nibbles=swap_nibbles(number)
        #print swapping nibbles
        print("Swapping Nibble of number {0} is {1}".format(number,swapping_nibbles))
        break
    except ValueError:
        print("Plz enter valid number") 