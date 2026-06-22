
Carolina managing all the advisors at Max. Needs to be advisors community. 
**Get Carolina involved**
Philipp and Olaf 

Change of scope will be covered there and agreed on it 
Architecture forum any architecture decision will be taken
Changes of these objectives we use these governance bodies

Archietctural questions - swedish database
comission defines active customers. No logic in our systems that. That employee dissapear from the MIS files and that's how we deduct

Carolina had a lot of comments on prospecting. Another requirement is that the advisor love it. 

CRM implementation is successful by the people using it. 
Prospecting is used mainly for L&P. 

This is how we capture requirements and scope. If we do requirements changes we use the governance forums to use these decisions. Will get estimated 

If we change scope we need to justify it and prioritize it. Do it within the same budget. 

**Key decision**
- Should the data be sent via the DW
- Customer leaving and joining 
- Update the CRM system (part of the MDM strategy)

DWH doesn't get data from Bonnaya. 
CRM system is not connected. 


Notes from the RS meeting. We extract it but we don't use it. 

Understand a policy of a client it's unstructured. Baseline insurances. Sometimes it's structured and unstructured. 
Unstructured need to converted to structured. **Heartbeat** is trying to solve this. 
Pension policy - it's a written document. contract between customer and insurer. we're giving you this pension and life instuance

Salesforce is the single pane of glass

What information do you want to react to. It's not policy that is important. 
We don't need to structure all the data but what is the rules for the salary exchange. 
A new person starts at a new company. An advisor is not involved in that process but salaray exchange. I'ts not that you get salary exchange. 
Upsell on a client level but on customer level. Upsell and cross sell.  Cross sell is important on client level. 
Recreate the offering for a client to give employees better solution and raising upsell solution. 
Cross sell between P&C and L&P. L&P is 90% of the commission. 

**Want to understand which processes have happened**
Carolina has added some new information. 

Sometimes the product varies between different types of client relationships. 

No more PML and Linda after GCP refactoring. 
Achieving business goals vs architectural solution to come. Replacement for PML and Linda won't arrive for another 12 months. 

Want to swap them out after refactorization is done. 
Salesforce could be a great idea to get value sooner. 

Advisor thinks It looks good until they start using it. Adoption dashboards

Carolina and Filip to get it off the ground. They will give the context. 
Generating commission is advisors target objective 

--- 

### 360 degree view?

Fredrik - See everything that - client level
Additional business opportunities . What values this specific value has.  Not pension policy, which advisor is responsible. No insurance specific. How big is this client. Number of individuals, pension and wealth. Casualties. Olycksfall and healthcare. Lines of business. 

Dont have to chagne system to L&P and P&C  and customer

What type of insruance for L&P and not necessary for the 360 view. 

P&C brokers 360 vieew. How big is this client. Cross and upsell. 

Is it sensitive when it gets down to customer level, but not on company level. 
Is it a maxm company. Are we working with this client. 
Regisrtration number. 
Use SF as source for leads. Accidentally find client that are clients to use. 

--- 
### P&C Requirements
Brokers only use SF, not only to develope new business but also. Encouraging brokers to use the same system. 
Not for prospecting. L&P brokers to see what we're doing. 
Next to sales numbers. 

Growing the business through L&P. Understand the state of the client. 

**Ability to see in Salesforce, per corporate client:** 

	
-**Ability to determine whether a client holds both L&P and P&C products, and where gaps exist for cross-sell opportunities.** 
- Related to identifying new opportunities.

**Ability to see commission generated:  -**
	- **At the corporate client level** 
	- **Across the total client relationship value** 
The value was that much and that inspired to give you numbers. Every broker would like that

 **Integration of P&C platforms (e.g., Bonnaya replacement / Broker Platform) with Salesforce and the Data Warehouse.** 
 - That data is needed. Need to happen within the 6 month. 

---
 **Ability to see all Private Banking clients and customer in Salesforce. ​**
 - Could be the same as L&P but can also be smaller 
 - Business on a client level or within investments in the company. 
    
 **For each PB client, the ability to see: ​**
- **Products held (mutual funds, discretionary mandates, savings products) ​**
- **Other products from outside WM (e.g., L&P or P&C) ​**
- Good enough to see if they have a private saving. Don't need to buy and sell. Do this customer have maxfonder. This customer have maxfonder and a saving at us. Not these 5 founds. 
- L&P needs to see which funds but private banking it's good enough to see the 360 view. Alvi as documentation. Also open accounts and make trades. Executing. Alvi. Could have 3 meeting prospecting. Not the same as L&P. They don't have a system for it. THey use an advisory tool. Get a recommendation and have some offers function. 
- ALBI has an API connection. 
- Customer should be able to buy and sell nad exchange of udns. If they want tot do anything outside the meeting and log into at Maxfonder. 

