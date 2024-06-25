#!/usr/bin/env python
# coding: utf-8

# In[94]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd  # Fehlender Import für pandas

# Daten laden
file_path = r"C:\Users\yasse\Downloads\ks-projects-201801.csv"  # Korrekter Pfad mit Raw String
kickstarter_data = pd.read_csv(file_path)

# Berechne Erfolg als Wahrheitswert (True/False)
kickstarter_data["successful"] = kickstarter_data["state"] == "successful"

# Gruppiere nach Hauptkategorie und berechne durchschnittliche Erfolgsrate, umgewandelt in Prozentsätze
kategorie = kickstarter.groupby("main_category")["erfolg"].mean()
sortiert = kategorie.sort_values(ascending=False) * 100

print(sortiert)

# Erstelle ein Balkendiagramm
plt.figure(figsize=(14, 8))  # Größe des Diagramms festlegen
plt.bar(sortiert.index, sortiert.values)  # Balkendiagramm erstellen-data
plt.xticks(rotation=45, ha='right')  # X-Achsen-Beschriftungen drehen für bessere Lesbarkeit
plt.title('Erfolgsraten von Kickstarter-Projekten nach Hauptkategorie')  # Titel hinzufügen
plt.xlabel('Hauptkategorie')  # X-Achsen-Beschriftung
plt.ylabel('Erfolgsrate (%)')  # Y-Achsen-Beschriftung
plt.show()  # Diagramm anzeigen


# In[19]:


# Filtern auf Film & Video Projekte
film_projects = kickstarter_data[kickstarter_data['main_category'] == 'Film & Video']

# Anzahl der Filmprojekte pro Kategorie aggregieren
projects_per_category = film_projects.groupby('category').size()

# Kreisdiagramm zur Visualisierung der Verteilung der Filmprojekte nach Kategorien
plt.figure(figsize=(10, 8))
projects_per_category.plot(kind='pie', autopct='%1.1f%%')
plt.title('Verteilung der Film & Video Projekte nach Kategorien')
plt.ylabel('')  # Entfernt die y-Achsenbeschriftung für ein saubereres Diagramm
plt.show()


# In[96]:


# Konvertieren des 'launched'-Strings in ein Datumsformat und Extrahieren des Jahres
kickstarter_data['year'] = pd.to_datetime(kickstarter_data['launched']).dt.year

# Filtern auf Film & Video Projekte
film_projects = kickstarter_data[kickstarter_data['main_category'] == 'Film & Video']

# Gruppieren der Daten nach Jahr und 'state'
grouped_data = film_projects.groupby(['year', 'state']).size().unstack(fill_value=0)

# Berechnen der Erfolgsrate (Anteil der erfolgreichen Projekte) pro Jahr
grouped_data['success_rate'] = grouped_data['successful'] / (grouped_data['successful'] + grouped_data['failed'])
print(grouped_data['success_rate'])
# Erstellen eines Liniendiagramms zur Visualisierung der Erfolgsraten von Filmprojekten im Zeitverlauf
plt.figure(figsize=(10, 6))
grouped_data['success_rate'].plot(kind='line', marker='o')
plt.title('Erfolgsraten von Filmprojekten auf Kickstarter im Zeitverlauf')
plt.xlabel('Jahr')
plt.ylabel('Erfolgsrate')
plt.grid(True)
plt.xticks(grouped_data.index, rotation=45)
plt.tight_layout()
plt.show()


# In[21]:


# Gruppierung der Daten nach Land und Berechnung der Erfolgsrate
country_success_rate = kickstarter_data.groupby('country')['successful'].mean()

# Visualisierung der Erfolgsrate nach Land mit einem einfachen Balkendiagramm
country_success_rate.sort_values(ascending=False).plot(kind='bar', figsize=(14, 8))
plt.title('Erfolgsrate nach Land')
plt.xlabel('Land')
plt.ylabel('Erfolgsrate (%)')
plt.xticks(rotation=45)  # Dreht die Beschriftungen der Länder für bessere Lesbarkeit
plt.show()


