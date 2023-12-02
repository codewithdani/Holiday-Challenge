import time
from random import choice

class FestiveWishGenerator:
    def __init__(self):
        # Emotions, tech adjectives, and recipients lists
        self.emotions = ['happy', 'magical', 'blessed', 'cheerful', 'wonderful']
        self.tech_adjectives = ['creative', 'easy', 'automatic', 'organized', 'perfect']
        self.recipients = ['coders', 'developers', 'tech enthusiasts', 'friends']
        # Celebration options
        self.celebrations = {
            1: 'Christmas',
            2: 'Hanukkah',
            3: 'Kwanzaa',
            4: 'Diwali',
            5: 'New Year',
        }

    def generate_wish(self, cohort_name, celebration):
        # Randomly choose elements from the lists
        emotion = choice(self.emotions)
        tech_adjective = choice(self.tech_adjectives)
        recipient = choice(self.recipients)

        # Generate the festive wish
        wish = (
            f"Wishing everyone in Cohort {cohort_name} and ALX community a {emotion} {celebration} filled with {tech_adjective} wonders! "
            f"May your code work well, your projects be easy, and your celebrations be as happy as a bug-free program. "
            f"Cheers to all {recipient} in ALX Cohort {cohort_name}!"
        )

        return wish

if __name__ == "__main__":
    # Get user input for cohort with error handling
    while True:
        try:
            cohort_name = int(input("Enter your ALX Cohort number: "))
            if cohort_name < 1:
                raise ValueError("Invalid Cohort number. Please enter a number greater than or equal to 1.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    # Display celebration options
    print("Choose a celebration:")
    for number, celebration in FestiveWishGenerator().celebrations.items():
        print(f"{number}. {celebration}")

    # Get user input for celebration by number with error handling
    while True:
        try:
            celebration_number = int(input("Enter the number of the celebration you want to wish for: "))
            if celebration_number < 1 or celebration_number > 5:
                raise ValueError("Invalid celebration number. Please enter a number between 1 and 5.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    selected_celebration = FestiveWishGenerator().celebrations.get(celebration_number, 'Unknown Celebration')

    # Create an instance of the FestiveWishGenerator
    wish_generator = FestiveWishGenerator()

    # Generate and print a festive wish
    festive_wish = wish_generator.generate_wish(cohort_name, selected_celebration)
    print(festive_wish)
    time.sleep(2)  # Adding a pause for a nice touch
