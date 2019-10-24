# cpsc_recalls_api

This package queries the U.S. Consumer Product Safety Commission Recalls database and saves the result into a JSON file. With the CLI interface, the -kv tag must be invoked before specifying a list of key/value pairs for the query. Query results will be saved in a JSON file in the "target" folder.

An example of usage:

    python src/app.py -kv RecallTitle=child RecallDescription=metal
