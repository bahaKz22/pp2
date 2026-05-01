# TSIS 1: Extended PhoneBook Application

A Python and PostgreSQL-based console application for managing contacts. This project extends basic CRUD operations by introducing relational database schema design, multi-field search, pagination, PL/pgSQL stored procedures, and file-based data exchange (JSON/CSV).

## 🚀 Features

* **Advanced Relational Data Model:** Supports multiple phone numbers per contact (1-to-many), emails, birthdays, and contact categorization via groups.
* **Smart Console Interface:** 
  * Filter contacts by specific groups.
  * Search contacts by partial email matching.
  * View contacts with sorting (by Name, Birthday, or Date Added) and interactive pagination.
* **Data Import/Export:**
  * **JSON:** Export the entire database to JSON or import from JSON with smart duplicate handling (Skip or Overwrite).
  * **CSV:** Extended CSV import support for new fields (email, birthday, group, phone type).
* **Database-Side Logic (PL/pgSQL):**
  * `add_phone`: Procedure to easily attach new phone numbers to existing contacts.
  * `move_to_group`: Procedure to reassign contact groups (automatically creates the group if it doesn't exist).
  * `search_contacts`: Advanced global search function scanning through names, emails, and all linked phone numbers.

## 📂 Repository Structure
```text
TSIS1/
├── phonebook.py        # Main Python console application logic
├── config.py           # Database connection credentials
├── connect.py          # PostgreSQL connection setup using psycopg2
├── schema.sql          # SQL script to create tables (contacts, phones, groups)
├── procedures.sql      # SQL script for PL/pgSQL procedures and functions
├── contacts_export.json# Generated JSON export file (created during runtime)
└── README.md           # Project documentation