# In[36]:


# Vereinfachung des Codes für den Vergleich der Erfolgsraten nach Filmkategorien

# Berechnung der Erfolgsrate für jede Kategorie
success_rate = film_projects.groupby('category')['state'].apply(lambda x: (x == 'successful').mean())

# Sortierung der Erfolgsrate für eine bessere Visualisierung
success_rate_sorted = success_rate.sort_values()
#Erstellung eines Balkendiagramms
plt.figure(figsize=(10, 8))
success_rate_sorted.plot(kind='barh', color='skyblue')
plt.title('Erfolgsraten nach Filmkategorien auf Kickstarter')
plt.xlabel('Erfolgsrate')
plt.ylabel('Filmkategorie')
plt.show()


# In[97]:


# Berechnung der Quartile für das Finanzierungsziel
quartile = kickstarter_data['goal'].quantile([0.25, 0.5, 0.75])
niedriges_ziel = quartile[0.25]
hohes_ziel = quartile[0.75]

# Funktion, um das Finanzierungsziel in Kategorien einzuteilen
def ziel_kategorisieren(ziel):
    if ziel <= niedriges_ziel:
        return 'Niedrig'
    elif ziel <= hohes_ziel:
        return 'Mittel'
    else:
        return 'Hoch'
    
 
# Kategorisierung der Finanzierungsziele anwenden
kickstarter_data['ziel_kategorie'] = kickstarter_data['goal'].apply(ziel_kategorisieren)

# Erfolgsrate für jede Zielkategorie berechnen
erfolgsrate_nach_ziel = kickstarter_data.groupby('ziel_kategorie')['successful'].mean() * 100  # In Prozent
print(erfolgsrate_nach_ziel)
# Ein Balkendiagramm zur Visualisierung der Erfolgsrate nach Zielkategorie
erfolgsrate_nach_ziel.sort_values().plot(kind='bar', color='skyblue')
plt.title('Erfolgsrate nach Finanzierungsziel')
plt.xlabel('Zielkategorie')
plt.ylabel('Erfolgsrate (%)')
plt.xticks(rotation=0)  # Keine Drehung der Beschriftungen
plt.show()


# In[103]:


# Berechnung der Erfolgsraten für jede Kategorie innerhalb der Hauptkategorie "Film & Video"
film_projects = kickstarter_data[kickstarter_data['main_category'] == 'Film & Video']

# Filtern nach Science-Fiction innerhalb der Filmprojekte
# Achte darauf, dass deine Daten eine 'category' Spalte haben, die für 'subcategory' steht
sci_fi_film_projects = film_projects[film_projects['category'] == 'Science Fiction'].copy()  # Verwendung von .copy() zur Vermeidung von SettingWithCopyWarning

# Konvertieren der 'launched' Spalte in das datetime Format und Extrahieren des Jahres
sci_fi_film_projects['launch_year'] = pd.to_datetime(sci_fi_film_projects['launched']).dt.year

# Zählen, wie viele Science-Fiction-Filmprojekte es pro Jahr gibt
sci_fi_projects_per_year = sci_fi_film_projects['launch_year'].value_counts().sort_index()

print(sci_fi_projects_per_year)
# Erstellen eines Liniendiagramms, um die Anzahl der Projekte pro Jahr zu zeigen
plt.figure(figsize=(10, 5))
plt.plot(sci_fi_projects_per_year.index, sci_fi_projects_per_year.values, marker='o', linestyle='-', color='blue')
plt.title('Science-Fiction-Filmprojekte auf Kickstarter pro Jahr')
plt.xlabel('Jahr')
plt.ylabel('Anzahl der Projekte')
plt.grid(True)
plt.xticks(rotation=45)  # Dreht die x-Achsen-Beschriftungen, damit sie besser lesbar sind
plt.show()


# In[102]:


