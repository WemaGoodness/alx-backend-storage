# MongoDB Command Files

This project contains MongoDB command files for various tasks. Each file is designed to be executed with the MongoDB shell to perform a specific task.

## Files

1. `0-list_databases`: Lists all databases.
2. `1-use_or_create_database`: Switches to or creates the `my_db` database.
3. `2-insert`: Inserts a document with the name "Holberton school" into the `school` collection.
4. `3-all`: Lists all documents in the `school` collection.
5. `4-match`: Lists all documents in the `school` collection where the name is "Holberton school".
6. `5-count`: Displays the number of documents in the `school` collection.
7. `6-update`: Updates documents in the `school` collection with the name "Holberton school" by adding the address "972 Mission street".

## Usage

To run a specific file, use the following command:

```bash
mongo <filename>
