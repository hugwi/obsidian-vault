
From sensors_v0 is the number of seessions 388906383 but in tm6_v1 it's only 162533951. Haven't check distinct though.  Compute takes 44 sec vs 44 min also which is strange.  Might be because we're filtering on country

https://vorwerkholding-my.sharepoint.com/:f:/r/personal/marcel_hellmann_vorwerk_ch/Documents/02_PROJECTS/04_ANALYTICS/TMSensor2024?e=5%3aaea62d7560464748b06ebaa017685316&sharingv2=true&fromShare=true&at=9
## TODO
Check with Vale and Bene if we have time for sensor analysis. 
- **Compare if it sells more if it was shown or not**
- See if the data 
- prod_sub.status_combine_v1 check if we have this daa. 
- Check raw_usagebox_tm6
- Check sensor error 
- We can set up with sales if we need more information about user behaviour.
- Verify discreption to SENSOR_CONNECTED,  SENSOR_COOKING_CONFIG,  SENSOR_ERROR
- Is portugal getting as good numbers as switzerland. 
- Are some markets more troubled by error
- **WAITING**: Sales number for sensors
- Check if we can use v1 data
# Analysis
- See how any  

# Hypothesis
- Can we see if Switzerland have higher sales and if it's correlated to the amount of demos. 

	Time for query in Athena without select dcid from advisors
![[Pasted image 20240704163833.png]]
Time for query in Athena
![[Pasted image 20240704163504.png]]

There is 3206294912 rows for 
```
prod_data_products.dh_usagebox_tm6.usagebox_tm6_log_v1 s
WHERE s.ts > '2024-06-01'
```

Not satisifed with sales TM sensor. 
Connects to bluetooth or mobile app. Main selling point is cakes. Cake in the oven. 
Success guarantee with recipes.
We can monitor when you put in the oven. 
120-130 euro. 
Not as good as expected. Thermometer is not showed enough it much. 
**Timeline**
Next week the 10th, they have steering meeting 17th. Stefan watch. product line manager for culinary. 
Can we see if Switzerland have higher sales and if it's shown. 
Germany are showing it in the same. 
Waiting for the sales data. per market per month. 24. 

Small thermomix that you can use beside your thermomix. It's also synced to bluetooth. We launched when corona started. They're a bit panicky when it comes to sales. Go through onsite -> online demos. 

**Sales**
- Number of sold units. 
- What's the pricing? 

- Usagebox data 
- Subscription data

Makes it difficult to know what belongs to a demo. Demo in one recipe. 

**Demo recipe**
There's multiple steps. 

![[Pasted image 20240702095707.png]]


In usagebox how to we define a demod recipe. 
Who's an advisor. Passionate sales. If you sell 4 thermomixes you get one for three. 
Most people that sell are self employed. 
We can determine if someone has free access. Advisor vouchers.
**Lara**  is the cosybox expert.
**Market share but won't share**

This vouchers belong to this person which has this thermomix

Vouchers expring June 1st meanss they were active 2024 June 1st. 

Filter one who has used the sensor once. 


How often do they use the sensor 
Per advisor 40 sessoins 20 with the sensor. 
Distribution per market. 
How much are advisors using the sensors (at rate), x

Vorwerk gives framework but they can tailor it later. 
Thermomixcontrol - target temperature started. 
Sensor state: 1 - 
Finished: 6 
Cakes 2->6 
Meats it can be 3,4,5


## Things to keep in mind
- Have a lot of data and is partitioned by ts key
- type for TT_SENSOR_COOKING_COOKED 
- TT_SENSOR_ESTIMATOR_STATE might show that it's actually in use? 

Might be that we have multiple events TT_SENSOR_CONNECTED  


https://miro.com/app/board/uXjVNDxJYHo=/



# Error in query
Didn't have quotes around 'pl'

In advisors_sensors_activity.sql how does this line work? You shouldn't get residence country from that? 
   AND m."dcid" IN (SELECT dcid FROM advisors)
	 