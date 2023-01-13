def f1(predmeti):
    assert isinstance(predmeti, list) and all(isinstance(s, str) for s in predmeti), "Input must be a list of strings."
    return {k: v[::-1] for k, v in enumerate(predmeti)}
  
print(f1(["Stol", "Stolica", "Krevet", "Fotelja"]))
