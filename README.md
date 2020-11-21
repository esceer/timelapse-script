# timelapse-script
This is a python script for capturing camera picture and saving it to a configured place. While this script can either capture multiple frame after a given delay but single runs can also be triggered from cron.

### Install
1. python3 -m venv venv
2. venv/bin/pip install --upgrade pip
3. venv/bin/pip install -r requirements.txt

### Usage
##### Via shell script
bin/run_timelapse.sh

##### Directly via python3
venv/bin/python3 timelapse.py <timelapse_output_directory>

### Timing
Crontab is used to schedule the script *(every X minutes)*
which initiates which takes a photo of the connected cam and saves it under the output directory.

##### Configure
crontab -u <*username*> -e
<br/>
*/5 * * * * <*install_dir*>/timelapse-script/bin/run_timelapse.sh <*timelapse_output_directory*>

