# Strategy: GIVEN-WHEN-THEN

## Contents

 - [Intro to Strategy: GIVEN-WHEN-THEN](#intro)

---

<div id="intro"></div>

## Intro to Strategy: GIVEN-WHEN-THEN

It can be difficult to get started writing tests. Where do I begin? My routine is to follow step-by-step instructions in a very simple model: GIVEN-WHEN-THEN.

 - **GIVEN:**
   - Describe the prerequisites for the test you will run and optionally make assertions about your setup
 - **WHEN:**
   - Run your function and explain what is supposed to happen.
 - **THEN:**
   - *Assert* the outcome of your test; return values or side effects.

Here's a quick example:

```python
# GIVEN the database doesn't contain any rows
assert DatabaseRow.query.count() == 0
# WHEN adding a new row to the database
new_name = 'Paul'
add_row(name=new_name, age=12)
# THEN there should be ONE new row added to the database
assert DatabaseRow.query.count() == 1
# ... with the expected name
assert DatabaseRow.query.first().name == new_name
```

---

**REFERENCES:**  
[How I test my code: motivation and strategy (part 1)](https://www.robinandeer.com/blog/2016/06/18/how-i-test-my-code-part-1)

---

**Rodrigo Leite -** *drigols*
