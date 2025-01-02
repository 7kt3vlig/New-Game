This is my first game using the Pygame module in Python
HOW TO RUN IN VSCODE
Install Python:

First, make sure Python is installed on your system. You can download it from python.org.
During installation, ensure that you check the box to "Add Python to PATH" before proceeding.
You can verify Python is installed by running the command python --version or python3 --version in your terminal/command prompt.
Download and Install VSCODE:

Download Visual Studio Code from VSCode Official Website and select your OS.
Install dependencies:

Open the terminal in VSCode (View > Terminal), and run the following command to install the required dependencies for your game:

bash
Copy code
pip install -r requirements.txt
Alternatively, you can open a terminal/command prompt (Powershell for Windows, Bash for macOS/Linux) and navigate to your game project directory using cd path/to/project, then run the same command:

bash
Copy code
pip install -r requirements.txt
Install Pygame:

If pygame is not listed in the requirements.txt file, you can install it separately using:

bash
Copy code
pip install pygame
Or if you're on a system where pip points to Python 2.x, you might need to use:

bash
Copy code
pip3 install pygame
Install "Code Runner" extension in VSCode:

In VSCode, search for and install the "Code Runner" extension in the Extensions marketplace (on the left side of VSCode).
This will make it easier to run your game directly from VSCode by simply pressing the "Run" button.
