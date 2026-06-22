---
title: "GitHub - middlewarehq/middleware: ✨ Open-source DORA metrics platform for"
source: "https://github.com/middlewarehq/middleware"
author: "github.com/middlewarehq"
published: 
created: 2026-05-07
description: "✨ Open-source DORA metrics platform for engineering teams ✨ - middlewarehq/middleware"
tags:
  - to-process
  - dev-tools
---

# middlewarehq/middleware


[![Middleware Logo](https://github.com/middlewarehq/middleware/raw/main/media_files/logo.png)](https://www.middlewarehq.com/)
**Open-source engineering management that unlocks developer potential**


[![continuous integration](https://camo.githubusercontent.com/d72013fe354cb76bdb62fae188d011c4d1bce7723189bacad6cbde6387cf52e6/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f6d6964646c657761726568712f6d6964646c65776172652f6275696c642e796d6c3f6272616e63683d6d61696e266c6162656c3d6275696c64267374796c653d666f722d7468652d6261646765)](https://github.com/middlewarehq/middleware/actions/workflows/build.yml)
[![Commit activity per month](https://camo.githubusercontent.com/b694441288287fd6f4c8750f3887fcc6853aef9bfc84ee8a0e1e490a7633639a/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f636f6d6d69742d61637469766974792f6d2f6d6964646c657761726568712f6d6964646c65776172653f7374796c653d666f722d7468652d6261646765)](https://github.com/middlewarehq/middleware/graphs/commit-activity)
[![contributors](https://camo.githubusercontent.com/15f7e201a0b0e240425157b1a7251f24a91dcd6b6bbec76af4ad66efda00eeba/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f636f6e7472696275746f72732d616e6f6e2f6d6964646c657761726568712f6d6964646c65776172653f636f6c6f723d79656c6c6f77267374796c653d666f722d7468652d6261646765)](https://github.com/middlewarehq/middleware/graphs/contributors)
[![license](https://camo.githubusercontent.com/44fae73fb8fb80dc9f5673dc4e1d0e57b1ac81da1166a70c8a5ce52bb39ed67f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f617061636865253230322e302d707572706c652e7376673f7374796c653d666f722d7468652d6261646765266c6162656c3d6c6963656e7365)](https://opensource.org/licenses/Apache-2.0)
[![Stars](https://camo.githubusercontent.com/eab8dfd78113b2679d98f9f33a66e3a157276c68cc4cf3541fa1287f4dddb379/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f6d6964646c657761726568712f6d6964646c65776172653f7374796c653d666f722d7468652d6261646765)](https://camo.githubusercontent.com/eab8dfd78113b2679d98f9f33a66e3a157276c68cc4cf3541fa1287f4dddb379/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f6d6964646c657761726568712f6d6964646c65776172653f7374796c653d666f722d7468652d6261646765)
[Join our Open Source Community](https://mhq.link/oss-community)


[![Middleware Opensource](https://github.com/middlewarehq/middleware/raw/main/media_files/banner.gif)](https://github.com/middlewarehq/middleware/blob/main/media_files/banner.gif)
  [![Middleware Opensource](https://github.com/middlewarehq/middleware/raw/main/media_files/banner.gif)](https://github.com/middlewarehq/middleware/blob/main/media_files/banner.gif)  


## Introduction


**Middleware** is an open-source tool designed to help engineering leaders measure and analyze the effectiveness of their teams using the [DORA metrics](https://dora.dev). The DORA metrics are a set of [four key values](https://dora.dev/guides/dora-metrics-four-keys/) that provide insights into software delivery performance and operational efficiency.


They are:


* **Deployment Frequency**: The frequency of code deployments to production or an operational environment.
* **Lead Time for Changes**: The time it takes for a commit to make it into production.
* **Mean Time to Restore**: The time it takes to restore service after an incident or failure.
* **Change Failure Rate**: The percentage of deployments that result in failures or require remediation.


**Table of Contents**


* [Middleware - Open Source](https://github.com/middlewarehq/middleware#introduction)
	+ [Features](https://github.com/middlewarehq/middleware#-features)
	+ [Quick Start](https://github.com/middlewarehq/middleware#-quick-start)
		- [Installing Middleware](https://github.com/middlewarehq/middleware#-installing-middleware)
		- [Troubleshooting](https://github.com/middlewarehq/middleware#%EF%B8%8F-troubleshooting)
	+ [Developer Setup](https://github.com/middlewarehq/middleware#-developer-setup)
		- [Using Gitpod](https://github.com/middlewarehq/middleware#%EF%B8%8F-using-gitpod)
		- [Using Docker](https://github.com/middlewarehq/middleware#-using-docker)
		- [Manual Setup](https://github.com/middlewarehq/middleware#%EF%B8%8F-manual-setup)
	+ [Usage](https://github.com/middlewarehq/middleware#-usage)
	+ [How we Calculate DORA](https://github.com/middlewarehq/middleware#-how-we-calculate-dora)
	+ [Roadmap](https://github.com/middlewarehq/middleware#%EF%B8%8F-roadmap)
	+ [Contributing guidelines](https://github.com/middlewarehq/middleware#%EF%B8%8F-contributing-guidelines)
	+ [Developer Automations](https://github.com/middlewarehq/middleware#-developer-automations)
	+ [Security guidelines](https://github.com/middlewarehq/middleware#%EF%B8%8F-security-guidelines)
	+ [License](https://github.com/middlewarehq/middleware#license)


## 🚀 Features


* Integration with various CI/CD tools
* Automated collection and analysis of DORA metrics
* Visualization of key performance indicators
* Customizable reports and dashboards
* Integration with popular project management platforms


## ✨ Quick Start


### ⭐ Installing Middleware


* Ensure that you have [docker](https://www.docker.com/products/docker-desktop/) installed and running.
* Open the terminal and run the following command:

 
```
docker volume create middleware_postgres_data
docker volume create middleware_keys
docker run --name middleware \
           -p 3333:3333 \
           -p 9696:9696 \
           -p 9697:9697 \
           -v middleware_postgres_data:/var/lib/postgresql/data \
           -v middleware_keys:/app/keys \
           -d middlewareeng/middleware:latest
docker logs -f middleware
```


* Wait for sometime for the services to be up.
* The app shall be available on your host at <http://localhost:3333>.


## 🛠️ Troubleshooting


1. In case you want to stop the container, run the following command:

 
```
docker stop middleware
```
2. In order to fetch latest version from remote and then starting the system, use following command:

 
```
docker pull middlewareeng/middleware:latest
docker rm -f middleware || true
docker run --name middleware \
           -p 3333:3333 \
           -v middleware_postgres_data:/var/lib/postgresql/data \
           -v middleware_keys:/app/keys \
           -d middlewareeng/middleware:latest
docker logs -f middleware
```
3. If you see an error like: `Conflict. The container name "/middleware" is already in use by container`.   
 Then run following command before running the container again:

 
```
docker rm -f middleware
```
4. If you wish to delete all the data saved in the container, you can delete the volumes created by running the following command:

 
```
docker volume rm middleware_postgres_data middleware_keys
```


## 👩‍💻 Developer Setup


### ☁️ Using GitPod


Gitpod enables development on remote machines and helps you get started with Middleware if your machine does not support running the project locally.


If you want to run the project locally you can [setup using docker](https://github.com/middlewarehq/middleware#-using-docker) or [setup everything manually](https://github.com/middlewarehq/middleware#-manual-setup).


1. Click the button below to open this project in Gitpod.
2. This will open a fully configured workspace in your browser with all the necessary dependencies already installed.


[![Open in Gitpod](https://camo.githubusercontent.com/b04f5659467d23b5109ba935a40c00decd264eea25c22d50a118021349eea94f/68747470733a2f2f676974706f642e696f2f627574746f6e2f6f70656e2d696e2d676974706f642e737667)](https://gitpod.io/#https://github.com/middlewarehq/middleware)
After initialization, you can access the server at port 3333 of the gitpod instance.


### 🐳 Using Docker


Important


We recommend minimum 16GB RAM when developing locally.


If you don't have docker installed, please install docker [over here](https://docs.docker.com/get-docker/). Make sure docker is running.


1. **Clone the Repository**:

 
```
git clone https://github.com/middlewarehq/middleware
```
2. **Navigate to the Project Directory**:

 
```
cd middleware
```
3. **Run `dev.sh` script in the project root 🪄**  
 `./dev.sh` creates a `.env` file with required development environments and runs a CLI with does all the heavy lifting from tracking the container with `docker compose watch` to providing you with logs from different services.  
 The usage is as follows:

 
```
./dev.sh
```
 You may update the `env.example` and set `ENVIRONMENT=prod` to run it in production setup.  
 Further if any changes are required to be made to ports, you may update the `docker-compose.yml` file, accordingly.
4. **Access the Application**: Once the project is running, access the application through your web browser at <http://localhost:3333>. Further, other services can be accessed at:


	* The analytics server is available at <http://localhost:9696>.
	* The sync server can be accessed at <http://localhost:9697>.
	* The postgres database can be accessed at host: `localhost`, port: `5434`, username: `postgres`, password: `postgres`, db name: `mhq-oss`.
	* The redis server can be accessed at host: `localhost`, port: `6385`.
5. **View the logs**: Although the CLI tracks all logs, the logs of services running inside the container can be viewed in different terminals using the following commands:

 **Frontend logs**

 
```
docker exec -it middleware-dev tail --lines 500 -f /var/log/web-server/web-server.log
```
 **Backend api server logs**

 
```
docker exec -it middleware-dev tail --lines 500 -f /var/log/apiserver/apiserver.log
```
 **Backend sync server logs**

 
```
docker exec -it middleware-dev tail --lines 500 -f /var/log/sync_server/sync_server.log
```
 **Redis logs**

 
```
docker exec -it middleware-dev tail --lines 500 -f /var/log/redis/redis.log
```
 **Postgres logs**

 
```
docker exec -it middleware-dev tail --lines 500 -f /var/log/postgres/postgres.log
```


## 🛠️ Manual Setup


To set up middleware locally, follow these steps:


1. **Clone the Repository**:

 
```
git clone https://github.com/middlewarehq/middleware.git
```
2. **Navigate to the Project Directory**:

 
```
cd middleware
```
3. **Run Redis and Postgres Containers**:

 If you don't have docker installed, please install docker [over here](https://docs.docker.com/get-docker/)

 Run the following commands to run Postgres and Redis using docker.

 
```
cd database-docker && docker-compose up -d
```
 If you don't prefer Docker, you can choose to install [Postgres](https://www.postgresql.org/download/) and [Redis](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/) manually.

 Once you are done with using or developing Middleware, you can choose to close these running container. (NOTE: Don't do this if you are following this document and trying to run Middleware.)

 
```
cd database-docker/
docker-compose down -v
```
4. **Generate Encryption keys**:

 Generate encryption keys for the project by running the following command in the project root directory:

 
```
cd setup_utils && . ./generate_config_ini.sh && cd ..
```
5. **Backend Server Setup**


	* Install python version `3.11.6`
	
	
		+ For this you can install python from [over here](https://www.python.org/downloads/) if you don't have it on your machine.
		+ Install pyenev
		
		 
		```
		git clone https://github.com/pyenv/pyenv.git ~/.pyenv
		```
		+ Add pyenv to your shell's configuration file (.bashrc, .bash\_profile, .zshrc, etc.):
		
		 
		```
		echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
		echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
		```
		+ Reload your shell:
		
		 
		```
		source ~/.bashrc
		
		```
	* Move backend directory to create a virtual environment
	
	 
	```
	cd backend
	python -m venv venv
	```
	* Activate virtual environment
	
	 
	```
	. venv/bin/activate
	```
	* Install Dependencies
	
	 
	```
	pip install -r requirements.txt -r dev-requirements.txt
	```
	* Create a `.env` file in the root directory and add the following environment variables, replacing the values with your own if needed:
	
	 
	```
	DB_HOST=localhost
	DB_NAME=mhq-oss
	DB_PASS=postgres
	DB_PORT=5434
	DB_USER=postgres
	REDIS_HOST=localhost
	REDIS_PORT=6385
	ANALYTICS_SERVER_PORT=9696
	SYNC_SERVER_PORT=9697
	DEFAULT_SYNC_DAYS=31
	
	```
	* Start the backend servers
	
	
		+ Change Directory to analytics\_server
		
		 
		```
		cd analytics_server
		```
		+ For backend analytics server:
		
		 
		```
		flask --app app --debug run --port 9696
		```
		+ For backend sync server:
		
		 
		```
		flask --app sync_app --debug run --port 9697
		```
		 NOTE: Open this sync sever in a new terminal window after activating the virtual environment only after starting analytics server.
6. **Web Server Setup**


	* Install NodeJs 16.17 (LTS) either [manually](https://nodejs.org/en/download) or using a tool like [nvm](https://github.com/nvm-sh/nvm) or [volta](https://volta.sh/).
	* Install `yarn` package manager
	
	 
	```
	npm install --global yarn
	```
	* Change Directory to web-server and install packages
	
	 
	```
	cd web-server
	yarn
	```
	* Start the web-server
	
	 
	```
	yarn dev
	```
7. **Access the Application**: Once the project is running, access the application through your web browser at <http://localhost:3333>.   
 Additionally:


	* The analytics server is available at <http://localhost:9696>.
	* The sync server can be accessed at <http://localhost:9697>.


# 🚀 Usage


[![Product Demo](https://github.com/middlewarehq/middleware/raw/main/media_files/product_demo_1.gif)](https://github.com/middlewarehq/middleware/blob/main/media_files/product_demo_1.gif)
  [![Product Demo](https://github.com/middlewarehq/middleware/raw/main/media_files/product_demo_1.gif)](https://github.com/middlewarehq/middleware/blob/main/media_files/product_demo_1.gif)  


* Setup the project by following the [steps mentioned above](https://github.com/middlewarehq/middleware#-quick-start).
* Generate and Add your PAT token from code provider.
* Create a team and select repositories for the team.
* See Dora Metrics for your team.
* Update settings related to incident filters, excluded pull requests, prod branches etc to get more accurate data.


# 📖 How we Calculate DORA


Middleware can display DORA Metrics using exclusively GitHub Data. The aim is to provide DORA metrics to anyone and everyone using their Git data, regardless of other integrations.


DORA metrics are derived from Pull Requests, Deployments, and Incidents.


For simplicity, we synchronize your Pull Request data and classify reverted Pull Requests as incidents and merged Pull Requests as Deployments.


**Lead Time for Changes**


* Lead time consists of First Commit to PR Open time, First Response Time, Rework Time, Merge Time, and Merge to Deploy Time.
* When calculating DORA using git-based data, PR merges are regarded as deployments, hence the merge to deploy time is considered as 0, while the rest of the time components remain the same.


**Deployment Frequency**


* This metric gauges how frequently code changes are deployed to production.
* When considering PR merges as deployments, this can also represent the daily/weekly/monthly frequency of PR merges.


**Mean Time to Recover (MTTR)**


* MTTR measures how swiftly a team can restore service after a failure occurs in production.
* The team's average incident resolution time is utilized to compute its MTTR.
* When treating Revert PRs as incidents, the resolution time for an incident is calculated from the merging of the original PR to the merging of the revert PR.


**Change Failure Rate (CFR)**


* CFR quantifies the percentage of changes that result in a service impairment or outage in production, aiding in the evaluation of deployment process stability and reliability.
* CFR is computed by linking incidents to deployments within an interval; each deployment may have several or no incidents.
* Deployments that can be linked to any incident are considered as causing a failure or outage.
* The fraction of deployments causing outages to the total deployments in an interval is used to determine the CFR.


## 🛣️ Roadmap


Coming Soon!


## ❤️ Contributing guidelines


[![contributor Metrics](https://camo.githubusercontent.com/584a70e9870ba6e99d50f5387bc966306490a20f84b71ef0ca27b21120cadb88/68747470733a2f2f6f70656e2d736f757263652d6173736574732e6d6964646c657761726568712e636f6d2f737667732f6d6964646c657761726568712d6d6964646c65776172652d636f6e7472696275746f722d6d6574726963732d6461726b2d7769646765742d7072656d69756d2e737667)](https://camo.githubusercontent.com/584a70e9870ba6e99d50f5387bc966306490a20f84b71ef0ca27b21120cadb88/68747470733a2f2f6f70656e2d736f757263652d6173736574732e6d6964646c657761726568712e636f6d2f737667732f6d6964646c657761726568712d6d6964646c65776172652d636f6e7472696275746f722d6d6574726963732d6461726b2d7769646765742d7072656d69756d2e737667)
To get started contributing to middleware check out our [CONTRIBUTING.md](https://github.com/middlewarehq/middleware/blob/main/CONTRIBUTING.md).


We appreciate your contributions and look forward to working together to make Middleware even better!


## 👨‍💻 Developer Automations


This sections contains some automation scripts that can generate boilerplate code to extend certain features and ship faster 🚀


### 1. Adding New Settings in Backend


* Context: Initially, adding a new setting required context of the settings system, changes across some files and making adapters and defaults based on the new setting class structure.
* This can now be done by running the `python make_new_setting.py` script in the `./backend/dev_scripts` directory


If you are in the root directory, you can run:



```
python ./backend/dev_scripts/make_new_setting.py

```

* Enter the setting name in the consitent format.
* Add the required keys and their types. Enter `done` once you have added all the fields.
* Update imports and linting.
* You are good to go :tada"
* Note: For more non-primitive types in the setting such as uuid, enums etc, you will have to make changes to the generated adaptors.


  setting\_creation\_automation.mp4    
# ⛓️ Security guidelines


To get started contributing to middleware check out our [SECURITY.md](https://github.com/middlewarehq/middleware/blob/main/SECURITY.md).


We look forward to your part in keeping Middleware secure!


## License


This project is licensed under the [Apache 2.0](https://github.com/middlewarehq/middleware/blob/main/LICENSE) License - see the LICENSE.md file for details.


[![Banner](https://github.com/middlewarehq/middleware/raw/main/media_files/banner.png)](https://github.com/middlewarehq/middleware/blob/main/media_files/banner.png)