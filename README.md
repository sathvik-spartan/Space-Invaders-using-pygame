# Space Invaders using Pygame

A simple yet classic **Space Invaders** game built using **Pygame**, the popular Python library for game development. In this project, you play as a spaceship and shoot down enemy invaders before they reach you. The game showcases basic Pygame mechanics like sprite movement, collision detection, sound effects, and scoring.

---

## Features

- Player spaceship that moves left and right when initiated.
- Shooting bullets to destroy enemies - Primary Game Mechanic.
- Multiple enemy invaders with randomized positions
- Collision detection between bullets and enemies
- Dynamic Scoring system
- Background music and sound effects
- Game over condition when enemies reach the player

---

## Primary Technologies Used

- **Python 3.11**
- **Pygame**

---

## Project Structure

```bash
space-invaders/
│
├── main.py              # Main game loop and logic
├── background.png       # Background image
├── player.png           # Player spaceship sprite
├── enemy.png            # Enemy sprite
├── bullet.png           # Bullet sprite
├── background.wav       # Background music
├── laser.wav            # Shooting sound
├── explosion.wav        # Collision sound
└── README.md            # Project documentation
```

## Installation & Setup
1. Clone the repository

```bash
git clone https://github.com/sathvik-spartan/Space-Invaders-using-pygame.git
cd Space-Invaders-using-pygame
```
2. Install Dependencies

Make sure Python is installed on your system. Then install Pygame:
```bash
pip install pygame
```
3. Run the game

```bash
python main.py
```

## Controls
- Left Arrow / Right Arrow → Move player
- Spacebar → Shoot bullet

## To-Do / Future Enhancements
- Add levels and increasing difficulty
- Power-ups or different types of enemies
- High score tracking system
- Game menu and pause screen

## Future Enhancements 

1. Object-Oriented version to enhance the code.
2. Add more levels and powerups
3. Add levels (increase speed after every 10 points).
4. Add multiple bullets or cooldown timer.
5. Add pause/resume feature.
6. Add high score save using a text file or JSON.
7. Show game over or restart option.
8. Game Over condition added
9. Restart or menu screen
10. Code to support high scores or levels

## Acknowledgements

> Inspired by the classic Space Invaders arcade game (Mostly Atari) and built as a part of learning game development using Pygame.

