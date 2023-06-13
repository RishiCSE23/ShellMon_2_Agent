# Setup the environment

1. Clone the repo
    ```
    git clone <REPO LINK>
    cd ShellMon_Agent     # enter the project directory
    ```
1. Update the repository 
    ```
    sudo apt -y update 
    ```
2. Install Python and additional dependencies 
    ```
    sudo apt -y install python3 python3-pip python3-venv 
    ```
3. create a venv
    ```
    python3 -m venv venv
    ```
4. activate the venv
    ```
    source venv/bin/activate  
    ``` 
5. upgrade pip to its latest version
    ```
    python3 -m pip install --upgrade pip
    ``` 
6. install dependencies
    ```
    pip install -r requirements.txt  
    ```
# Run the Agent 
1. Each ShellMon agent is identified uniquely by its system IP. Check the active IP interface whose IP will be used as the system ip. 
    ```
    ip a
    ```
2. Make sure the Virtual Environemnt is active
    ```
    source venv/bin/activate 
    ```
3. Run 
    ```
    python3 sender.py
    ```