# Simple YouTube to blog generator
Generates a pretty terrible blog by transcribing the video from a link with AssemblyAI, and then uses OpenAI API to generate text.
Based on the [Learn Python Backend Development by Building 3 Projects \[Full Course\]](https://www.youtube.com/watch?v=ftKiHCDVwfA&t=10088s) tutorial by [CodeWithTomi](https://www.youtube.com/c/CodeWithTomi) (the first project).
Improved in several ways - basic checking of user inputs, minor added functionality and slight visual polish.

## Tech stack
Django for backend, simple HTML for frontend.

## Setup
1. Clone the repository:
    ```sh
    git clone https://github.com/lmProgramming/youtube-to-blog-ai-generator
    ```
2. Navigate to the project directory:
    ```sh
    cd youtube-to-blog-ai-generator
    ```
3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Navigate to backend directory:
   ```sh
    cd backend
    ```
5. Run local server:
   ```sh
    python manage.py runserver
    ```
