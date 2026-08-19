# Smart Manufacturing using Predicate Logic

machines = {
    "M1": "Active",
    "M2": "Active",
    "M3": "Maintenance",
    "M4": "Active"
}

# Check machine status
for machine, status in machines.items():

    if status == "Active":
        print(machine, "-> Producing")

    elif status == "Maintenance":
        print(machine, "-> Not Producing")


# Product production information
products = {
    "M1": "Gear",
    "M2": "Wheel",
    "M3": "Gear",
    "M4": "Motor"
}

print("\nAvailable Products:")

for machine, product in products.items():

    if machines[machine] == "Active":
        print(product, "is Available")


# Check Gear production
if machines["M3"] == "Maintenance":
    print("\nGear production by M3 is affected by maintenance.")
