# cpsc_recalls_api

This package queries the U.S. Consumer Product Safety Commission Recalls database
and save the result into a json file. With the CLI interface, the -kv tag must be 
invoked before specifying a list of key/value pair for query. Query result will 
be saved in a json file in the "target" folder.

An example of usage:

    python src/app.py -kv RecallTitle=child RecallDescription=metal
