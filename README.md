# PlanetTerp API Python Wrapper

This is a Python wrapper around the [PlanetTerp API](http://api.planetterp.com).

To install, either use [the code on GitHub](https://github.com/planetterp/PlanetTerp-API-Python-Wrapper), or install with `pip install planetterp` (you might need to run `pip3 install planetterp`).

### Example usage

```python
import planetterp

course = planetterp.course(name="CMSC131", reviews=True)
courses = planetterp.courses(department="CMSC", limit=2)
prof = planetterp.professor(name="TBA", reviews="true")
profs = planetterp.professors(type_="ta", limit=2)
grades = planetterp.grades(course="CMSC131", professor="TBA")

print(course)
print(courses)
print(prof)
print(profs)
print(grades)
```
