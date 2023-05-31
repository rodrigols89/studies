# GitHub Actions

## Contents

 - **Examples:**
   - [Create a CI to codecov Pipeline](#codecov-example)
 - [**References**](#references)

<!--- ( Examples ) -->

---

<div id="codecov-example"></div>

## Create a CI to codecov Pipeline

 - To start let's, create a directory **".github/workflows"**.
 - Now, inside the **/workflows** directory let's create **test.yaml** file.

Now, let's add a name (Tests) to this pipeline.

[.github/workflows/test.yaml](.github/workflows/test.yaml)
```yaml
name: Tests
```

Now, let's add a **"trigger (gatilho)"** to this pipeline, that's, what action on GitHub will call these tests. For this, we use "on" statement:

[.github/workflows/test.yaml](.github/workflows/test.yaml)
```yaml
name: Tests
on: [push, pull_request] # triggers (gatilhos) list
```

> **NOTE:**<br>
> The tests always run on **"push"** and **"pull_request"**.

Now, let's add a **"job"** to the pipeline.

[.github/workflows/test.yaml](.github/workflows/test.yaml)
```yaml
name: Tests
on: [push, pull_request] # triggers (gatilhos) list

jobs:
```

> **Ok, but how we called the job?**

Let's, call **"coverage"**:

[.github/workflows/test.yaml](.github/workflows/test.yaml)
```yaml
name: Tests
on: [push, pull_request] # triggers (gatilhos) list

jobs:
  coverage:
```

> **Ok, but where is this going to run? (Ok, mas onde isso vai rodar?)**

Let's, configure to run on ubuntu. For this, we use the **"runs-on"** statement:

[.github/workflows/test.yaml](.github/workflows/test.yaml)
```yaml
name: Tests
on: [push, pull_request] # triggers (gatilhos) list

jobs:
  coverage:
    runs-on: ubuntu-latest
```

**NOTE - You can check another Operating Systems to use here:**<br>
[About GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners)

Now, let's create some **"steps"** on our container (ubuntu). In the first step, let's copy your local project files to the container, and for that let's use the [Checkout GitHub Action](https://github.com/actions/checkout):

[.github/workflows/test.yaml](.github/workflows/test.yaml)
```yaml
steps:
  - name: Copy local (repository) files to remote container
    uses: actions/checkout@v3  # Get latest 3.x
```

In the next **"step"** let's install **Python** in our container (ubuntu):

[.github/workflows/test.yaml](.github/workflows/test.yaml)
```yaml
- name: Install Python
  uses: actions/setup-python@v4  # Get latest 4.x
  with:
    python-version: '3.11'
```

With Python installed in the next **"step"**, let's add **Poetry** tool:

[.github/workflows/test.yaml](.github/workflows/test.yaml)
```yaml
- name: Install Poetry tool
  run: pip install poetry
```

Now, in the next **"step"** let's install the project dependencies (without docs dependencies) on our container (ubuntu):

[.github/workflows/test.yaml](.github/workflows/test.yaml)
```yaml
- name: Install project dependencies
  run: poetry install --without doc  # Not install doc dependencies.
```

In the next **"step"** let's use Poetry to run **"task test --cov-report=xml"** statement, that's, let's run the project tests:

[.github/workflows/test.yaml](.github/workflows/test.yaml)
```yaml
- name: Run tests
  run: poetry run task test --cov-report=xml  # Use poetry to run test without env.
```

Finally, let's configure the **codecov.io** to coverage our tests. Go to [https://app.codecov.io/gh](https://app.codecov.io/gh):

 - Select your repository by clicking:
   - Not yet enabled setup repo
 - Get your CODECOV_TOKEN=????????? and add to your repository:
   - Secrets and variables:
     - Actions:
       - Secrets (Not variables):
         - New repository secret
           - Name: CODECOV_TOKEN
           - Secret: your-secret
           - Finally, "Add Secret".

Now, let's add a "step" to coverage:

[.github/workflows/test.yaml](.github/workflows/test.yaml)
```yaml
      - name: Up coverage for codecov
        uses: codecov/codecov-action@v3  # Get latest 3.x
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
```

Finally, let's get codecov and pipeline badges:

 - To get a Pipeline badge change the link below to your repository:
   - `[![CI](https://github.com/drigols/musical-notes/actions/workflows/pipeline.yaml/badge.svg)](https://github.com/drigols/musical-notes/actions/workflows/pipeline.yaml)`
 - To get a codecov badge:
   - Go to [https://app.codecov.io/gh/](https://app.codecov.io/gh/)
   - Select your covered project.
   - Settings > Badges & Graphs > Markdown:
     - `[![codecov](https://codecov.io/gh/dota2learning/d2l/branch/main/graph/badge.svg?token=O2FMF315N4)](https://codecov.io/gh/dota2learning/d2l)`


<!--- ( References ) -->

---

<div id="references"></div>

## References

 - [Configurando Integração contínua para o nosso pacote Python com GitHub Actions #CodaComigo](https://www.youtube.com/watch?v=1C6Pe3Wy7Mc)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
