def kinetic_energy():
    print("\n--- Kinetic Energy (KE = 1/2 * m * v^2) ---")
    m = float(input("Enter mass (kg): "))
    v = float(input("Enter velocity (m/s): "))
    ke = 0.5 * m * (v ** 2)
    print(f"Kinetic Energy = {ke} Joules\n")

def ohms_law():
    print("\n--- Ohm's Law (V = I * R) ---")
    I = float(input("Enter current (A): "))
    R = float(input("Enter resistance (Ω): "))
    V = I * R
    print(f"Voltage = {V} Volts\n")

def gravitational_potential_energy():
    print("\n--- Gravitational Potential Energy (PE = m * g * h) ---")
    m = float(input("Enter mass (kg): "))
    h = float(input("Enter height (m): "))
    g = 9.81  # m/s²
    pe = m * g * h
    print(f"Potential Energy = {pe} Joules\n")

def force():
    print("\n--- Newton's Second Law (F = m * a) ---")
    m = float(input("Enter mass (kg): "))
    a = float(input("Enter acceleration (m/s²): "))
    F = m * a
    print(f"Force = {F} Newtons\n")

def wave_speed():
    print("\n--- Wave Speed (v = f * λ) ---")
    f = float(input("Enter frequency (Hz): "))
    wavelength = float(input("Enter wavelength (m): "))
    v = f * wavelength
    print(f"Wave Speed = {v} m/s\n")


def main():
    while True:
        print("=== Physics Formula Calculator ===")
        print("1. Kinetic Energy: KE = 1/2 m v²")
        print("2. Ohm’s Law: V = I R")
        print("3. Gravitational Potential Energy: PE = m g h")
        print("4. Force: F = m a")
        print("5. Wave Speed: v = f λ")
        print("6. Exit")

        choice = input("Choose a formula (1–6): ")

        if choice == "1":
            kinetic_energy()
        elif choice == "2":
            ohms_law()
        elif choice == "3":
            gravitational_potential_energy()
        elif choice == "4":
            force()
        elif choice == "5":
            wave_speed()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()