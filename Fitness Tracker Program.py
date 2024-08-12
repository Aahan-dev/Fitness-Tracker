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

    