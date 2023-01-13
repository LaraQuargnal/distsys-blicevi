def f1(predmeti):
    assert isinstance(predmeti, list) and all(isinstance(s, str) for s in predmeti), "U listi moraju biti svi stringovi."
    return {k: v[::-1] for k, v in enumerate(predmeti)}
  
print(f1(["Stol", "Stolica", "Krevet", "Fotelja"]))
