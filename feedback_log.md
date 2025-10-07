## FEEDBACK LOG (RECEIVED) 1

Date: 4th October 2025

Checked by: Sam Maclean

Documentation checked: ```README.md``` ```docs```

Feedback:

*“I really like how the README immediately tells me what the app is, why it exists, and who it’s for. Code, documentation, and requirements are clearly laid out and easy to follow. One enhancement could be adding a “Documentation” link or table of contents directly in the README so users don’t have to hunt around for the docs folder. Also, since the app embraces a playful, colourful interface, giving the README a bit more personality with emojis, styled headings or use the ASCII banner as the title in the README could make it fit more with the app’s tone. Because the app handles user accounts and passwords, iI would like to see a brief statement about this in the README, a security statement. Something that outlines how passwords and my data would be securely stored and not shared. This would strengthen trust for any would-be user. Enhance the app to match professional standards around security and user privacy seen in the real-world. Overall, the foundation is strong and these tweaks would raise usability and trust even further.”*

Actions taken:

1. Added a direct link in ```README``` to ```docs``` folder to guide user to help files, improve usability and accessibility.
    
    *Australian Government Digital Service Standard (Criteria 9: Make it simple and intuitive).*
2. Added a Security and Privacy section to ```README```. Emphasise transparent, responsible handling of user data.
    
    *Australian Privacy Act 1988 (Cth) – APP 6 (use and disclosure of personal information).*
3. Enhanced visual appeal of ```README``` by adding emojis and ASCII banner title. Creating a more enjoyable, positive user experience through design.
    
    *Australian Computer Science Code of Professional Conduct (Value 1.3 — Enhancement of Quality of Life)*
<hr>

## FEEDBACK LOG (RECEIVED) 2

Date: 5th October 2025

Checked by: Joshua Duong

Documentation checked: ```README.md```

Feedback:

*“Your readme looks great! Gives me a clear picture on your features, who its intended for and a brief that explains the differences to your product and others. I would recommend: 1. expand a little further on the features that makes your product stand out against the competitors. This would be the key sales pitch that piques potential clients into buying into your product. 2. Add the more operational information in your readme. Users would need to understand how to setup their environments, how to install any dependencies to use your products, and how to launch said product”*

Actions taken:

1. Added a direct link in ```README``` to ```docs``` folder to guide user to help files, improve usability and accessibility.
    
    *Australian Government Digital Service Standard (Criteria 9: Make it simple and intuitive).*
2. ```README``` features elaborated on further to highlighting it's uniqueness for potential users.
    
    *Australian Computer Science Code of Professional Conduct (Value 1.3 — Enhancement of Quality of Life)*
<hr>

## FEEDBACK LOG (RECEIVED) 3

Date: 5th October 2025

Checked by: Matt Vete

Documentation checked: ```README.md```

Feedback:

*“Looks really clean! I really like the visual appeal with the terminal screenshot doubling as a title for the readme. One thing I would suggest to consider is putting a simplified install/setup section straight into the main README. you have linked your documents well, but having quick copy-paste steps on the front page makes it super accessible for users who just want to get started right away without having to delve into the full documentation”*

Actions taken:

1. Added a simplified installation section to ```README```. Users can quickly copy-paste to launch the app.
    
    *Australian Computer Science Code of Professional Conduct (Value 1.4 — Competence).*
    
    *Australian Government Digital Service Standard (Criteria 9: Make it simple and intuitive).*
<hr>

## FEEDBACK LOG (RECEIVED) 4

Date: 6th October 2025

Checked by: Stefan Pejnovic

Documentation Checked: ```README.md```, ```docs/*```

Feedback:
"The README is good and covers what I'd want to see at a glance. Some links to other docs in the docs folder would be a nice to have, and/or a table of contents in so I quickly see what I want.

Each of the docs in the docs folder are good in isolation, but there's a fair bit of repetition between them and the README. For example, the contents of the requirements.txt can be found in the README, Installation.md, Dependencies.md and of course the file itself. Low level documentation like this tends to go out of date quickly in a real world scenario, so it may be a good idea to just link the user straight to the requirements.txt file and let it be self-updating as the project progresses.

The in-code documentation is quite extensive and each function is clearly explained. For the future, some simple methods could either be slightly renamed, or have their arguments renamed resulting in them being self-documenting. This is handy because docstrings tend to be forgotten about during development and have a habit of going out of date.

