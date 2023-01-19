# Metadata and Docs URLs

## Contents

 - [Metadata for API](#metadata)
 - [Metadata for tags](#tags)

---

<div id="metadata"></div>

## Metadata for API

You can set the following fields that are used in the OpenAPI specification and the automatic API docs UIs:

| Parameter            | Type   | Description                                                                        |
|----------------------|--------|------------------------------------------------------------------------------------|
| **title**            | str    | The title of the API.                                                              |
| **description**      | str    | A short description of the API. It can use Markdown.                               |
| **version**          | string | The version of the API. This is the version of your own application, not of OpenAPI. For example 2.5.0. |
| **terms_of_service** | str    | A URL to the Terms of Service for the API. If provided, this has to be a URL.      |
| **contact**          | dict   | The contact information for the exposed API. It can contain several fields (dict). |
| **license_info**     | dict   | The license information for the exposed API. It can contain several fields (dict). |

You can set them as follows:

[metadata.py](src/metadata.py)
```python
from fastapi import FastAPI

description = """
ChimichangApp API helps you do awesome stuff. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

app = FastAPI(
    title="ChimichangApp",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Deadpoolio the Amazing",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


@app.get("/items/")
async def read_items():
    return [{"name": "Katana"}]
```

To test run:

```python
uvicorn metadata:app --reload
```

![img](images/image01.png)  

---

<div id="tags"></div>

## Metadata for tags

You can also add additional metadata for the different **tags** used to group your path operations with the parameter <u>openapi_tags</u>.

To understand ["Metadata for tags" click here...](https://fastapi.tiangolo.com/tutorial/metadata/#metadata-for-tags)

---

**REFERENCES:**  
[Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
