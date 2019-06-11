# Group Tree Delete

Feed this guy a Rock group id and it will delete the group and all the groups, attendance, attendance occurrences nested under that group.  Great for cleaning up old groups.

## This will DELETE data, no getting it back.

Pass the following arguments at the command line, all are required:

-u Rock RMS URL
-k Rock RMS API Key
-g Rock RMS Group ID

Example:

```python3 grouptreedelete.py -u 'https://rock.example.com' -k 'API Key' -g '123456'```