Also a small note regarding variable names. Most are very clear throughout the project, but the emojis can be a bit confusing. When I saw a line like print_info(f"{interesting} You don't have any tasks listed, let's add some!") out of context, it wasn't clear what interesting was. Making those variable names more distinct would make understanding the code a bit easier.

Overall great work and a well documented project, it was clear what the project was, who it was for and why it delivers value. The code itself is also generally easy to understand and follow."

Actions Taken:

1. Added links in `README` to `docs` folder to improve navigation and accessibility.

2. Cleaned up repeated installation instructions in `README` and `docs/Installation.md`.

3. Renamed variables containing emojis to more descriptive names for clarity.

<hr>

## FEEDBACK LOG (PROVIDED) 1

Date: 5th October 2025

Checked by: Nick Fahey

Documentation checked: [GitHub Repo: flask-lms](https://github.com/macfluffy/flask-lms/tree/master)

Feedback:

"Hey guys,
Readme looks great! A couple of things I would suggest, and some general notes:

1. I think it would be good to position the setup section closer to the top, e.g. above background & rationale. Easy access to the setup guide means users can find the commands required quickly and set up faster.

2. Maybe consider separating some of the README information into separate docs? E.g. background / rationale, target users, and sections under security / data considerations. It's structured well currently, but the quick access section is the only one under a drop down, and it's probably the most important one for a user to read!

3. Your setup script for the database:
```psql -U postgres <<'SQL'
CREATE DATABASE lms_db;
CREATE USER lms_user WITH PASSWORD 'change-me';
GRANT ALL PRIVILEGES ON DATABASE lms_db TO lms_user;
SQL
```

grants privileges for the database but not schema 'public', so lms_user won't be able to perform operations. Consider adding privileges for the schema, or alternatively create the database after the user, and set the DB owner to lms_user.

4. There may be some ethical concerns regarding distribution of this app without authentication implemented. While it is made clear in the README that this feature isn't yet available - the docs also present this app as "...inspired by these platforms but intentionally scoped as a lightweight solution for educational institutions. It ". This could be interpreted as suggesting this app as a simple to use replacement for the alternatives mentioned, and a user might implement this as is without considering the importance of keeping PII safe. I would suggest adding a disclaimer in the README and docs to highlight that this app is not production ready, and should not be used to store sensitive user data until authentication is implemented.
Consider the IEEE code of ethics section I, 1. "... to protect the privacy of others ..."
The IEEE code can be viewed here: https://www.ieee.org/content/dam/ieee-org/ieee/web/org/about/corporate/ieee-code-of-ethics.pdf
<hr>

## FEEDBACK LOG (PROVIDED) 2

Date: 6th October 2025

Checked by: Lillie Chapman

Documentation checked: [GitHub Repo: flask-lms](https://github.com/macfluffy/flask-lms/tree/master)

Feedback:

"Hey Matt & Joshua! Great idea to use the project from class!

Feedback:
1. As someone who has only recently entered the tech world (I had no experience prior to this course), I actually didn’t know what LMS stood for and had to google it. I suggest typing “Learning Management System (LMS)” at the start of the README. Promoting good accessibility practices and ensures documentation is clear and inclusive. Ethical ref: WCAG 2.1 (Guidelines for making digital content understandable and perceivable for all users).

2. Great dot points under background and rationale. This research really does highlight the need for this API.

3. I couldn’t find the system hardware requirements or the list of dependencies? This could  lead to install issues and users not being able to run the project properly. Including a clear list in the README/help file would help ensure users can set it up safely and correctly.

4. The features list is well detailed but I don’t think it fits your target market as it’s written in developer language. I assume most teachers and administer staff wouldn’t really understand it. I suggest translating it into everyday user talk to align with target market. Making it more accessible and inclusive. E.g:
Instead of “RESTful CRUD endpoints for students, teachers, and courses with JSON responses” = Say: "Quickly add, update, and view students, teachers, and courses through a simple interface, keeping records consistent and enrolment faster."
Instead of "CLI helpers (flask db create|drop|seed) for rapid database lifecycle management" = Say: "Easily set up and update the system’s database with minimal effort, keeping information accurate and up-to-date."
Ethical ref: ISO/IEC 38500 (Corporate governance of IT – ensuring IT is aligned with users’ needs and ethical principles)."