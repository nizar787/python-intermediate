courses = {
    "js": "JavaScript",
    "python": ["Python", "Python"],
    "html": "HTML"
}

# print(courses.get("css", "CSS"))
if courses.get("css", None):
    print("You are enrolled in CSS")
