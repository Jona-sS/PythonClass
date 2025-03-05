# Beispielhaftes Programm zur Bearbeitung einer Liste mit join und split
# Ursprüngliche Liste
original_list = ['Apfel', 'Banane', 'Kirsche', 'Dattel']

# Liste in einen String umwandeln, getrennt durch Kommas
joined_string = ', '.join(original_list)
print(f"Verbundener String: {joined_string}")

# String wieder in eine Liste umwandeln
split_list = joined_string.split(', ')
print(f"Geteilte Liste: {split_list}")