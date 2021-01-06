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
        being reviewed. Defaults to False.
    """
    params = {"name" : name, "reviews": "true" if reviews else "false"}
    url = BASE_URL + "course?" + urlencode(params)

    return requests.get(url).json()


def courses(department = None, reviews = False, limit = 100, offset = 0):
    """
    Get all courses meeting some criteria.

    Parameters
    ----------
    department: string, optional
        Only return courses in the given department. The department name must be
        four characters. Defaults to all departments.
    reviews: bool, optional
        Also return reviews for the course, specifically reviews for
        professors that taught the course and have the course listed as the one
        being reviewed. Defaults to False.
    limit: int, optional
        Maximum number of courses to return. Must be between 1 and 1000
        inclusive. Defaults to 100.
    offset: int, optional
        Number of courses to skip (offered for pagination). Defaults to 0.
    """
    params = {"department" : department,
              "reviews": "true" if reviews else "false",
              "limit": limit, "offset": offset}

    # filter out None args
    params = {k:v for k, v in params.items() if v is not None}
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


def professors(type_ = None, reviews = False, limit = 100, offset = 0):
    """
    Get all professors meeting some criteria.

    Parameters
    ----------
    type_: {"professor", "ta"}, optional
        Only return reviews for the specified instructor type, either professors
        or TAs. Defaults to returning both.
    reviews: bool, optional
        Whether to also return reviews for the instructors. Defaults to false.
    limit: int, optional
        Maximum number of instructors to return. Must be between 1 and 1000
        inclusive. Defaults to 100.
    offset: int, optional
        Number of instructors to skip (offered for pagination). Defaults to 0.
    """
    if type_ and type_ not in ["professor", "ta"]:
        raise ValueError("Expected type to be one of ['professor', 'ta'], got "
                         + str(type_))

    params = {"type" : type_, "reviews": "true" if reviews else "false",
              "limit": limit, "offset": offset}

    # filter out None args
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
        Limit the grades returned to only this course. Defaults to all courses.
        Either `course` or `professor` must be passed.
    professor: str
        The name of the professor to return grades for. Defaults to all
        professors. Either `course` or `professor` must be passed.
    semester: str, optional
        The semester to return grades for. This should be passed as the year
        followed by the semester code. The spring semester code is 01 and the
        fall semester code is 08. For example, 202001 is Spring 2020.
    section: str, optional
        Limit the grades returned to only this section. Defaults to all
        sections.

    Notes
    -----
    Either `course` or `professor` must be passed.
    """
    params = {"course" : course, "professor": professor, "semester": semester,
              "section": section}

    # filter out None args
    params = {k:v for k, v in params.items() if v is not None}
    url = BASE_URL + "grades?" + urlencode(params)

    return requests.get(url).json()
