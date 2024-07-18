from itertools import permutations

def solve_cryptarithmetic(puzzle):
    # Remove spaces and convert puzzle to lowercase
    puzzle = puzzle.replace(" ", "").lower()

    # Split puzzle into left-hand side (lhs) and right-hand side (rhs)
    lhs, rhs = puzzle.split('=')
    lhs_terms = lhs.split('+')

    # Extract unique letters
    unique_letters = set(lhs + rhs)

    # Generate permutations of digits from 0 to 9 for unique letters
    for perm in permutations(range(10), len(unique_letters)):
        if any(perm[0] == 0 for perm in lhs_terms + [rhs]):  # Skip permutations with leading zeros
            continue
        
        # Create a mapping of letters to digits
        mapping = {letter: digit for letter, digit in zip(unique_letters, perm)}

        # Evaluate the left-hand side and right-hand side with current mapping
        lhs_value = sum(int(''.join(str(mapping[letter]) for letter in term)) for term in lhs_terms)
        rhs_value = int(''.join(str(mapping[letter]) for letter in rhs))

        # Check if the equation is satisfied
        if lhs_value == rhs_value:
            print("Solution found:")
            print(mapping)
            return mapping

    print("No solution found.")
    return None

# Example usage:
if __name__ == "__main__":
    puzzle = "SEND + MORE = MONEY"
    solve_cryptarithmetic(puzzle)
