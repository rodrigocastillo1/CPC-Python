dortmund_events_set = {
    ("2026-09-04", "1. Philharmonisches Konzert 'Seelenklänge' (Konzerthaus Dortmund)"),
    ("2026-09-05", "Fine Arts Quartet (Orchesterzentrum NRW)"),
    ("2026-09-12", "Heavysaurus - Kids Rock Tour (Junkyard)"),
    ("2026-09-15", "FATT – Festival of Arts, Tech & Taste (Kokerei Hansa)"),
    ("2026-09-18", "Das Dortmunder Oktoberfest (Revierpark Wischlingen)"),
    ("2026-09-19", "DEW21 Museumsnacht: Marquess Live-Konzert & Musikfeuerwerk (Friedensplatz)"),
    ("2026-09-19", "DEW21 Museumsnacht: 'what is wisdom' Fassaden-Mapping durch storyLab kiU (Dortmunder U)"),
    ("2026-09-19", "DEW21 Museumsnacht: Synthesizer-Workshop von DachDeckende Randgruppe (Dortmunder Kunstverein)"),
    ("2026-09-19", "DEW21 Museumsnacht: Sonderführungen durch die Fußballgeschichte (Deutsches Fußballmuseum)"),
    ("2026-09-19", "DEW21 Museumsnacht: Historische Nachtführungen (Apotheken-Museum & Borusseum)"),
    ("2026-09-20", "Seebühne am Sonntag (Westfalenpark)"),
    ("2026-09-23", "Die Comedy Werkstatt (WeinGrün)"),
    ("2026-09-24", "Open Space // Medienwerkstatt (Dortmunder U)"),
    ("2026-09-26", "Asterix & Obelix: The Immersive Adventure (Phoenix des Lumières)"),
    ("2026-09-29", "BRKN – 'Lösch meine Nummer' Tour (FZW)")
}

def getEventsByDate(date):
    return [e for e in dortmund_events_set if e[0] == date]

def main():
    print("This program will list the events that took place in the date specified.")
    date = "2026-09-19" # Dortmund Museum night!
    print("The events that took place during", date, "were: ")
    for e in getEventsByDate(date):
        print(e[1])

if __name__ == "__main__":
    main()