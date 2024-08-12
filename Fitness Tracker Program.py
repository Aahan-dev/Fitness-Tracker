class FitnessTracker:
    def __init__(self):
        """Initialize the fitness tracker with empty logs and goals."""
        self.workouts = []  # List to store workout logs
        self.goals = {}     # Dictionary to store fitness goals

    def log_workout(self, date, workout_type, duration, calories): # Allows you to log a workout.
        """
        Log a workout.
        
        Parameters:
        date (str): The date of the workout.
        workout_type (str): The type of workout (e.g., 'Running', 'Cycling').
        duration (float): Duration of the workout in minutes.
        calories (float): Calories burned during the workout.
        """
        workout = { # Creates a dictionary for the workout.
            'date': date,
            'workout_type': workout_type,
            'duration': duration,
            'calories': calories
        }
        self.workouts.append(workout) # Adds the workout to the list of workouts.
        print(f"Logged workout: {workout}") 

    def set_goal(self, goal_type, target_value): # Allows you to set a fiteness goal.
        """
        Set a fitness goal.
        
        Parameters:
        goal_type (str): The type of goal (e.g., 'Weekly Distance', 'Weight Loss').
        target_value (float): The target value for the goal.
        """
        self.goals[goal_type] = target_value 
        print(f"Set goal: {goal_type} to {target_value}") # Allows you to set a fitness goal.

    def track_progress(self): # Allows you to track your progress.
        """Display the logged workouts and current goals."""
        print("\n--- Workout Log ---")
        for workout in self.workouts:
            print(f"Date: {workout['date']}, Type: {workout['workout_type']}, "
                  f"Duration: {workout['duration']} min, Calories: {workout['calories']} cal")


        print("\n--- Fitness Goals ---") # Allows you to track your progress.
        for goal_type, target_value in self.goals.items():
            print(f"{goal_type}: {target_value}")


    def total_calories_burned(self): # Allows you to view how many calories you have burned.
        """Calculate the total calories burned from logged workouts."""
        total_calories = sum(workout['calories'] for workout in self.workouts)
        return total_calories


# Main program
if __name__ == "__main__":
    tracker = FitnessTracker()


    # Example usage
    tracker.log_workout('2024-08-01', 'Running', 30, 300)
    tracker.log_workout('2024-08-02', 'Cycling', 45, 450)
   
    tracker.set_goal('Weekly Distance', 15)  # Set a goal for distance
    tracker.set_goal('Weight Loss', 5)        # Set a goal for weight loss


    # Track progress
    tracker.track_progress()


    # Display total calories burned
    total_calories = tracker.total_calories_burned()
    print(f"\nTotal Calories Burned: {total_calories} cal")
