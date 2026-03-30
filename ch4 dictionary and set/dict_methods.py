dit = {"name": "Alice",
           "marks": {"math": 85, "science": 90, "literature": 78},
           "passed": True}

print(dit.keys())
print(dit.values())
print(dit.items())
print(dit.get("name"))
print(dit.get("age", "Not found"))
dit.update({"age": 25, "city": "New York"})
print(dit)