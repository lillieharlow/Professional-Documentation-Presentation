## Dependencies

| Library           | Version  | Purpose                               | License      | License Info                         |
|-------------------|----------|---------------------------------------|--------------|--------------------------------------|
| bcrypt            | 4.3.0    | Password hashing (security)           | Apache 2.0   | [PyPI](https://pypi.org/project/bcrypt/) |
| emoji             | 2.14.1   | Emoji rendering in CLI                | BSD          | [PyPI](https://pypi.org/project/emoji/)  |
| rich              | 13.7.1   | CLI formatting, colors, tables        | MIT          | [PyPI](https://pypi.org/project/rich/)   |
| pyfiglet          | 1.0.2    | ASCII art banners                     | MIT          | [PyPI](https://pypi.org/project/pyfiglet/) |
| markdown-it-py    | 3.0.0    | Markdown parsing (rich dependency)    | MIT          | [PyPI](https://pypi.org/project/markdown-it-py/) |
| mdurl             | 0.1.2    | Markdown URL handling                 | MIT          | [PyPI](https://pypi.org/project/mdurl/)  |
| Pygments          | 2.19.2   | Syntax highlighting (rich dependency) | BSD          | [PyPI](https://pypi.org/project/Pygments/) |
| six               | 1.17.0   | Python 2/3 compatibility              | MIT          | [PyPI](https://pypi.org/project/six/)    |

All dependencies are open source and compatible with each other.
<hr>

**Purpose of Each Dependency**
   - **bcrypt:** Provides secure password hashing to protect user data.
   - **emoji:** Display emojis in the CLI for a fun user experience.
   - **rich:** Enhances CLI with style, colours, task table and formatting for better readability.
   - **pyfiglet:** Creates ASCII art banners to make the app pop! Visually engaging and fun.
   - **markdown-it-py, mdurl, Pygments:** Support rich text rendering and syntax highlighting used by `rich`.
   - **six:** Ensures compatibility between Python 2 and 3, used by `bcrypt`.

**Legal & Ethical Impacts**  
   - All files are created and managed by the app, no external dependencies or third-party code.
   - User data stays local and is stored securely in JSON format.
   - Only reputable open source libraries are used (MIT, Apache 2.0, BSD licenses).
   - No restrictive or copyleft licenses—safe for personal or project use and distribution.
   - No external data sharing or tracking.

- **Security Impact** 
   - User passwords are hashed (never stored as plain text).
   - All user data is stored locally and no personal data is shared externally.
   - The app has no internet connectivity requirements, further ensuring data privacy.

- **Conflicts**
   - These packages are known to be fully compatible with each other, with no conflicting versions or installation issues on the specified versions.
   - Use a virtual environment to avoid conflicts with other Python projects. Pinning versions in `requirements.txt` preserves compatibility, preventing future issues with updates.