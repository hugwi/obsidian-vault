
tech id: identifies the client anonymization 
each browser will have a different ID 

RTBF might still visit the website. Thus we need to delete the token. 

Don't know if we should use the dcid and personalization id. 

Would prefer having the personalization id since it's user. We don't know if we have the personalization id. 

Risk?
- Might need to 
Referential integrity? 
- Personalization ID is better, since device collect it already. With DCID they need to join to other datasets. 

### Dependencies
- Mobile app need to provide it. 
