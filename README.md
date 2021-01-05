# PlanetTerp API Python Wrapper

This is a thin python wrapper around the [PlanetTerp API](http://api.planetterp.com/).

### Usage

```python
import planetterp

course = planetterp.course(name="CMSC132", reviews=True)
courses = planetterp.courses(department="CMSC", limit=3)
prof = planetterp.professor(name="Fawzi Emad", reviews="true")
profs = planetterp.professors(type_="ta", limit=2)
grades = planetterp.grades(course="CMSC132", professor="Fawzi Emad")

print(course)
print(courses)
print(prof)
print(profs)
print(grades)
```
