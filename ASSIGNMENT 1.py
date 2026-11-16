print("This program is designed to solve the specific problems listed below")
print("To select Velocity type S")
print("To select Force type N")
print("To select Stress type P")
print("To select Density type W")
print("To select Strain type E")

choice = input("Choose an option S, N, P, W, E: ").upper()  

if choice == "S":
        
        # Formula for velocity
        displacement = float(input("Input the distance in meters: "))
        time = float(input("Input the time in seconds: "))
        velocity = displacement / time
        print(f"The velocity of the object is {velocity} m/s")

elif choice == "N":

        # Formula for force
        mass = float(input("Input the mass in kilograms: "))
        acceleration = float(input("Input the acceleration in m/s^2: "))
        force = mass * acceleration
        print(f"The force is {force} N")

elif choice == "P":

        # Formula for Stress
        force = float(input("Input force in Newtons (N): "))
        area = float(input("Input area in square meters (m^2): "))
        stress = force / area
        print(f"The stress on the object is {stress} Pa")

elif choice == "W":

        # Formula for Density
        mass = float(input("Input mass in kilograms: "))
        volume = float(input("Input volume in cubic meters (m^3): "))
        density = mass / volume
        print(f"The density on the object is {density} kg/m^3")

elif choice == "E":

        # Formula for Strain
        extension = float(input("Input extension in meters: "))
        original_length = float(input("Input original length in meters: "))
        strain = extension / original_length
        print(f"The strain on the object is {strain}")

else:
        print("Invalid choice. Please select a valid option.")

