---
created: 2026-06-23 13:28
---
tags:: [[+Daily Notes]]

# Invalid date

<< [[Invalid date|Yesterday]] | [[Invalid date|Tomorrow]] >>

---

# 🔥 Todo 

---

# 📝 Notes
- <% tp.file.cursor() %>

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

