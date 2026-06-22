---
created: 2023-12-06 09:09
---
tags:: [[+Daily Notes]]

# Wednesday, December 06, 2023

<< [[2023-12-05-Tuesday|Yesterday]] | [[2023-12-07-Thursday|Tomorrow]] >>

---

# 🔥 Todo 
- [ ] Vw
	- [ ] Sketch anonymization flow
	 - [ ] Reach out to Valentina and Benedikt to ask about dcid
- [ ] Netlight 
	 - [ ] Remove myself from the Munich group
	 - [ ] Reach out to Klarna to setup a meeting - Gunnar Tångring
	- [ ] Faktura flytt kolla victoria
 - [ ] Backlog
	- [ ] Sketch Ingestion flow
	- [ ] Remove administrator role
	- [ ] WAITING - Check if CDC is disadvantagous if data is updated daily.
	- [ ] Create a data and dumplings website
	- [ ] Write about data governance initiative
	- [ ] See how a role for reading CDC can be setup.
- [ ] Thoughts
	- [ ] Can we do quality checks too see that CDC works. For isntance hashnig a table?

---

# 📝 Notes
#databricks-account-admin
Please refer here - [https://community.databricks.com/s/question/0D58Y000098lIqgSAE/unity-catalog-azure-account-console-h...](https://community.databricks.com/s/question/0D58Y000098lIqgSAE/unity-catalog-azure-account-console-how-to-access)

- You must be an Azure Databricks account admin.
- **The first Azure Databricks account admin must be an Azure Active Directory Global Administrator at the time that they first log in to the Azure Databricks account console.** Upon first login, that user becomes an Azure Databricks account admin and no longer needs the Azure Active Directory Global Administrator role to access the Azure Databricks account. The first account admin can assign users in the Azure Active Directory tenant as additional account admins (who can themselves assign more account admins). Additional account admins do not require specific roles in Azure Active Directory.
- Your Azure Databricks account must be on the [Premium plan](https://azure.microsoft.com/pricing/details/databricks/).

[https://accounts.azuredatabricks.net/login/](https://accounts.azuredatabricks.net/login/)

## Development of data strategy

Another consultancy workshop. How should Vorwerk organization should look like. 
How to 

---
### Notes created today
```dataview
LIST  
WHERE file.cday = this.file.day  
SORT file.time asc  
```

### Notes last touched today
```dataview
LIST  
WHERE file.mday = this.file.day  
SORT file.mtime asc  
```

