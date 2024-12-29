import os
import subprocess
import sys

def install_packages():
    """Install the required Python packages."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "telebot", "requests"])
        print("Required Python packages installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing packages: {e}")
        sys.exit(1)

def compile_cpp():
    """Compile the C++ file."""
    cpp_file = "soulcracks.cpp"
    output_file = "jai"
    compile_command = f"g++ -std=c++14 {cpp_file} -o {output_file} -pthread"

    if not os.path.exists(cpp_file):
        print(f"Error: {cpp_file} not found.")
        sys.exit(1)

    try:
        subprocess.check_call(compile_command, shell=True)
        print(f"Compiled {cpp_file} successfully into {output_file}.")
    except subprocess.CalledProcessError as e:
        print(f"Error compiling {cpp_file}: {e}")
        sys.exit(1)

def run_python_script():
    """Run the Python script."""
    python_script = "m.py"

    if not os.path.exists(python_script):
        print(f"Error: {python_script} not found.")
        sys.exit(1)

    try:
        subprocess.check_call([sys.executable, python_script])
        print(f"Ran {python_script} successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running {python_script}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("Starting setup...")
    install_packages()
    compile_cpp()
    run_python_script()
    print("Setup completed successfully.")