date: {{date}}
Yesterday: <% tp.date.yesterday("YYYY-MM-DD") %>
Tomorrow: <% tp.date.tomorrow("YYYY-MM-DD") %>
file title: <% tp.file.title %>
File existence of current file: 
<% await tp.file.exists(tp.file.folder(true)+"/"+tp.file.title+".md") %>
<% tp.web.daily_quote() %>
