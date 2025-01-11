# PyCVGenerator

**PyCVGenerator** is a simple curriculum vitae generator written in Python. It takes your personal data and generates a formatted `.docx` file for your CV.

# How to Install Dependencies

Create a virtual environment (optional but recommended):

On Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required dependencies: 
After activating the virtual environment, install the necessary dependencies with pip:
```bash
pip install -r requirements.txt
```

Verify the installation: Make sure all dependencies are correctly installed. Now you can run the program.

## How to Use

1. **Replace `content.xml`**  
   Replace the contents of `content.xml` with your CV data. This file serves as the data source for your CV.

2. **Change the photo**  
   Replace the placeholder photo with your own.

3. **Set paths in the configuration file**  
   Update the paths in the configuration file (`config` file) to match your setup.

4. **Run the program**  
   Execute the following command to generate your CV:
   ```bash
   py main.py

# Output

The program will generate a formatted .docx file containing the contents of your CV.

Feel free to contribute or open an issue if you encounter any problems!
