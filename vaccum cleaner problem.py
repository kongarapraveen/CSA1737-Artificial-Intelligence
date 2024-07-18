class VacuumCleaner:
    def __init__(self, environment):
        self.environment = environment
        self.position = (0, 0)  # Starting position of the vacuum cleaner
    
    def print_environment(self):
        for row in self.environment:
            print(row)
    
    def clean(self):
        while True:
            # Clean current position
            x, y = self.position
            self.environment[x][y] = 'Clean'
            
            # Check for other dirty positions
            dirty_positions = []
            for i in range(len(self.environment)):
                for j in range(len(self.environment[0])):
                    if self.environment[i][j] == 'Dirty':
                        dirty_positions.append((i, j))
            
            if not dirty_positions:
                print("Environment is clean.")
                break
            
            # Move to the closest dirty position
            closest_position = self.find_closest_dirty_position(dirty_positions)
            self.move_to_position(closest_position)
    
    def find_closest_dirty_position(self, dirty_positions):
        current_x, current_y = self.position
        min_distance = float('inf')
        closest_position = None
        
        for position in dirty_positions:
            x, y = position
            distance = abs(x - current_x) + abs(y - current_y)
            if distance < min_distance:
                min_distance = distance
                closest_position = position
        
        return closest_position
    
    def move_to_position(self, position):
        current_x, current_y = self.position
        target_x, target_y = position
        
        if target_x > current_x:
            print("Moving down.")
            self.position = (current_x + 1, current_y)
        elif target_x < current_x:
            print("Moving up.")
            self.position = (current_x - 1, current_y)
        elif target_y > current_y:
            print("Moving right.")
            self.position = (current_x, current_y + 1)
        elif target_y < current_y:
            print("Moving left.")
            self.position = (current_x, current_y - 1)
        
        print(f"Current position: {self.position}")

# Example usage:
if __name__ == "__main__":
    # Example environment with 3x3 grid
    environment = [
        ['Dirty', 'Clean', 'Dirty'],
        ['Clean', 'Dirty', 'Clean'],
        ['Dirty', 'Clean', 'Dirty']
    ]
    
    cleaner = VacuumCleaner(environment)
    print("Initial environment:")
    cleaner.print_environment()
    
    print("\nStarting to clean:")
    cleaner.clean()
