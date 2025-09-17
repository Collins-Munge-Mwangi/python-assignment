import random

# --- Activity 1: Inheritance & Encapsulation ---

class Character:
    """
    A base class for both superheroes and villains, demonstrating encapsulation.
    Hides internal health management and exposes only the necessary methods.
    """

    def __init__(self, name, power, catchphrase, role):
        """Initializes the character with basic attributes."""
        self.name = name
        self.power = power
        self.catchphrase = catchphrase
        self._health = 100  # Encapsulated attribute (internal use)
        self.role = role

    def get_health(self):
        """Returns the current health of the character."""
        return self._health

    def display_info(self):
        """Prints the character's information."""
        print(f"Role: {self.role}")
        print(f"Name: {self.name}")
        print(f"Power: {self.power}")
        print(f"Catchphrase: '{self.catchphrase}'")
        print(f"Health: {self.get_health()}\n")

    def use_power(self):
        """Simulates the character using their power."""
        print(f"{self.name} uses their {self.power}!")

    def take_damage(self, amount):
        """Reduces the character's health, handling minimum health."""
        self._health -= amount
        if self._health < 0:
            self._health = 0
        print(f"{self.name} takes {amount} damage. Health is now {self.get_health()}.")

class Superhero(Character):
    """A subclass for a superhero, inheriting from Character."""

    def __init__(self, name, power, catchphrase, team):
        super().__init__(name, power, catchphrase, role="Superhero")
        self.team = team

    def fly(self):
        """A unique method for a superhero."""
        print(f"{self.name} soars through the sky to save the day!")

class Villain(Character):
    """A subclass for a villain, inheriting from Character."""

    def __init__(self, name, power, catchphrase, evil_plan):
        super().__init__(name, power, catchphrase, role="Villain")
        self.evil_plan = evil_plan

    def reveal_plan(self):
        """A unique method for a villain."""
        print(f"Mwahahaha! My evil plan is to {self.evil_plan}!")


# --- Activity 2: Polymorphism Challenge ---

def battle(fighter1: Character, fighter2: Character):
    """
    Polymorphic function that makes any two Character objects battle.
    The specific 'move' method is determined at runtime based on the object's type.
    """
    print("--- Battle Commences! ---")
    
    # Each character "moves" differently
    fighter1.use_power()
    fighter2.use_power()
    
    # Simulate a round of combat
    damage1 = random.randint(10, 30)
    damage2 = random.randint(10, 30)
    
    fighter1.take_damage(damage2)
    fighter2.take_damage(damage1)
    
    print("-" * 20)
    
    # Check health and declare a winner (or continue)
    if fighter1.get_health() <= 0:
        print(f"The winner is {fighter2.name}!")
    elif fighter2.get_health() <= 0:
        print(f"The winner is {fighter1.name}!")
    else:
        print("The battle rages on!")

# --- Main Program Execution ---

# Create instances of the classes
hero = Superhero("Captain Courage", "Super Strength", "For justice!", "The Avengers")
villain = Villain("Dr. Malice", "Mind Control", "Your will is mine!", "conquer the city with robots")

# Display initial information
print("--- Character Profiles ---")
hero.display_info()
villain.display_info()

# Demonstrate a specific hero method
hero.fly()

# Demonstrate a specific villain method
villain.reveal_plan()

# Start the battle, demonstrating polymorphism
# The same function 'battle' can handle different types of Character objects.
battle(hero, villain)
battle(villain, hero) # The order doesn't matter due to polymorphism

# We can also create a list of different characters and have a battle loop
characters = [
    hero,
    villain,
    Superhero("Wonder Woman", "Lasso of Truth", "Truth prevails!", "Justice League")
]

print("\n--- Epic Battle Royale ---")
for i in range(len(characters) - 1):
    for j in range(i + 1, len(characters)):
        battle(characters[i], characters[j])