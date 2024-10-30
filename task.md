# using_python_iterables_and_collection
Exploring the functions that work with iterables and collections

# Task - Maths with dictionary elements

You're given two dictionaries. Both have the same keys `a`, `b`, `c` with their values being random numbers. You need to multiply the values with the same key value in the other dict and sum all results.

## Input:

```
dict1 = {
  'a': 4,
  'b': 16,
  'c': 3
}

dict2 = {
  'a': 8,
  'b': 2,
  'c': 3
}
```

## Output:

```
73
```

# Task - Convert keys between cases

Different programming languages use different kind of schemes to name things. For example Python uses `snake_case`, JavaScript uses `camelCase`. You might also come across `kebap-case` - sometimes also called `dash-case`. You can read more about naming conventions in programming the [matching Wikipedia article](https://en.wikipedia.org/wiki/Naming_convention_(programming)).

When an API you are using is implemented using a different language it might not match Python's convention of naming things. Hence your task is to implement a method that converts a dictionary with natural cased keys like `A random key` to `a_random_key`.

## Input A:

```python
natural_case = {
  'Company name': 'Digital Career Institute',
  'Street': 'Vulkanstraße',
  'House Number': 1,
  'City': 'Berlin'
}
```

## Output A:

```python
snake_case = {
  'company_name': 'Digital Career Institute',
  'street': 'Vulkanstraße',
  'house_number': 1,
  'city': 'Berlin'
}
```

## Input B:

```python
natural_case = {
  'Movie name': 'James Bond 007: Skyfall',
  'Director': 'Sam Mendes',
  'Production Year': 2012,
  'Duration in minutes': 143,
  'Production countries': ['US', 'UK']
}
```

## Output B:

```python
snake_case = {
  'movie_name': 'James Bond 007: Skyfall',
  'director': 'Sam Mendes',
  'production_year': 2012,
  'duration_in_minutes': 143,
  'production_countries': ['US', 'UK']
}
```

# Task - Matrix mean

You are given a two dimensional list of numbers. Calculate the mean of those numbers by implementing a `mean` method that takes a list as an argument.

## Input:

```
numbers = [[5, 6, 3], [8, 3, 1], [9, 10, 4], [8, 4, 2]]
```

## Output:

```
> mean(numbers)

[19, 65, 23, 90]
```

# Task - Combine lists into a dict

You are given two lists. One with color names (`['red', 'green', 'blue']`) and the other one with their RGB hex value (`['#FF0000','#00FF00', '#0000FF']`). Create a combined dict `colors` from those two lists so that for example printing `colors['green']` shows `#008000` on the screen.

## Input:

```
color_names = ['red', 'green', 'blue']
color_hex = ['#FF0000','#00FF00', '#0000FF']
```

## Output:

```
{
  'blue': '#0000FF', 
  'green': '#00FF00', 
  'red': '#FF0000'
}
```

# Task - Highscore

You have a list of participants as strings. This list holds title-cased names. Alongside there is a dictionary with scores, using the same names as keys with a integer as their value.

Implement a method `get_score` that takes a name as an argument, verifies it is in the list of participants and then prints the name with the score.

If the participant can't be found print a message telling that.

## Input:

```
participants = ['Brian', 'Britney', 'Ben']
scores = {
  'brian': 25,
  'britney': 80,
  'ben': 50
}

get_score('Paul')
get_score('Britney')
```

## Output:

```
Paul did not participate
Britney scored 80 points
```


# Task - Count characters

Implement a method called `count_characters`. It should accept any string and count how often each letter occurs in it.

## Input:

```
'Elephant'
```

## Output:

```
{'a': 1, 'e': 2, 'h': 1, 'l': 1, 'n': 1, 'p': 1, 't': 1}
```
