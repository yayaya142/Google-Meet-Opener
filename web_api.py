import webbrowser
import subprocess

# this api is used to open the web browser and create a new meeting
def open_web_api():
    URL = 'https://www.meet.new/'  
    webbrowser.open(URL)
    
    
    
    
# this api is used to get the url of the open window
def get_open_web_url_api():
    URL = get_open_url_with_power_shell()
    return URL




# this function use the powershell to get the url of the open window
def get_open_url_with_power_shell():
        # set the powershell command
    powershell_command = r"powershell.exe -Command Get-Process | Where-Object {$_.MainWindowTitle -like '*Google Chrome*'} | Select-Object MainWindowTitle"
    # Run the PowerShell command
    result = subprocess.run(powershell_command, capture_output=True, text=True)

    # Check if the command was successful
    if result.returncode == 0:
    # Extract the output
        output_lines = result.stdout.splitlines()
    else:
        return None
    
    URL = extract_meeting_id(output_lines[3])
    URL = create_meeting_invite(URL)    
    
    return URL


# this function is used to extract the meeting id from the title of the window
def extract_meeting_id(title):
    parts = title.split(' - ')  # split the string by ' - '
    if len(parts) > 1:
        return parts[1]  # return the second part
    else:
        return None  # return None if there's no ' - ' in the strings
    
    
    
# this function is used to create a meeting invite
def create_meeting_invite(key):
    base_url = "https://meet.google.com/"
    if key is None:
        return None
    return base_url + key