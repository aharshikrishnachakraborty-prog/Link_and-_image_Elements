"""Info={
    "Key": "Value",
    "Name": "Aharshi",
    "learning": "Python",
    "Ke": "Value",
}
print(Info["learning"])"""

student = {
    "Name": "Aharshi",
    "Age": 20,
    "Grade": "A+++",
    "Subjects":{
        "Phy":100,
        "Chem":100,
        "Maths":100,
    }
}
print(student["Subjects"]["Maths"])
print(list(student.keys()))
print(tuple(student.values()))
print(student.items())
print(student.get("Age"))
print(student.update({"Age":21}))