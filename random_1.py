import random

def generate_info():
  names = ["Alice", "Bob", "Charlie", "Daisy"]
  cities = ["New York", "London", "Paris", "Tokyo"]
  countries = ["USA", "UK", "France", "Japan"]
  activities = ["reading", "writing", "singing", "dancing"]

  name = random.choice(names)
  age = random.randint(18, 99)
  gender = random.choice(["male", "female"])
  city = random.choice(cities)
  country = random.choice(countries)
  activity = random.choice(activities)

  return {
    "name": name,
    "age": age,
    "gender": gender,
    "city": city,
    "country": country,
    "activity": activity
  }

info = generate_info()

html = """
<html>
<head>
  <title>About Me</title>
</head>
<body>
  <h1>About Me</h1>
  <p>Hello, my name is {name} and I am a {age} year old {gender}. I live in {city}, {country} and I love to spend my time {activity}.</p>
  <p>One funny anecdote about me is:</p>
  <p>I once tried to teach my cat to fetch, but she just looked at me like I was crazy and went back to sleep. I guess she's more of a "catch and release" kind of feline.</p>
</body>
</html>
""".format(**info)

print(html)