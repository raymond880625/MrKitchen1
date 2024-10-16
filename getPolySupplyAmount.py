import math

def getPolySupplyAmount(outer_diameter_addition):
    # Fixed values
    D_inner = 426  # Inner diameter in mm
    thickness = 0.4  # Thickness of paper in mm
    
    # Calculate outer diameter (inner diameter + user input)
    D_outer = D_inner + outer_diameter_addition
    
    # Calculate the length using the given formula
    length = (math.pi * (D_outer**2 - D_inner**2)) / (4 * thickness)  # Length in mm
    length_meters = length / 1000  # Convert to meters
    
    return length_meters

# Get user input for the additional outer diameter value
outer_diameter_input = float(input("Enter the additional diameter (e.g., for 14, type 14): "))
length_result = getPolySupplyAmount(outer_diameter_input)
print(f"The length of the Polyvision roll is approximately: {length_result:.2f} meters")

