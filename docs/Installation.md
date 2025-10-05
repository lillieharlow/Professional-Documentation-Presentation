## Setup & Installation
TO DO. will run on all major operating systems, including Windows, macOS and Linux.
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
   ```bash
   pip install -r requirements.txt
   ```
   > **Note:** Sub-dependencies like `Pygments`, `markdown-it-py`, `mdurl`, and `six` are installed automatically.
<hr>

3. **Run the App**
   Start the app from the terminal:

   ```bash
   python3 todo_manager/main.py
   ```
   Follow the on-screen prompts to sign up, log in, or try the app in guest mode.