# PlanetTerp API Python Wrapper

This is a thin python wrapper around the [PlanetTerp API](http://api.planetterp.com/).

### Usage

```python
import planetterp

course_ = planetterp.course(name="CMSC132", reviews=True)
courses_ = planetterp.courses(department="CMSC", limit=3)
prof = planetterp.professor("Fawzi Emad", reviews="true")
profs = planetterp.professors(type_="ta", limit=2)
grades_ = planetterp.grades(course="CMSC132", professor="Fawzi Emad")

print(course_)
print(courses_)
print(prof)
print(profs)
print(grades_)

```