# Erfolgsrate berechnen
success_rate = sci_fi_projects.groupby('state').size() / len(sci_fi_projects) * 100
#print(success_rate)
# Erfolgsrate von Science-Fiction-Filmprojekten im Vergleich zu anderen Filmkategorien
plt.figure(figsize=(10, 6))
success_rate.plot(kind='bar')
plt.title('Erfolgsraten von Science-Fiction-Filmprojekten auf Kickstarter')
plt.xlabel('Zustand')
plt.ylabel('Prozentsatz')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()


# In[14]:


# Filtern der erfolgreichen Projekte
successful_projects = film_projects[film_projects['state'] == 'successful']

# Gruppieren der erfolgreichen Projekte nach Kategorie und Zählen der Einträge
successful_counts = successful_projects.groupby('category').size()

# Gruppieren aller Projekte nach Kategorie und Zählen der Einträge
total_counts = film_projects.groupby('category').size()

# Berechnung der Erfolgsrate für jede Kategorie
success_rate = successful_counts / total_counts

# Sortierung der Erfolgsrate für eine bessere Visualisierung
success_rate_sorted = success_rate.sort_values()

# Erstellung eines Balkendiagramms
plt.figure(figsize=(10, 8))
success_rate_sorted.plot(kind='barh', color='skyblue')
plt.title('Erfolgsraten nach Filmkategorien auf Kickstarter')
plt.xlabel('Erfolgsrate')
plt.ylabel('Filmkategorie')
plt.show()


# In[15]:


# Vereinfachter Code zum Vergleich der durchschnittlich angefragten vs. erreichten Beträge bei Filmprojekten

# Filtern auf Film & Video Projekte
film_projects = kickstarter_data[kickstarter_data['main_category'] == 'Film & Video']

# Berechnung der durchschnittlich angefragten und erreichten Beträge
average_goal = film_projects['goal'].mean()
average_pledged = film_projects['pledged'].mean()

# Erstellung eines Balkendiagramms für den Vergleich
plt.figure(figsize=(8, 6))
plt.bar(['Durchschnittliches Ziel', 'Durchschnittlich zugesagt'], [average_goal, average_pledged], color=['blue', 'green'])
plt.title('Vergleich der durchschnittlichen angefragten vs. erreichten Beträge bei Filmprojekten')
plt.ylabel('Betrag in USD')
plt.show()


# In[98]:


# Filtern nach erfolgreichen Science-Fiction-Filmprojekten in der Hauptkategorie "Film & Video"
successful_sci_fi_projects = kickstarter_data[(kickstarter_data['main_category'] == 'Film & Video') & 
                                               (kickstarter_data['category'] == 'Science Fiction') & 
                                               (kickstarter_data['state'] == 'successful')]

# Aggregation der durchschnittlichen Anzahl von Unterstützern für diese Projekte nach Ländern
supporters_by_country = successful_sci_fi_projects.groupby('country')['backers'].mean().reset_index()
print(supporters_by_country)
# Visualisierung der durchschnittlichen Anzahl der Unterstützern pro Land in einem Balkendiagramm
plt.figure(figsize=(12, 8))  # Größe des Diagramms festlegen
plt.bar(supporters_by_country['country'], supporters_by_country['backers'], color='teal')  # Balkendiagramm erstellen
plt.title('Durchschnittliche Anzahl von Unterstützern für erfolgreiche Sci-Fi-Filmprojekte nach Land')  # Titel des Diagramms
plt.xlabel('Land')  # Beschriftung der x-Achse
plt.ylabel('Durchschnittliche Anzahl von Unterstützern')  # Beschriftung der y-Achse
plt.xticks(rotation=45)  # Ländernamen drehen, damit sie lesbar sind
plt.grid(axis='y', linestyle='--')  # Gitterlinien für die y-Achse hinzufügen
plt.show()  # Diagramm anzeigen


# In[17]:


# Filtern auf Film & Video Projekte
film_projects = kickstarter_data[kickstarter_data['main_category'] == 'Film & Video']

# Aggregation der Anzahl der Filmprojekte nach Land
projects_per_country = film_projects.groupby('country').size()

