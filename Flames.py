# FLAMES Game - Find relationship outcome based on two names
# Rules: Count common letters, then eliminate letters based on FLAMES list

def play_flames():
    # Get names from users
    name1 = input("Enter the First person's Name: ").lower().replace(" ", "")
    name2 = input("Enter the second person's Name: ").lower().replace(" ", "")
    
    # FLAMES options
    flame_list = ['Friend', 'Love', 'Affection', 'Marriage', 'Enemy', 'Sister']
    
    # Convert to lists for easy manipulation
    list1 = list(name1)
    list2 = list(name2)
    
    # Remove common letters
    for letter in list1[:]:  # Create a copy to iterate
        if letter in list2:
            list1.remove(letter)
            list2.remove(letter)
    
    # Count remaining letters
    count = len(list1) + len(list2)
    
    print(f"\n{name1.title()} + {name2.title()}")
    print(f"Remaining letters count: {count}")
    
    # Eliminate from FLAMES list using count
    while len(flame_list) > 1:
        # Eliminate every count-th element
        index = (count - 1) % len(flame_list)
        flame_list.pop(index)
    
    print(f"Result: {flame_list[0]} ❤️")
    
    # Ask if user wants to play again
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again == 'yes' or again == 'y':
        play_flames()

# Run the game
if __name__ == "__main__":
    play_flames()