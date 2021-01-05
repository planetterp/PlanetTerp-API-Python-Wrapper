# PlanetTerp API Python Wrapper

This is a thin python wrapper around the [PlanetTerp API](http://api.planetterp.com/).

### Usage

```python
from planetterp import course, courses, professor, professors, grades
import json

def pretty_json(json_object, indentation = 2):
    return json.dumps(json_object, indent=indentation)

course_ = course(name="CMSC132", reviews="true")
courses_ = courses(department="CMSC", limit="3")
prof = professor("Fawzi Emad", reviews="true")
profs = professors(type_="ta", reviews="true", limit="2")
grades_ = grades(course="CMSC132", professor="Fawzi Emad")

print(pretty_json(course_))
print(pretty_json(courses_))
print(pretty_json(prof))
print(pretty_json(profs))
print(pretty_json(grades_))

```
