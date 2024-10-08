def vacuum_world():
    # Initializing goal_state: 0 indicates Clean, 1 indicates Dirty
    goal_state = {'A': '0', 'B': '0'}
    cost = 0

    # User input: location of vacuum
    location_input = input("Enter Location of Vacuum (A/B): ").upper()
    
    # User input: status of the location vacuum is placed
    status_input = input(f"Enter status of {location_input} (1 for Dirty, 0 for Clean): ")
    
    # Status of the other room
    status_input_complement = input(f"Enter status of the other room (1 for Dirty, 0 for Clean): ")

    print("Initial Location Condition:", str(goal_state))

    # Logic based on the vacuum's starting location
    if location_input == 'A':
        print("Vacuum is placed in Location A")
        
        if status_input == '1':  # If Location A is Dirty
            print("Location A is Dirty.")
            goal_state['A'] = '0'  # Clean the room
            cost += 1  # Cost for cleaning
            print("Cost for CLEANING A:", cost)
            print("Location A has been Cleaned.")
        
        if status_input_complement == '1':  # If Location B is Dirty
            print("Location B is Dirty.")
            print("Moving RIGHT to Location B.")
            cost += 1  # Cost for moving right
            print("Cost for moving RIGHT:", cost)
            goal_state['B'] = '0'  # Clean Location B
            cost += 1  # Cost for cleaning
            print("Cost for SUCK:", cost)
            print("Location B has been Cleaned.")
        else:
            print("Location B is already clean. No action needed.")
    
    else:  # Vacuum starts at Location B
        print("Vacuum is placed in Location B")
        
        if status_input == '1':  # If Location B is Dirty
            print("Location B is Dirty.")
            goal_state['B'] = '0'  # Clean Location B
            cost += 1  # Cost for cleaning
            print("Cost for CLEANING B:", cost)
            print("Location B has been Cleaned.")
        
        if status_input_complement == '1':  # If Location A is Dirty
            print("Location A is Dirty.")
            print("Moving LEFT to Location A.")
            cost += 1  # Cost for moving left
            print("Cost for moving LEFT:", cost)
            goal_state['A'] = '0'  # Clean Location A
            cost += 1  # Cost for cleaning
            print("Cost for SUCK:", cost)
            print("Location A has been Cleaned.")
        else:
            print("Location A is already clean. No action needed.")
    
    # Goal State and Performance
    print("GOAL STATE:", goal_state)
    print("Performance Measurement (Total Cost):", cost)

# Calling the function
vacuum_world()



