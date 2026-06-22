
# Workshop 6 Dec


## Transportköpare

### Contract based profiles 

Bättre insikt i kundererna och relation till transporköpare
Bygg customization till platformen 
One stop shhop entiteet subcontractor:
- ladda upp kontrakt
- Certifikat för elcertifiering tex Transportör laddar upp det

### Jämförelse av transportörer
Kan jämföra de man har. Kan vi tillhandahålla market place some pricerunner men för transportörer. 
Vart ligger transportören idag i utsläpp. 
Vissa transportörer vill inte vara där. 

### Roller
Olika typer av transporköpare, olika widget kan vara intressanta för olika personer 

### Transportköpare KPI/mål 
Samla deras mål och se hur de förhåller sig till det. 

### Death to excel 
Svåra att jobba med. Bättre användarupplevelse. 

## Risker Marknadsplats
+ Finns push back
+ Mindre transportör har inte samma investeringsmöjlighet. 
- We can opt in

Trying to slow down ...



## Data 

What do we need to enable low latency products? 

![[Pasted image 20241209154459.png]]



### Nils och Hugo (st) - co2 emission 

Svårt att ha bra data kvalité för data 
Jobbade med standardavvikelser 
Katogoriserar data 
3e part system för att få emission factors. 

Emission faktor kan till exempel vara att beräkna utsläpp per krona för transport. 

Credit och debit är att hålla koll på varifrån de kommer. 

Folk har olika åsikter kring hur mycket 1 kg bränsle släpper ut. 

Hämta bensin? Produktion av bensin? 




















































# Security 

https://netlight.slack.com/archives/C04G2CJP6/p1718096164760419
My client is looking at **different options for isolating access to processing of certain restricted** **data** **domains in AWS**. We have an AWS+Snowflake based data platform with some shared tooling, such as Airflow, custom EL(T) framework, CICD framework, and some other utilities. Generally, data lands into AWS S3, it is minimally processed (Lambda/Glue/EMR), and then loaded to Snowflake for further transformations. For each restricted domain there is a specific team that develops the data processing and only this team should have access to the data and processing.![:one:](https://a.slack-edge.com/production-standard-emoji-assets/14.0/apple-medium/0031-fe0f-20e3@2x.png) Until now, everything has been deployed to the same AWS accounts (dev/preprod/prod), but we have had issues protecting HR data from unauthorised/inadvertent access. Previously, the data was encrypted with CMKs but the maintenance overhead of the setup was significant, and it was simplified to just use bucket policies. The problem is, the processing infrastructure is not protected, and the security issues are obvious. Also, currently our CICD framework doesn't support this approach and some of the infra related to HR data needs to be manually deployed.![:two:](https://a.slack-edge.com/production-standard-emoji-assets/14.0/apple-medium/0032-fe0f-20e3@2x.png) Now the CSRD related reporting is being worked on. Some of the data used there are so sensitive that the same risks that have been taken with HR data cannot be accepted, and the infrastructure for processing the very sensitive CSRD-related data will be set up from scratch into separate AWS accounts. The challenge with this approach is that none of the tooling in the data-plaform AWS accounts cannot be used, resulting into custom/duplicate solutions.![:arrow_right:](https://a.slack-edge.com/production-standard-emoji-assets/14.0/apple-medium/27a1-fe0f@2x.png) We started to investigate **multi-account support for** **data** **platform** – basically, if refactoring the shared tooling/approaches used in the data platform AWS accounts could allow us to support multiple separate AWS accounts, so that the restricted data could be easily isolated and yet there would be no need for custom solutions / duplicate work.**Has anyone faced similar business requirements**, meaning the need to securely isolate data processing in a centralised data platform in AWS? **What has been your approach?** Isolating on account level, using encryption/CMKs, or something else?




Vikotria - Co founder & sustainability lead
Viktor - developer 
Oscar - Venture builder
Samuel - project 
Viet-Anh - Co-venture lead
Mikael - CTO
Melina Kamyab - front end engineer, snart mamma ledig 
