# Snake Game 🐍

Welcome to **Snake**, a classic arcade game where you guide a growing snake to eat fruits and avoid obstacles. This project is an implementation of the iconic game in Python, developed with object-oriented programming principles.

## 📜 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Images](#images)
- [File Structure](#file-structure)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [About This Project](#about)
- [License](#license)
- [Security](#security)
- [Code of Conduct](#code-of-conduct)


## 🕹️ Features <a name="features"></a>

- Classic Snake gameplay with growing tail
- Multiple levels with increasing difficulty and obstacles
- Random fruit generation
- Game-over conditions for colliding with obstacles, walls, or the snake's own tail
- Graphical interface with intuitive keyboard controls

## 🚀 Installation <a name="installation"></a>

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/SebaB29/Snake.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Snake
   ```

3. Run the game:
   ```bash
   python main.py
   ```

## 🎮 Usage <a name="usage"></a>

Use the following controls to play the game:

- **Left Arrow**: Move left
- **Right Arrow**: Move right
- **Up Arrow**: Move up
- **Down Arrow**: Move down
- **P**: Pause

Avoid obstacles and eat fruits to grow longer!

## 📷 Images <a name="images"></a>

<div style="display: flex;">
    <img alt="Img Snake" src="img/snake.png" width="400px" height="400px">
    <img alt="Img Game Over" src="img/gameover.png" width="400px" height="400px">
</div>

## 📁 File Structure <a name="file-structure"></a>

The project structure is as follows:

```
Snake/
├── .github/
│   ├── CODE_OF_CONDUCT.md
│   ├── CONTRIBUTING.md
│   ├── SECURITY.md
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── PULL_REQUEST_TEMPLATE.md
├── graphics/
│   ├── game_render.py
│   └── gamelib.py
├── img/
│   └── [2 demo images of the game]
├── resources/
│   └── obstacles.txt
├── src/
│   ├── constant.py
│   ├── event_controller.py
│   ├── fruit.py
│   ├── game.py
│   ├── obstacle_loader.py
│   ├── obstacle.py
│   ├── program.py
│   └── snake.py
├── .gitignore
├── LICENSE
├── main.py
└── README.md
```

- **graphics/**: Contains libraries for rendering the game (gamelib and custom graphics).
- **img/**: Includes demo images showcasing the game's functionality.
- **resources/**: Contains the obstacles configuration file (`obstacles.txt`).
- **src/**: Includes source code files for game logic (snake, fruit, obstacles, and game flow).
- **main.py**: The entry point of the application.

## 🛠️ Technologies <a name="technologies"></a>

This project is built with:

- Python
- [Gamelib](https://github.com/dessaya/python-gamelib) (A library created by the instructor to facilitate the use of threads and rendering for the interface)

## 🤝 Contributing <a name="contributing"></a>

Contributions are welcome! If you'd like to improve the game, feel free to fork the repository and submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## 📚 About This Project <a name="about"></a>

This project was developed as a practical assignment for university. It aims to implement the classic Snake game using Python, focusing on game logic and graphical interface through object-oriented programming principles.

## 📄 License <a name="license"></a>

Distributed under the MIT License. See `LICENSE` for more information.

## 🔐 Security <a name="security"></a>

If you discover a vulnerability, please review our [Security Policy](.github/SECURITY.md) for guidance on reporting.

## 📜 Code of Conduct <a name="code-of-conduct"></a>

Please read our [Code of Conduct](.github/CODE_OF_CONDUCT.md) to understand expected behavior.