# Erstellung eines Balkendiagramms zur Visualisierung der Anzahl der Projekte pro Land
plt.figure(figsize=(12, 8))
projects_per_country.sort_values(ascending=False).plot(kind='bar', color='lightblue', edgecolor='black')
plt.title('Anzahl der Filmprojekte nach Ländern auf Kickstarter')
plt.xlabel('Land')
plt.ylabel('Anzahl der Projekte')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[100]:


# Berechnung der durchschnittlichen Finanzierungsbeträge und Zielsummen für erfolgreiche Science-Fiction-Filmprojekte
avg_funding_goal = successful_sci_fi_projects[['goal', 'pledged']].mean()
 #Visualisierung der durchschnittlichen Finanzierungsbeträge und Zielsummen
print(avg_funding_goal)
plt.figure(figsize=(10, 6))
avg_funding_goal.plot(kind='bar', color=['skyblue', 'lightgreen'])
plt.title('Durchschnittliche Finanzierungsbeträge und Zielsummen für erfolgreiche Sci-Fi-Filmprojekte')
plt.xlabel('Finanzielle Kennzahlen')
plt.ylabel('Betrag in USD')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--')
plt.show()


# In[40]:


# Vereinfachung des Codes für die Erstellung des Balkendiagramms zur Anzahl der Filmprojekte nach Ländern

# Filtern auf Film & Video Projekte
film_projects = kickstarter_data[kickstarter_data['main_category'] == 'Film & Video']

# Aggregation der Anzahl der Filmprojekte nach Land
projects_per_country = film_projects.groupby('country').size().sort_values(ascending=False)

 #Erstellung eines Balkendiagramms zur Visualisierung
plt.figure(figsize=(10, 6))
projects_per_country.plot(kind='bar', color='lightblue')
plt.title('Anzahl der Filmprojekte nach Ländern auf Kickstarter')
plt.xlabel('Land')
plt.ylabel('Anzahl der Projekte')
plt.xticks(rotation=45)
plt.show()



# In[22]:


# Filterung nicht erfolgreicher Science-Fiction-Filmprojekte
unsuccessful_sci_fi_projects = sci_fi_film_projects[sci_fi_film_projects['state'] != 'successful']

# Berechnung der durchschnittlichen Finanzierungsziele für erfolgreiche und nicht erfolgreiche Projekte
avg_goal_successful = successful_sci_fi_projects['goal'].mean()
avg_goal_unsuccessful = unsuccessful_sci_fi_projects['goal'].mean()

# Erstellung eines DataFrame für die Visualisierung
avg_goals_comparison = pd.DataFrame({'Status': ['Erfolgreich', 'Nicht erfolgreich'],
                                     'Durchschnittliches Finanzierungsziel': [avg_goal_successful, avg_goal_unsuccessful]})

# Visualisierung der durchschnittlichen Finanzierungsziele
plt.figure(figsize=(10, 6))
plt.bar(avg_goals_comparison['Status'], avg_goals_comparison['Durchschnittliches Finanzierungsziel'], color=['green', 'red'])
plt.title('Vergleich der Finanzierungsziele zwischen erfolgreichen und nicht erfolgreichen Sci-Fi-Filmprojekten')
plt.xlabel('Status des Projekts')
plt.ylabel('Durchschnittliches Finanzierungsziel (USD)')
plt.grid(axis='y', linestyle='--')
plt.show()


# In[22]:





# In[23]:


# Konvertierung der 'launched' Spalte in datetime Format und Extraktion des Monats
sci_fi_film_projects['month'] = pd.to_datetime(sci_fi_film_projects['launched']).dt.month

# Aggregation der Anzahl der Projekte und der durchschnittlichen Unterstützerzahlen pro Monat
projects_per_month = sci_fi_film_projects.groupby('month').size()
supporters_per_month = sci_fi_film_projects.groupby('month')['backers'].mean()

# Erstellung von Liniendiagrammen zur Darstellung der saisonalen Muster
fig, ax1 = plt.subplots(figsize=(12, 6))

