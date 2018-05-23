# zabbix-docker-python
A Short Tutorial With ZABBIX Running in Docker and Python

# Dependencies
1. Docker https://www.docker.com/
2. ZABBIX https://www.zabbix.com/
3. ZABBIX already provides docker images https://hub.docker.com/u/zabbix/

# Running the Example
1. You should start the Docker container running the following command:                 
   ```docker-compose -f docker-compose-local.yml up```                                       
   You can then access the ZABBIX Web Frontend http://localhost:8081
2. Make sure that the ZABBIX server entails the right configuration
   ![Server Configuration](https://user-images.githubusercontent.com/13030569/40416348-5a6f0d36-5e7d-11e8-9afa-8125b002c087.png)
   - You need to have the *host* configured ([see ZABBIX docs](https://www.zabbix.com/documentation/3.0/manual/quickstart/host))
     - Host name: my.local.sender
     - Groups: Templates/Applications
     - Agent interfaces: keep original configuration
   - You need to have at least the *Trapper item* configured ([see ZABBIX docs](https://www.zabbix.com/documentation/3.0/manual/quickstart/item))
     - Name: Trapper item
     - Type: Zabbix trapper
     - Type of information: Numeric unsigned
3. (Optional) Create a python virtualenv                                     
   ```virtualenv -p python3 ./venv```
4. Install the python requirements                                                      
   ```pip install -r requirements.txt```  
5. Start the zabbix_client                            
   ```python zabbix_client/__init__.py```
6. You should then receive a message like this:                     
   ```{"processed": 1, "failed": 0, "total": 1, "time": "0.000140", "chunk": 1}```
7. If you get ```{"processed": 0, "failed": 1, "total": 1, "time": "0.000140", "chunk": 1}``` check your server configuration!

# Improvements
Maybe it's possible to provision the ZABBIX server in order to avoid manual configuration which is error prone.            Therefore, the api could be used.

