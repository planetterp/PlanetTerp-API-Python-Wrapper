# PlanetTerp API Python Wrapper

This is a Python wrapper around the [PlanetTerp API](http://api.planetterp.com).

To install, either use [the code on GitHub](https://github.com/planetterp/PlanetTerp-API-Python-Wrapper), or install with `pip install planetterp` (you might need to run `pip3 install planetterp`).

### Example usage

```python
import planetterp

course_ = planetterp.course(name="CMSC132", reviews=True)
courses_ = planetterp.courses(department="CMSC", limit=3)
prof = planetterp.professor(name = "Fawzi Emad", reviews="true")
profs = planetterp.professors(type_="ta", limit=2)
grades_ = planetterp.grades(course="CMSC132", professor="Fawzi Emad")

print(course_)
print(courses_)
print(prof)
print(profs)
print(grades_)

```