color = 'tab:blue'
ax1.set_xlabel('Monat')
ax1.set_ylabel('Anzahl der Projekte', color=color)
ax1.plot(projects_per_month.index, projects_per_month.values, color=color, label='Anzahl der Projekte', marker='o')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # Erstellung einer zweiten y-Achse
color = 'tab:red'
ax2.set_ylabel('Durchschnittliche Anzahl von Unterstützern', color=color)
ax2.plot(supporters_per_month.index, supporters_per_month.values, color=color, label='Durchschnittliche Anzahl von Unterstützern', marker='x')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # Anpassung des Layouts
plt.title('Projektanzahl und durchschnittliche Unterstützerzahlen nach Monaten')
plt.show()


# In[24]:


# Annahmen für die geplante Kampagne von "Neon Genesis"
neon_genesis_data = {
    'Kategorie': ['Zielsumme', 'Dauer (Tage)', 'Anzahl der Unterstützer'],
    'Neon Genesis': [50000, 60, 300]  # Beispielwerte für Zielsumme, Dauer und Unterstützer
}

# Durchschnittswerte erfolgreicher Science-Fiction-Filmprojekte
avg_successful_sci_fi_data = {
    'Zielsumme': successful_sci_fi_projects['goal'].mean(),
    'Dauer (Tage)': (pd.to_datetime(successful_sci_fi_projects['deadline']) - pd.to_datetime(successful_sci_fi_projects['launched'])).dt.days.mean(),
    'Anzahl der Unterstützer': successful_sci_fi_projects['backers'].mean()
}

# Erstellung eines DataFrame für die Visualisierung
comparison_df = pd.DataFrame(neon_genesis_data).set_index('Kategorie')
comparison_df['Durchschnitt erfolgreiche Sci-Fi-Filme'] = avg_successful_sci_fi_data.values()

# Visualisierung des Vergleichs
comparison_df.plot(kind='bar', figsize=(12, 6))
plt.title('Vergleich der geplanten Kampagne von "Neon Genesis" mit durchschnittlichen Werten erfolgreicher Sci-Fi-Filmprojekte')
plt.ylabel('Werte')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--')
plt.show()


# In[50]:


# Filtern auf Film & Video Projekte
film_projects = kickstarter_data[kickstarter_data['main_category'] == 'Film & Video']

# Anzahl der Filmprojekte pro Kategorie aggregieren
projects_per_category = film_projects.groupby('category').size()

# Kreisdiagramm zur Visualisierung der Verteilung der Filmprojekte nach Kategorien
plt.figure(figsize=(10, 8))
projects_per_category.plot(kind='pie', autopct='%1.1f%%')
plt.title('Verteilung der Film & Video Projekte nach Kategorien')
plt.ylabel('')  # Entfernt die y-Achsenbeschriftung für ein saubereres Diagramm
plt.show()


# In[55]:


kickstarter_data.head(30)


# In[86]:


# Filtern der Daten für erfolgreiche Science-Fiction-Filme
sci_fi_success = kickstarter_data[(kickstarter_data['main_category'] == 'Film & Video') & 
                      (kickstarter_data['category'] == 'Science Fiction') & 
                      (kickstarter_data['state'] == 'successful')]

# Zählen, wie viele erfolgreiche Science-Fiction-Filme es pro Land gibt
sci_fi_success_by_country = sci_fi_success['country'].value_counts()

# Berechnung des Prozentsatzes
sci_fi_success_percentage = (sci_fi_success_by_country / sci_fi_success_by_country.sum()) * 100

# Erstellung eines Balkendiagramms für die erfolgreichen Science-Fiction-Filme nach Land in Prozent
sci_fi_success_percentage.plot(kind='bar', figsize=(14, 8), color='lightgreen')
plt.title('Erfolgreiche Science-Fiction-Filme nach Land in Prozent')
plt.xlabel('Land')
plt.ylabel('Prozentsatz der erfolgreichen Filme (%)')
plt.xticks(rotation=45)
plt.show()


# In[93]:


