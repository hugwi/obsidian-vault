Getting error 

```
TypeError: 'str' object is not callable
```

describe here https://github.com/datahub-project/datahub/issues/7855

Reinstalling everything from scratch but now I miss sqlalchemy dependency.

![[Pasted image 20230711172046.png]]

Currently installing manually. 

Might be cause I didn't install acryl-datahub[biguquery] but the whole package

```python
ERROR: Cannot install acryl-datahub[bigquery]==0.10.2.3, acryl-datahub[bigquery]==0.10.3, acryl-datahub[bigquery]==0.10.3.1, acryl-datahub[bigquery]==0.10.3.2, acryl-datahub[bigquery]==0.
10.4, acryl-datahub[bigquery]==0.10.4.1, acryl-datahub[bigquery]==0.10.4.2, acryl-datahub[bigquery]==0.10.4.3, acryl-datahub[bigquery]==0.10.5, acryl-datahub[bigquery]==0.10.5.1 and sqlpa rse>=0.4.4 because these package versions have conflicting dependencies.

The conflict is caused by:
    The user requested sqlparse>=0.4.4
    acryl-datahub[bigquery] 0.10.5.1 depends on sqlparse==0.4.3; extra == "bigquery"
    The user requested sqlparse>=0.4.4
    acryl-datahub[bigquery] 0.10.5 depends on sqlparse==0.4.3; extra == "bigquery"
    The user requested sqlparse>=0.4.4
    acryl-datahub[bigquery] 0.10.4.3 depends on sqlparse==0.4.3; extra == "bigquery"
    The user requested sqlparse>=0.4.4
    acryl-datahub[bigquery] 0.10.4.2 depends on sqlparse==0.4.3; extra == "bigquery"
    The user requested sqlparse>=0.4.4
    acryl-datahub[bigquery] 0.10.4.1 depends on sqlparse==0.4.3; extra == "bigquery"
    The user requested sqlparse>=0.4.4
    acryl-datahub[bigquery] 0.10.4 depends on sqlparse==0.4.3; extra == "bigquery"
    The user requested sqlparse>=0.4.4
    acryl-datahub[bigquery] 0.10.3.2 depends on sqlparse==0.4.3; extra == "bigquery"
    The user requested sqlparse>=0.4.4
    acryl-datahub[bigquery] 0.10.3.1 depends on sqlparse==0.4.3; extra == "bigquery"
    The user requested sqlparse>=0.4.4
    acryl-datahub[bigquery] 0.10.3 depends on sqlparse==0.4.3; extra == "bigquery"
    The user requested sqlparse>=0.4.4
    acryl-datahub[bigquery] 0.10.2.3 depends on sqlparse==0.4.3; extra == "bigquery"

To fix this you could try to:
1. loosen the range of package versions you've specified
2. remove package versions to allow pip attempt to solve the dependency conflict
```


Upgrading sqllineage==1.3.8 and sqlparse>=0.4.4 works

#### ReDos
Not sure either of severe this issue is for us either tbh. I think ReDos is mostly concerned with public facing apps where they validate use input and shouldn't be a concern to us. There might of course be some edge cases that might affect us. 

sqlparse is used when computing lineage for tables and columns as well as queries.  

#### TODO: 
- Check datahub contribution.
- Test locally
- Aks in slack if it's possible to upgrade and how they usually take care of this vulnerabilities. 


