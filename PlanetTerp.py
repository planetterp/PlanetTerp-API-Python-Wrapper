import requests
import json

class PlanetTerp:
    url = 'https://api.planetterp.com/v1/'

    # Query Parameters
    # Name	    Type	Description
    # name	    string	Required. Show the given course.
    # reviews	boolean	Optional. Show reviews for the course (reviews for professors that taught the course and have this course listed as the one being reviewed). Default: false
    def course(self, name, reviews = False):
        request_string = self.url + 'course?name=' + name.replace(" ", "%20")
        if reviews:
            request_string += '&reviews=true'

        return requests.get(request_string).json()


    # Query Parameters
    # Name	        Type	Description
    # department	string	Optional. Only get courses in a department. Must be four characters. Default: all departments
    # reviews	    boolean	Optional. Show reviews for the course (reviews for professors that taught the course and have this course listed as the one being reviewed). Default: false
    # limit	        integer	Optional. Maximum number of records to return. Must be between 1 and 1000. Default: 100
    # offset	    integer	Optional. Number of records to skip for pagination. Default: 0
    def all_courses(self, department = None, reviews = False, limit = None, offset = None):
        request_string = self.url + 'courses?'
        if department:
            request_string += 'department=' + department + '&'
        if reviews:
            request_string += 'reviews=true' + '&'
        if limit:
            request_string += 'limit=' + str(limit) + '&'
        if offset:
            request_string += 'offset=' + str(offset) + '&'

        # We ignore the last character as it will be an extra '&'
        request_url = request_string[:-1]
        return requests.get(request_url).json()

    # Query Parameters
    # Name    Type    Description
    # name    string  Required. Show the given professor.
    # reviews boolean Optional.Show reviews for the professor.Default: false
    def professor(self, name, reviews = False):
        request_string = self.url + 'professor?name=' + name.replace(" ", "%20")
        if reviews:
            request_string += '&reviews=true'

        return requests.get(request_string).json()

    # Query Parameters
    # Name	    Type	Description
    # type	    string	Optional. Show only reviews for professors or teaching assistants. Default: show both. Options: professor, ta
    # reviews	boolean	Optional. Show reviews for the professors. Default: false
    # limit	    integer	Optional. Maximum number of records to return. Must be between 1 and 1000. Default: 100
    # offset	integer	Optional. Number of records to skip for pagination. Default: 0
    def all_professors(self, type_ = None, reviews = False, limit = None, offset = None):
        request_string = self.url + 'professors?'
        if type_:
            request_string += 'type=' + type_ + '&'
        if reviews:
            request_string += 'reviews=true' + '&'
        if limit:
            request_string += 'limit=' + str(limit) + '&'
        if offset:
            request_string += 'offset=' + str(offset) + '&'

        # We ignore the last character as it will be an extra '&'
        request_url = request_string[:-1]
        return requests.get(request_url).json()


    # Query Parameters
    # Name	    Type	Description
    # course	string	Optional. Show only grades for the given course.
    # professor	string	Optional. Show only grades for the given professor.
    # semester	string	Optional. Show only grades for the given semester. Semester should be provided as the year followed by the semester code. 01 means Spring and 08 means Fall. For example, 202001 means Spring 2020. Default: all semesters
    # section	string	Optional. Show only grades for the given section. Default: all sections
    def grades(self, course = None, professor = None, semester = None, section = None):
        request_string = self.url + 'grades?'
        if not course and not professor:
            print("Error! Must provide either a course or professor as input")
            return None
        if course:
            request_string += 'course=' + course + '&'
        if professor:
            request_string += 'professor=' + professor.replace(" ", "%20") + '&'
        if semester:
            request_string += 'semester=' + semester + '&'
        if section:
            request_string += 'section=' + section + '&'

        # We ignore the last character as it will be an extra '&'
        request_url = request_string[:-1]
        return requests.get(request_url).json()
    
    
