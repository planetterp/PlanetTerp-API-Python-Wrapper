import requests
import json
from urllib.parse import urlencode, quote

BASE_URL = 'https://api.planetterp.com/v1/'

def course(name, reviews = False):
    """
    Get a course.

    Parameters
    ----------
    name: string
        The name of the course.
    reviews: bool, optional
        Whether to also return reviews for the course, specifically reviews for
        professors that taught the course and have the course listed as the one
        being reviewed.
    """
    params = {"name" : name, "reviews": "true" if reviews else "false"}
    url = BASE_URL + "course?" + urlencode(params)
    return requests.get(url).json()


def all_courses(department = None, reviews = False, limit = 100, offset = 0):
    """
    Get all courses meeting some criteria.

    Parameters
    ----------
    department: string
        Only return courses in the given department. The department name must be
        four characters. Defaults to all departments.
    reviews: bool
        Also return reviews for the course, specifically reviews for
        professors that taught the course and have the course listed as the one
        being reviewed.
    limit: int
        Maximum number of courses to return. Must be between 1 and 1000
        inclusive. Defaults to 100.
    offset: int
        Number of courses to skip (offered for pagination). Defaults to 0.
    """
    params = {"department" : department,
              "reviews": "true" if reviews else "false",
              "limit": limit, "offset": offset}
    url = BASE_URL + "courses?" + urlencode(params)
    return requests.get(url).json()


def professor(name, reviews = False):
    """
    Get a professor.

    Parameters
    ----------
    name: str
        The name of the professor.
    reviews: bool, optional
        Whether to also return reviews for the given professor. Defaults to
        false.
    """
    params = {"name" : name, "reviews": "true" if reviews else "false"}
    url = BASE_URL + "professor?" + urlencode(params)
    return requests.get(url).json()


def all_professors(type_ = None, reviews = False, limit = None, offset = None):
    """
    Get all professors meeting some criteria.

    Parameters
    ----------
    type_: {"professor", "ta"}
        Only return reviews for the specified instructor type, either professors
        or TAs. Defaults to returning both.
    reviews: bool
        Also return reviews for the instructors. Defaults to false.
    limit: int
        Maximum number of courses to return. Must be between 1 and 1000
        inclusive. Defaults to 100.
    offset: int
        Number of courses to skip (offered for pagination). Defaults to 0.
    """
    if type_ not in ["professor", "ta"]:
        raise ValueError("Expected type to be on of ['professor', 'ta'], got "
                         + str(type_))
    params = {"type" : type_, "reviews": "true" if reviews else "false",
              "limit": limit, "offset": offset}
    # fitler out None args
    params = {k:v for k, v in params.items() if v is not None}
    url = BASE_URL + "professors?" + urlencode(params)
    return requests.get(url).json()


def grades(course = None, professor = None, semester = None, section = None):
    """
    Get grades for a given course, professor, semester, section, or combination
    thereof.

    Parameters
    ----------
    course: str
        Limit the grades returned to only this course.
    professor: str
        The name of the professor to return grades for.
    semester: str
        The semester to return grades for. This should be passed as the year
        followed by the semester code. The spring semester code is 01 and the
        fall semester code is 08. For example, 202001 is Spring 2020.
    """
    params = {"course" : course, "professor": professor, "semester": semester,
              "section": section}
    params = {k:v for k, v in params.items() if v is not None}
    url = BASE_URL + "grades?" + urlencode(params)
    return requests.get(url).json()
