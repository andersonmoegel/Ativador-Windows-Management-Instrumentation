# WMI Diagnostic and Repair Script for Windows

## Description  
This script was developed to check, activate, and repair the WMI (Windows Management Instrumentation) service on Windows systems. It also includes a logging system to monitor the operations performed.

---

## Features

1. **Administrator Privilege Check**  
   The script checks whether it is being run with administrative privileges, which are required to manipulate system services and modify files in protected directories.

2. **Diagnostic Logs**  
   Creates and writes detailed logs to the file `C:\Windows\Temp\wmi_status.txt` to record the status of WMI and any corrective actions taken.

3. **WMI Diagnostic**  
   Uses the `win32com.client` library to attempt a connection with the WMI service and check its status.

4. **WMI Activation**  
   If the WMI service is stopped, the script attempts to start it using the `sc start winmgmt` command.

5. **WMI Repair**  
   If the WMI check fails, the script attempts to repair the WMI repository using the commands `winmgmt /verifyrepository` and `winmgmt /salvagerepository`.

---

## Requirements
- Python must be installed on the system.
- The `pywin32` module is required to interact with WMI.  
  You can install it with:
  ```bash
  pip install pywin32
  ```

---

## Usage
1. Make sure to run the script with administrator privileges.  
   - If not started as administrator, the script will attempt to relaunch itself with elevated privileges.
2. The result of the operations will be saved in the log file `C:\Windows\Temp\wmi_status.txt`.
3. The script prints status messages to the console for easy monitoring during execution.

---

## Notes and Considerations
- **Compatibility:** This script is designed for Windows systems.  
- **Potential Risks:** Manipulating WMI may affect critical system services. Use with caution and only if necessary.
- **Old Log Deletion:** The previous log file is deleted before creating a new one to keep the report up to date and prevent excessive file growth.

---

## Limitations
- If the script fails to obtain administrator permissions, it will not be able to perform WMI diagnostics or repairs.
- It relies on internal Windows commands (`sc`, `winmgmt`), which may vary between different Windows versions.

---

## Changelog
- Version 1.0: Initial functional version with WMI diagnostic, activation, and repair.

---

## Contributions
Suggestions for improvements and new features are welcome.
