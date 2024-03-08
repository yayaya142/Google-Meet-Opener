import webbrowser
import subprocess


# this class control the web api 
class WebApi:
    # URL = 'meet.new'
    # PREFIX = "meet"
    # base_url = "https://meet.google.com/"
    URL = 'https://www.example.com/'
    PREFIX = "Example"
    base_url = "https://testing.example.com/"
    

    # this api is used to open the web browser and create a new meeting
    def open_web_api():
        webbrowser.open(WebApi.URL)
       
    # this api is used to get the url of the open window
    def get_open_web_url_api():
        URL = get_open_url_with_power_shell()
        if (URL is None):
            return None
        URL = WebApi.extract_meeting_id(URL)
        if (URL is None):
            return None
        URL = WebApi.create_meeting_invite(URL)
        if (URL is None):
            return None
        
        return URL

    # Define the extract_meeting_id function
    def extract_meeting_id(title):
        if title.startswith(WebApi.PREFIX) == False:
            return None
        
        parts = title.split(' - ')  
        if len(parts) > 1:
            return parts[1] 
        else:
            return None  
    
    
    # this function is used to create a meeting invite
    def create_meeting_invite(key):
        if key is None:
            return None
        return WebApi.base_url + key
    


    
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
        
   
    return output_lines[3]


