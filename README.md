# Animal Movement Simulation

This Python program demonstrates object-oriented programming concepts, particularly inheritance and polymorphism, through a simulation of different animal movements.

## Features

- **Base Animal Class**: Provides a foundation with a `move()` method that must be implemented by subclasses
- **Multiple Animal Subclasses**: 
  - Bird (flies)
  - Fish (swims)
  - Snake (slithers)
  - Dog (runs)
  - Kangaroo (hops)
- **Extended Behaviors**:
  - Cheetah (sprints and hunts)
  - Rabbit (darts and evades)
- **Polymorphism Demonstration**: All animals respond to the `move()` method in their own way

## Code Structure

```python
class Animal:
    # Base class with abstract move() method
    
class Bird(Animal):
    # Implements flying movement
    
class Fish(Animal):
    # Implements swimming movement
    
# ... other animal classes ...

class Cheetah(Dog):
    # Extends Dog with hunting behavior
    
class Rabbit(Kangaroo):
    # Extends Kangaroo with evasion behavior
```

## Usage

1. The program creates a list of different animal objects
2. It demonstrates polymorphism by calling `move()` on each animal
3. Shows predator-prey interactions between Cheetah and Rabbit

## Example Output

```
--- Animal Movement Demonstration ---
Pigeon is flying! 🕊️
Goldie is swimming! 🐟
Viper is slithering! 🐍
Rex is running! 🐕
Joey is hopping! 🦘

--- Extended Animal Behavior ---
Chester chases Bugs!
Chester is sprinting at 70 mph! 🐆
Bugs is darting quickly! 🐇
---
Bugs tries to escape from Chester!
Bugs is darting quickly! 🐇
Chester is sprinting at 70 mph! 🐆
```

## Requirements

- Python 3.x

## How to Run

Simply execute the Python script:

```bash
python animal_movement.py
```

## Educational Value

This code demonstrates:
- Inheritance in OOP
- Method overriding
- Polymorphism
- Class hierarchies
- Abstract methods (via NotImplementedError)
