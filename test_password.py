import unittest

def validate_password(password_input):
    
    try:
        password_length = len(password_input)
    except TypeError:
        return False
    
    if password_length < 10:
        return False
    
    #initialize flags
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    
    for char in password_input:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        
        if has_uppercase and has_lowercase and has_digit:
            break
        
    if has_uppercase and has_lowercase and has_digit:
        return True
    else:
        return False
    

class TestPasswordValidator(unittest.TestCase):
    
    def test_valid_password(self):
        self.assertTrue(validate_password("HelloTom123"))
        
    def test_too_short(self):
        self.assertFalse(validate_password("aB123"))
        
    def test_non_string_input(self):
        self.assertFalse(validate_password(47464))
        
        
unittest.main()


































# import unittest

# def validate_password(password_input) -> bool:
#     """
#     Prüft ein Passwort auf Mindestlänge, Groß-/Kleinbuchstaben und Ziffern.
#     Verwendet Fehlerbehandlung, um nicht-String-Eingaben abzufangen.
#     """
#     # 1. Fehlerbehandlung (Typenprüfung): try-except Block
#     try:
#         # Versuch, string-spezifische Methoden aufzurufen. 
#         # Wenn passwort_eingabe kein String ist, wird hier ein TypeError ausgelöst.
#         password_length = len(password_input)
#     except TypeError:
#         # print(f"FEHLER: Die Eingabe muss ein String sein, es wurde {type(password_input).__name__} übergeben.") # Für Tests auskommentiert
#         return False
    
#     # 2. Kontrollstruktur (Bedingung): Länge prüfen
#     MIN_LENGTH = 10
#     if password_length < MIN_LENGTH:
#         # print(f"Prüfung fehlgeschlagen: Passwort ist zu kurz...") # Für Tests auskommentiert
#         return False
    
#     # Initialisierung der Flags (Datentyp bool)
#     has_uppercase = False
#     has_lowercase = False
#     has_digit = False
    
#     # 3. Kontrollstrukturen (Iteration & Bedingungen): Zeichen prüfen
#     for char in password_input:
#         if char.isupper():
#             has_uppercase = True
#         elif char.islower():
#             has_lowercase = True
#         elif char.isdigit():
#             has_digit = True
            
#         if has_uppercase and has_lowercase and has_digit:
#             break
            
#     # 4. Kontrollstrukturen (Bedingungen): Finales Ergebnis prüfen
#     if has_uppercase and has_lowercase and has_digit:
#         # print("Prüfung erfolgreich: Das Passwort erfüllt alle Stärke-Anforderungen.") # Für Tests auskommentiert
#         return True
#     else:
#         # print("Prüfung fehlgeschlagen: Mindestens ein Kriterium fehlt.") # Für Tests auskommentiert
#         return False

# # -----------------------------------------------------------------


# class TestPasswordValidator(unittest.TestCase):
#     """
#     Testklasse für die Funktion validate_password.
#     """

#     ## 1. Tests für gültige Passwörter (sollten True zurückgeben)
#     def test_valid_password(self):
#         # Alle Kriterien erfüllt
#         self.assertTrue(validate_password("GoodPassword123"))

#     def test_valid_password_min_length(self):
#         # Exakt Mindestlänge, alle Kriterien erfüllt
#         self.assertTrue(validate_password("aB12345678"))

#     ## 2. Tests für fehlgeschlagene Kriterien (sollten False zurückgeben)
#     def test_too_short(self):
#         # Zu kurz (unter 10 Zeichen)
#         self.assertFalse(validate_password("aB12345"))

#     def test_missing_uppercase(self):
#         # Keine Großbuchstaben
#         self.assertFalse(validate_password("notstrong123"))

#     def test_missing_lowercase(self):
#         # Keine Kleinbuchstaben
#         self.assertFalse(validate_password("NOTSTRONG123"))

#     def test_missing_digit(self):
#         # Keine Ziffern
#         self.assertFalse(validate_password("NoDigitsHere"))

#     def test_only_letters_long(self):
#         # Lang genug, aber nur Buchstaben
#         self.assertFalse(validate_password("LongPasswordButNoNumber"))

#     ## 3. Tests für Fehlerbehandlung (sollten False zurückgeben, da kein String)
#     def test_non_string_input_int(self):
#         # Eingabe ist eine Zahl
#         self.assertFalse(validate_password(1234567890))

#     def test_non_string_input_none(self):
#         # Eingabe ist None
#         self.assertFalse(validate_password(None))

#     def test_non_string_input_list(self):
#         # Eingabe ist eine Liste
#         self.assertFalse(validate_password(["a", "B", "1"]))

#     def test_non_string_input_bool(self):
#         # Eingabe ist ein Boolescher Wert
#         self.assertFalse(validate_password(True))


# # Führen Sie die Tests aus, wenn das Skript direkt gestartet wird
# #if __name__ == '__main__':
# unittest.main()