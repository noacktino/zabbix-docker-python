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
2. (Optional) Create a python virtualenv                                     
   ```virtualenv -p python3 ./venv```
3. Install the python requirements                                                      
   ```pip install -r requirements.txt```  
4. Start the zabbix_client                            
   ```python zabbix_client/__init__.py```
5. You should then receive a message like this:                     
   ```{"processed": 1, "failed": 0, "total": 1, "time": "0.000140", "chunk": 1}```


