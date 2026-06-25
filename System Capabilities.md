---
categories:
  - "[[Areas]]"
domain: clients
created: 2026-06-23
---

## Commission 

XML format that more an more insurers support, but some need csv files


How commission is received  use commission type, product type. Can also reduce the money paid out if they paid out too much. 

Salesforce - need to build something that can translate something. Can build it in Salesforce but have limitations    
Account, technical ledger. Financial transaction match it to a cost center. In terms in how it's kept against the books. 
Each transaction for example commisision is one transaction. For general ledger it's 2. Bookkeeping rules need to account like a income that is realised. Reduce the future revenue? Match to specific account in general ledger and it keeps all the calculations. 

There is nothing in salesforce for the ingestion. 
**It passes it in another system?** 

A lot of manual correction for commission, it's an unbelievable  amount of corrections. 
Currently have it in netsuite? or moving to netsuite? 
MMVP going live 1 april, but they're not first out

## costandcenter
discussion for a partner company to take over it. SF would have something similar it something that 

Requried by law to inform where we get information from.
Not advisor in Salesforce 
Wealth management is really hard to do
L&P, WM 


## insclear-importer
add a percent before we pay premium
premium utrymme, 4.5% up to certain iincome basbelopp and then you can have 2% 



---
# Kunddefinition – Liv & Pension 

1). För att **definieras som aktuell kund** ska individen träffas av minst ett av nedanstående kriterier: 

- Det finns en giltig förmedlingsfullmakt utställd av individen 
- Det genereras intäkter på individen (inklusive Gruppförsäkring eller tjänster via MMVP) 
- Det finns aktiva försäkringar med pågående premieinbetalning och där Max Matthiessen har förmedlingsfullmakt antingen på ägaren av försäkringen (företag) eller individen 
- Kunden har giltigt individavtal gällande MRP (senare även MFR). Detta styrs av aktuella taggningar i försäkringslistan   
     

2.) Utöver detta ska tidigare kunder och prospekt **finnas tillgänglig för uppföljning och fortsatt bearbetning,** om de träffas av minst ett av följande kriterier:   
 

- Det har gått mindre än 36 månader sedan senaste rådgivningstillfället 
- Det har gått mindre än 36 månader sedan aktiv tjänstepension lades i fribrev inom Max Storkund eller Maxplan PC 
- En informationsfullmakt har registrerats under de senaste tolv månaderna 
- Individen har registrerats i systemet för mindre än tolv månader sedan    
     

3.) Sista kategorin gäller tidigare kunder och prospekt där **historik och dokumentation arkiveras, men som** _**inte**_ **får bearbetas** och där få medarbetare hos Max Matthiessen ska ha möjlighet att ta del av informationen: 

- Det har gått mer än 36 månader, men mindre än 132 månader sedan senaste rådgivningstillfället upprättades 
- Det har gått mindre än 36 månader sedan någon av följande åtgärder genomfördes utan att kunden träffas av någon av definitionerna i kategori ett eller två:   
       
    - Försäkringstransaktioner har genomförts   
    - Ny lön har registrerats   
    - Fakturor har upprättats   
    - Dokument har lästs in   
    - Individen har registrerats i tjänstegrupp   
    - Korrespondens har upprättats 

Individer som inte uppfyller rekvisiten för att inkluderas i någon av kategorierna ovan ska raderas.


Försökte göra pensionssimuleringar själva innan man köpte capitex
Capitex gör pensionssimulering 
Bygger på Lindas försäkringsmodell. Finns arv i hur man mappar den försäkringsmodell till capitex. 

## Capitex-benefit-service
mappar om till den modell capitex behöver


![[Pasted image 20260115103841.png]]

## DKI 
Customer suvey, väldigt statiska men har 0-5 


## Heartbeat Hj 
Sträcker sig över heartbeat RS. Länken mellan heartbeat och RS. Allting som görs efter ett möte. Vissa grejor skickas av workflow. Den skapar ärende i Maxview ärenden. 
Den skapar ärende eller gör arbetet själv . Gör bara individ val. Alla råd som leder till en uppgift som behöver göras av en masking eller person. 

## Insclear importering

arvodering. Måste göra återbetalningar. Bokföra arvodering och transaktioner 

## Communication
Vad ska gå via email? 
Kanske bara ska skicka ut att de ska kolla i avanza. 
Support funktion 
Ska vi skicka fysiska brev eller skicka via Kivra 
Vi ska kunna ha tracability att vi skickar ut varningar som de kan agera på tex löneväxling. 

### Notifier 
office 365 


## Trio 
Hanterar direkt frågor 
Se hela min pension. 
Alla kunder har gått ut direkt frågor så man kan få aktuell MIS data. Få senast information från försäkringsbolagen

## XPH ?? 


## Info quality 
personnummer byte och purge 
Ska inte ha personnummer. 

## Integration med andra system som Spar
Koppla ihop och säga att det är samma individ


## PML översikt
![[Pasted image 20260115112440.png]]