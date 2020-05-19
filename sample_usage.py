import PlanetTerp
import json

def pretty_json(json_object, indentation = 2):
    return json.dumps(json_object, indent=indentation)

pt = PlanetTerp.PlanetTerp()

#print(pretty_json(pt.course(name="CMSC132", reviews="true")))

#print(pretty_json(pt.all_courses(department="CMSC", limit="3")))

#print(pretty_json(pt.professors("Fawzi Emad", reviews="true")))

#print(pretty_json(pt.all_professors(type="ta", reviews="true", limit="2")))

#print(pretty_json(pt.grades(course="CMSC132", professor="Fawzi Emad")))