- GDPR: up to L&P broker. 
- Might need to discuss the access model. Comlicated to have data model. 
- Documentation from ALVI, but accounts and transaction from backoffice. 


**Is this a private banker customer.** 
Salesforce for the 360 view. But people use it in ALVI. 

**L&P needs Maxfonder**

**Should Alwy be used?** 
Started out, 3 months. 
FSC har overlap with ALWY. It has life timeline. 
- We need to 
- We should talk to Olof. 


**Should SF be 360 view**
Du öppnar IPS och öppnar en likvid. Alla flytta om du baa ha en depå med Likvid. We can get it from the backoffice system. 
An old API connection prevents from seeing all information. 

**A lot of the data we need might be in the bacoffice system**

Need maxofonder anyway. Need to log into the Maxfonder, but cannot see it in Maxview. 

**Specialised system for doing the business.** 
Aggregated view across the business lines. 

- Ability to assess the total relationship value across WM and non-WM products, including premiums and commissions. ​



--- 
# L&P Requirements
**Visibility of company-level details via integration with Swedish National Companies database. ​**
Can look up the information. Right official address. 
	
**Ability to see how the Client’s Pension policy is set up. The information is available in MaxView**.
How much pension (tjänstepension), and it's in heartbeat. 

 **Ability to see per employee: ​**
 Need all information, whether in Maxview or not. All that information is in Maxview. What is a sales opportunity? 

**Ability to identify which employees are customers and which are not, and measure penetration rates for products across the employee base. ​**
In some cases, we have employees that is ensured through MaxM, and some people are used in. Also handle salary exchange. Not all employees don't have a salary exchange, but they're prospects. 

**Ability for the advisor to use a tool for premium calculation – today in MaxView ​**
If the advisor is gonna work outside of MaxView. We shouldn't build a new one. Do the calculations on demand. Storing the calculations. The estimated premium and invoiced. 
Will help broker in the discussion if they have this view. 

The people use it in Maxivew. 
The best part is to use advisors use Salesforce. Can do 90% work. Use Maxxview to add information to add infor about Maxview. advisors do that. 

Differerence between advisors and admins are blurry. What processes do we want to have in each system. Advisor processes doesn't need to move to Maxview. 

All other advisors is going through Maxview. Can be fine for them to use it. 

If they do it in SF it should change in Maxview. 

**Ability to collect all data from the section “fact gathering” in the Advisor System (RS) and ability to structure and search in the data to find groups with possible upsell possibilities  ​**
- Some part is putting meet notes. Is that a CRM activity or operational activiy.
- You want to gather information from RS to gather sales opportunities. 
- That type of information is in faktainsamling. 
- Compliance tool. You need to write done things to be compliant. 
- Structured meeting notes. 
<mark style="background: #FF5582A6;">(Ask about how the RS is used for upsell)</mark>

**Cross sell**
Don't have a function for that today.  A senior advisor have this information. 
Want to report on a business opportunity. We want to experiment. 
<mark style="background: #FF5582A6;">(Today Carl is doing that? Which should look at this. )</mark>

**Ability to identify a customer’s current stage in the customer journey at any given point in time, and to use this information to deliver relevant communications via email, SMS, and in-platform messages on the homepage. ​**
Mariusz: Advisor could send up to 200 people at time. If you want to automate it for everyone you can't use the standard SF. 

**To ensure accurate information and communication, the system must link each customer to the structure of their employer’s pension plan. This should include details such as available group insurance offerings, eligibility for salary sacrifice, and applicable thresholds (e.g., minimum salary levels). ​**
<mark style="background: #FF5582A6;">Ask Carl about where there is analyzed currently</mark>

**KYC issue** 
- KYC issue. We need a new KYC system 
- Need additional information. Need integration of a KYC system. 
- KYC model in SF. Trapetz we partly use today. 
- Need to ingest it for a different system. Clients and customer. 
- They have 3 system. 
- Client and customer. 
- Client does in during onboarding. Depend on the risk
---
**Prospect on the client level**
Carolina head of sales new prospects. Have a good understanding of the needs. 
This is what it should be,  but not target. 
Important to include in scope. 
