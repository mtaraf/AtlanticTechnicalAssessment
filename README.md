Entitlements System

This project implements a simple entitlements system for a publisher website. It models user access based on purchased products and supports entitlement lifecycle management including expiration and revocation.

Features
Three subscription products: - Digital → website content access - Print → website content + print magazine - Premium → website content + print magazine + no ads
Users can hold one or more entitlements
Entitlements support: - Expiration (end_date) - Revocation (revoked)
API to query current user entitlements
Django Admin interface for inspection
Seed command for demo data

Tech Stack

- Python 3.10+
- Django 4.2+
- Django REST Framework
- SQLite (default DB)

Setup Instructions

1. Create virtual environment
   - python -m venv venv
   - Windows: venv\Scripts\activate
   - Mac/Linux: source venv/bin/activate
2. Install dependencies
   - pip install -r requirements.txt
3. Run migrations
   - python manage.py makemigrations
   - python manage.py migrate
4. Seed demo data
   - python manage.py seed_data

This creates the following users:

| Username     | Password    | Product |
| ------------ | ----------- | ------- |
| digital_user | password123 | Digital |
| print_user   | password123 | Print   |
| premium_user | password123 | Premium |

5. Create a superuser
   - python manage.py createsuperuser
6. Run server
   - python manage.py runserver
   - available at: http://127.0.0.1:8000/

API Usage

Create Entitlement
POST /api/entitlements/
Request:
{
"user": 1,
"product": "PREMIUM",
"end_date": "2026-06-01T00:00:00Z",
"revoked": false
}

Get Current User Entitlements
GET /api/entitlements/user/{user_id}/current/
Response:
{
"entitlements": [
"website_content",
"print_magazine",
"no_ads"
]
}
