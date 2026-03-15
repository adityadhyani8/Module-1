🌐 Why Databases Are Important in Real-World AI Systems?

• 	Centralized storage: AI systems often rely on huge volumes of data (user profiles, sensor readings, transaction logs). Databases provide a reliable way to store and retrieve this information.

• 	Efficiency: Structured databases allow fast queries, which is critical for real-time AI applications like recommendation engines or fraud detection.

• 	Consistency: Databases enforce rules (constraints, schemas) so the data remains clean and usable.

Examples of data stored:
• 	E-commerce AI: user accounts, product catalogs, order histories.
• 	Healthcare AI: patient records, lab results, prescriptions.
• 	Finance AI: transactions, account balances, fraud alerts.

👉 Without structured storage, data would be scattered in files, making it hard to query, update, and ensure accuracy.


📊 Describe the Relational Database Mental Model?

Relational databases organize data into tables:
- Table = represents one entity (e.g., Users, Orders).
- Row = one record (e.g., a single user).
- Column = one attribute (e.g., user’s name, email).

👉 Each table should represent a single entity to avoid confusion. Mixing users and orders in one table would make queries messy and redundant


🔑 Explain the concept of a primary key?

- A primary key uniquely identifies each row in a table.
- Must be unique (no duplicates) and non-null (always present).
- Helps prevent ambiguity when retrieving or updating records.

Example:
- In the Users table, UserID is the primary key.
- Even if two users share the same name, their UserID ensures they are distinct.


📐 Explain what a database schema is?

- A schema defines the structure of the database: tables, columns, data types, relationships, and constraints.
- Ensures consistency so every developer or AI system knows how the data is organized.

Example Schema Info:
- Users table: columns → UserID (INT), Name (VARCHAR), Email (VARCHAR)
- Orders table: columns → OrderID (INT), UserID (INT), Amount (DECIMAL)

👉 Schemas are like blueprints — they prevent chaos when multiple teams or systems interact with the same database.


🔗 Explain how relationships between tables work in relational databases?

Relational databases connect tables using foreign keys:
- A foreign key is a column in one table that references the primary key of another.
- This creates logical links between entities.

Example: Users and Orders
- Users(UserID) is the primary key.
- Orders(UserID) is a foreign key referencing Users(UserID).