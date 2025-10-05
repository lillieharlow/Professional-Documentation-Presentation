![TO-DO. art banner](docs/img/art_banner.png)

👋 TO DO. is a fun, secure, and easy-to-use task management app that runs directly in your terminal.
Unlike typical plain-text CLI tools, TO DO. brings your productivity to life with emoji, colour, and ASCII art banners — making task management engaging and stress-free.

In today’s world of productivity apps, many solutions are either overly complex (e.g., Notion, Trello) or too minimal (simple text files or todo.txt). TO DO. addresses this gap by providing:

- ✅ A lightweight and accessible tool you can use directly in the terminal.

- ✅ A secure environment with hashed passwords and JSON-based storage.

- ✅ An engaging user experience, so managing your tasks doesn’t feel like a chore.
<hr>

Command line tools are still one of the fastest ways to get work done, especially for developers. They use minimal resources and fit right into existing workflows [1]. At the same time, studies show that good design, like clear visuals and easy-to-use interfaces  keeps people coming back to an app [2].

TO DO. adds colour, ASCII banners, and emojis to make managing tasks in the terminal more fun and engaging.

## Features

- 🌈 Colourful CLI - Colour-coded output, emoji icons, and ASCII banners, TO DO. transforms simple task lists into a visually rich experience that keeps motivation high.

- 🔒 Secure login system - Many CLI tools store data in plain text. TO DO. protects users with bcrypt password hashing and local JSON storage, ensuring personal data stays private and secure.

- 👤 Guest mode - No accounts, dashboards, or installations beyond your terminal. Jump straight in with Guest Mode to test the app, then create an account when you’re ready.

- 📝 Task management - You’ll be able to add, view, mark as complete, and delete tasks effortlessly, with a clean, intuitive interface that fits right into your workflow.

- 🔝 Prioritisation - Easily organise your tasks by High, Medium, or Low priority. You’ll stay on top of your goals with visual cues that highlight which task to tackle next.

- 💾 Lightweight & Persistent — Your tasks are saved locally, ready whenever you return. TO DO. runs directly in your terminal, it's fast, efficient, and distraction-free.

## Docs & Help Files

For more detailed information, click the ```docs``` folder:

- ⚙️ ```Dependencies.md``` – The libraries and packages TO DO. needs to operate, it's purpose and an outline of the legal and ethical impacts.

- 💻 ```Installation.md``` – Step-by-step guide to get TO DO. running on your system.

- 📋 ```Requirements.md``` – Hardware and system requirments.

- 📝 ```Usage.md``` – Detailed instructions for using all features of TO DO.

These help files make it easy to set up, use, and troubleshoot the app — everything you need in one place!

## Target Market & User Stories
Perfect for students, developers, and anyone who loves organising their day without leaving the terminal.

- 🎓 Students who need a simple but reliable task manager.<br>
*“As a student, I want to organise assignments by priority so I don’t miss deadlines.”*

- 👨‍💻 Developers who work in the terminal and want a non-boring alternative to plain task apps.<br>
*“As a developer, I want to manage tasks without leaving my terminal workflow.”*

- ⚡ Productivity enthusiasts looking for a lightweight tool without syncing to external services.<br>
*"As a user who is productively organised, I want a lightweight tool that keeps me organised without syncing to external services."*

- 👀 Casual users who want to “try before they commit” with guest mode. <br>
*“As a new user, I want to try an app in guest mode before creating an account.”*

## Quick Install

For the best experience, use a dark theme in your code editor (e.g., "Visual Studio Dark" in VS Code).

1. **Clone Repository**
   ```bash
   git clone https://github.com/lillieharlow/Professional-Documentation-Presentation.git
   cd TO_DO._App
   ```
2. **Install Dependencies**
   ```bash
   pip install rich pyfiglet bcrypt emoji
   ```
   Or create `requirements.txt` and manually add the dependencies (recommended for consistency):
   ```
   bcrypt==4.3.0
   emoji==2.14.1
   markdown-it-py==3.0.0
   mdurl==0.1.2
   pyfiglet==1.0.2
   Pygments==2.19.2
   rich==13.7.1
   six==1.17.0
   ```

## Security & Data Storage

TO DO. takes your privacy and data seriously. Whether you’re managing assignments, work tasks, or personal projects, you can trust that your information is safe:

- 💻 Secure login system – Passwords are hashed using bcrypt, ensuring they’re never stored in plain text.

- 💾 Local storage – All task data is stored in JSON files on your machine, giving you full control without relying on external servers.

- 🕵️‍♂️ Guest mode – Try the app without creating an account. Tasks created in guest mode aren’t saved, protecting your privacy.

- 💾 Data persistence – Tasks you create are saved locally, so you can return to your to-do list exactly as you left it.

- 🚫 No external tracking or cloud syncing – Your data stays on your machine unless you choose to back it up yourself.

## Similar Projects & Inspiration

- 💡 [Todo.txt CLI](http://todotxt.org/) – A minimalist task manager in plain text.

- 💡 [Taskwarrior](https://taskwarrior.org/) – A powerful CLI task manager, but with a steep learning curve.

TO DO. draws inspiration from these projects but TO DO. isn’t just another CLI tool. It’s a secure, joyful, productivity companion that fits naturally into your workflow, keeps your data safe, and turns to-do lists into something you'll actually enjoy using.

## References
[1] Arjun K. (2024) *Why Command-Line Tools Are Still Relevant in the Age of GUIs*, https://dev.to/arjun98k/why-command-line-tools-are-still-relevant-in-the-age-of-guis-3n7m?utm_, accessed 3 October 2025.

[2] Stutcliffe, A. G. (2023) *Why people choose apps: Aesthetics, usability, and engaging interaction*, https://www.sciencedirect.com/science/article/pii/S1071581922001835?utm_, accessed 3 October 2025.