
def pit_stop_optimiser():
    """Function for calculating the total pit time and the percentage of the race spent in the pits"""
    try:
        total_race = float(input("What was the total race time in seconds? "))
        total_pit_stops = int(input("How many pit stops were made? "))
        average_pit_duration = float(input("What was the average pit stop duration in seconds? "))
        
        total_pit_time = average_pit_duration * total_pit_stops
        pit_percentage = (total_pit_time / total_race) * 100
        return total_pit_time, pit_percentage
    except ValueError: #To prevent users inputting words or other inputs that are not valid
        print("Please enter a number!")
    
result = pit_stop_optimiser()

if result:
    total_pit_time, pit_percentage = result
    print(f"The total pit stop time is {total_pit_time}s")
    print(f"{pit_percentage:.2f}% of race time was spent in the pits")

    if pit_percentage > 5:
        print("You need a new pit crew. 🛠️")
    
