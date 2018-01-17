
### Notes:
* What is currently built
  * Basic authentication
  * SSL (need key on droplet though)
  * Basic loan calculator
  * Unittests for loan calc
  * Dev and prod server deployment options
  * Basic error handling
  * Help documentation
  *

### Instructions for setting up:
1. Download repo 
```
git clone https://github.com/mclaypool/finance_api.git
```
2. Install system deps it not installed
```
sudo apt-get install sqlite3 python-pip
pip install --user virtualenv
```
3. Create the env 
```
cd finance_api/sandbox_api/
virtualenv -p python3 env
source env/bin/activate
```
4. Install deps 
```
pip install -r requirements.txt
```
5. Run the app! 
```
python run.py
```