# Zählen der gesamten Science-Fiction-Filme pro Land
total_sci_fi_projects_by_country = kickstarter_data[(kickstarter_data['main_category'] == 'Film & Video') & 
                                        (kickstarter_data['category'] == 'Science Fiction')]['country'].value_counts()

# Berechnen der Erfolgsrate in Prozent
sci_fi_success_rate = (sci_fi_success_by_country / total_sci_fi_projects_by_country) * 100

# Sortieren der Daten, um sicherzustellen, dass die Länder mit der höchsten Erfolgsrate oben stehen
sci_fi_success_rate_sorted = sci_fi_success_rate.sort_values(ascending=False)
print(sci_fi_success_rate_sorted)
# Plot
sci_fi_success_rate_sorted.plot(kind='bar', figsize=(14, 8), color='coral')
plt.title('Erfolgsrate der Science-Fiction-Filme nach Land')
plt.xlabel('Land')
plt.ylabel('Erfolgsrate (%)')
plt.xticks(rotation=45)
plt.show()


# In[92]:


# Filtern der Daten für erfolgreiche Science-Fiction-Filme
sci_fi_success = kickstarter_data[(kickstarter_data['main_category'] == 'Film & Video') & 
                      (kickstarter_data['category'] == 'Science Fiction') & 
                      (kickstarter_data['state'] == 'successful')]

# Zählen, wie viele erfolgreiche Science-Fiction-Filme es pro Land gibt
sci_fi_success_by_country = sci_fi_success['country'].value_counts()

# Berechnung des Prozentsatzes-
sci_fi_success_percentage = (sci_fi_success_by_country / sci_fi_success_by_country.sum()) * 100
print(sci_fi_success_percentage)
# Erstellung eines Balkendiagramms für die erfolgreichen Science-Fiction-Filme nach Land in Prozent


sci_fi_success_rate_sorted.plot(kind='bar', figsize=(14, 8), color='coral')
plt.title('Erfolgsrate der Science-Fiction-Filme nach Land')
plt.xlabel('Land')
plt.ylabel('Erfolgsrate (%)')
plt.xticks(rotation=45)
plt.show()




# In[91]:


# Filtern der Daten für erfolgreiche Science-Fiction-Filme
sci_fi_success = kickstarter_data[(kickstarter_data['main_category'] == 'Film & Video') & 
                      (kickstarter_data['category'] == 'Science Fiction') & 
                      (kickstarter_data['state'] == 'successful')]

# Zählen, wie viele erfolgreiche Science-Fiction-Filme es pro Land gibt
sci_fi_success_by_country = sci_fi_success['country'].value_counts()

# Berechnung des Prozentsatzes
sci_fi_success_percentage = (sci_fi_success_by_country / sci_fi_success_by_country.sum())


# In[104]:


sci_fi_projects_ks = kickstarter_data[(kickstarter_data['main_category'] == 'Film & Video') & (kickstarter_data['category'] == 'Science Fiction')]

# Umwandeln des 'launched' Strings in ein datetime Objekt für die gefilterten Projekte
sci_fi_projects_ks['launched'] = pd.to_datetime(sci_fi_projects_ks['launched'])

# Hinzufügen einer neuen Spalte für das Startjahr der gefilterten Projekte
sci_fi_projects_ks['launch_year'] = sci_fi_projects_ks['launched'].dt.year

# Berechnung der Erfolgsrate pro Jahr für die gefilterten Projekte
success_rate_per_year_ks = sci_fi_projects_ks.groupby('launch_year')['state'].apply(lambda x: (x == 'successful').mean() * 100)

# Visualisierung der Erfolgsrate von Science-Fiction-Filmprojekten auf Kickstarter nach Jahr
plt.figure(figsize=(10, 6))
success_rate_per_year_ks.plot(kind='bar', color='skyblue')
plt.title('Erfolgsrate von Science-Fiction-Filmprojekten auf Kickstarter nach Jahr')
plt.xlabel('Jahr')
plt.ylabel('Erfolgsrate (%)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', linewidth=0.7)
plt.show()


# In[ ]:




