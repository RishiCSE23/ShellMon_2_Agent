# runs the collection agent 

set -e   # breaks the script when exception occurs 

deactivate # deactivate any active runtime 
source venv/bin.activate  # activate the venv
echo "Running Agent..."
python3 sender.py # run the agent 