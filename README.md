##  How to use this package:

### 1. Download all files from this repo to custom folder. (this app needs "psutil" to be installed).

### 2. From custom folder enter "pip install ." in terminal ("pip" should be installed beforehand).

### 3. Enter python in terminal ("python" should be installed beforehand).

###  **Important! If "custom folder" is not indicated in sys.path please type:**

   ### *   import sys
   ### *   sys.path.insert(0, 'path_to_custom_folder')

### 4. Enter "import snapshot".

### 5. Enter "snapshot.go()" to start this app which will collect metrics to the file which will be created in the same folder you run this app.

### 6. To terminate this app press "Ctrl + c".

### 7. You may change default configuration in "config.ini" file (available formats "json" and "txt").

### 8. You may also change default interval.

### 9. After you change the configuration you should terminate your python session and make steps 3-6 again.

### 10. To uninstall this app please enter "uninstall snapshot" in terminal.

### 11. Default configuration (output format = txt, time interval = 5 minutes).








