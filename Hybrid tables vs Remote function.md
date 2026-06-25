---
categories:
  - "[[Resources]]"
domain: engineering
created: 2026-06-23
---

# Hybrid tables 

## Pros 
- Everything reside in snowflake and the replication is perfect in sync 
- A table that is a perfect replicate will be in Snowflake 
- Less moving parts 
- Har tillräckligt latency 
- 
## Cons
- Data is shared with 


# Remote function

## Pros 
- Everything is # contained 
Cons 
- Flera punkter som går fel
- Inte är i synk
+ Undviker discrepencies
+ Mer logic på båda sidorna
+ Laga data på flera ställen



--- 

API som vi ska hämta
+ Vi vet inte om en användare ändrar något i ett fordon -> updated at
+ En task för att skjuta mot den och uppdatera 
+ Flera


---
Tja! 

Hörde att du snackade lite om hybrid tables och användet av replikering av postgres data via remote functions. 

Pratade lite mer om Preben vad det hade inneburit från våra sida och nackdelarna med att ha det i postgres istället för hybrid tables är

- Flera punkter som kan gå fel
- Undviker potentiella data diskrepensar och data som inte är i synk. 
- Mer komplexitet och logik på båda sidorna: Det behöver ändras I API:et och vi måste sätta upp en task på vår sida som anropar funktionen samt schedulera och underhålla de. 
- Vi lagrar data på flera ställen: Tangerar lite det jag sa ovan att det finns risk för diskrepanser. 
- Var även tal på att vi skulle lägga till en till tabell så kunden kan lägga till default vehicles vilket hade inneburit en till tabell som också ska ha replikering: Varje till tabell och tjänst som vi lägger till måste vi bygga nya replikering för.

Fördelen med Snowflake som jag ser är: 

- Data är lagrat på ett ställe 
- Färre rörliga delar (undivker maintenance och saker som kan gå fel)
- Lätt att byta ut: Det är i princip bara en connection som behöver ändras (vilket vi redan gjort) 
- ⁠Snabbare att implementera i och med att vi bara byter en connection 

Nackdelarna skulle kunna vara: 

- Latency - Detta tror jag dock inte är kritiskt och hybrida tables ska vara snabbare än vanliga tables vilket vi vet tar ish 1 sek
- Security - Jag förtstår verkligen var denna concern kommer från. Jag känner mig inte särskilt oroligt för detta då det dels inte är någon känslig data och dessutom är en typ av sharing som har blivit godkänt "scania wide". Preben nämnde även att de skickar mycket känsligare data mellan instanser. Man kan också sätta upp private links för att göra det säkrare i framtiden. 

Jag förstår även att det kan känns lite som ett "uncharted territory", men jag ser det som en rimlig risk för det vi vinner i tid. Jag ser även alternatived med replikering med remote functions som en bra backup ifall det blir några problem med hybrid tables. 

 Fokuserat lite mer på de konsekvenerar jag ser att ha data i postgres och fördelarna med att ha det i hybrid tables, men skriv gärna ner dina tankar också så kan vi försöka komma till ett beslut idag. 