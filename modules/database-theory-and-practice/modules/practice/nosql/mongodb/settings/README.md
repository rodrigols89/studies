# Settings

## Contents

 - [MongoDB Settings (Linux Approach)](#mongo-linux-settings)
 - [Docker Compose Settings](#docker-settings)
 - [Python Settings](#python-settings)

---

<div id="mongo-linux-settings"></div>

## MongoDB Settings (Linux Approach)

 - MongoDB stores data in **db** folder within **data** folder. But, since this data folder is not created automatically, you have to create it manually.
 - Remember that data directory should be created in the root (/).

```
cd /
```

```
sudo mkdir data
```

```
cd data
```

```
sudo mkdir db
```

```
cd db
```

---

<div id="docker-settings"></div>

## Docker Compose Settings

I strongly recommender install Docker container that contains MongoDB installed:

```
sudo docker compose up -d
```

Now, only enter into MongoDB into the container:

```
sudo docker exec -it mongodb-testing bash
```

Finally, to run the MongoDB inside the container run:

```
mongosh
```

To quit run:

```
exit()
```

---

<div id="python-settings"></div>

## Python Settings

**CREATE VIRTUAL ENVIRONMENT:**  
```python
python -m venv environment
```

**ACTIVATE THE VIRTUAL ENVIRONMENT:**  
```python
source environment/bin/activate
```

**UPDATE PIP:**
```
python -m pip install --upgrade pip
```

**INSTALL PYTHON DEPENDENCIES:**  
```python
pip install -U -v --require-virtualenv -r requirements.txt
```

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
