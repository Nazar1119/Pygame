# Skeleton Hero Defense - PyGame Project

Welcome to **Skeleton Hero Defense**! This is an exciting 2D action defense game created using PyGame. In this game, you control a skeleton hero tasked with defending against waves of wolves and ghosts. Your weapons are bones and a powerful super-weapon: skulls!

## Table of Contents

- [Game Overview](#game-overview)
- [Gameplay Mechanics](#gameplay-mechanics)
- [How to Play](#how-to-play)
- [Game Win and Loss Conditions](#game-win-and-loss-conditions)
- [Contributing](#contributing)
- [Installation](#installation)

## Game Overview

In **Skeleton Hero Defense**, you control a skeleton warrior who must defend against oncoming wolves and ghosts, which are attacking from the right side of the screen. Armed with a limited supply of bones and powerful skulls, your goal is to stop the enemies from reaching your position.

You will win the game by defeating 50 enemies. However, you lose if any of the enemies touch you, or if 3 or more enemies manage to pass by without being stopped.

## Gameplay Mechanics

- **Main Hero (Skeleton)**: The player controls a skeleton who throws bones and uses skulls as weapons.
  
- **Weapons**:
  - **Bones**: Your main weapon. A bone kills only one enemy it touches. You start with 5 bones, and an additional bone is added to your supply every 3 seconds. Use them wisely!
  - **Skulls (Super-Weapon)**: Skulls are special items that kill all enemies on the current line when used. You can pick up skulls from fallen enemies and deploy them strategically.

- **Enemies**:
  - **Wolves**: Fast-moving enemies that charge towards you.
  - **Ghosts**: Slightly slower than wolves but trickier to deal with.


## How to Play
- **Movement**: Use the arrow keys to move your skeleton hero.
- **Throw a bone**: Press 'A' key to throw a bone at the enemies. The bone will travel in a straight line and destroy the first enemy it touches. You start with 5 bones, and every 3 seconds, you gain one more bone.
- **Use a skull**: Press 'D' key to drop and use a skull. The skull kills all enemies on the current line instantly.
- **Defeat enemies**: Defeat wolves and ghosts to collect skulls, which will help you in tough situations.

Plan your attacks, manage your bone supply, and use skulls strategically to stay alive!

## Game Win and Loss Conditions

- **Win**: You win the game when you defeat a total of 50 enemies using your bones and skulls.

- **Loss**: The game is over if:
  - **Any enemy touches your skeleton hero.**
  - **3 or more enemies manage to pass through the entire screen without being killed.**

## Contributing

Contributions are welcome! If you'd like to improve the game, add new features, or fix bugs, follow these steps:

1. **Fork the repository**: This will create a copy of the repository under your GitHub account.
   
2. **Create a new branch**: Create a branch for your feature or bugfix.


## Installation

To run the game on your local machine, you need to install Python and PyGame. Follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/skeleton-hero-defense.git
