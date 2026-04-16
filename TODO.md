# Django PostgreSQL Connection Fix - TODO List

## Approved Plan Steps (User confirmed: yes)

**Goal:** Fix PostgreSQL connection error, enable migrations/server.

**Step 1: [DONE] PostgreSQL check**
- No service/pg tools found → Not installed.

**Step 2: [PENDING] Setup PostgreSQL (if needed)**
- Install if missing
- Start service
- Create DB `bibliotheque` and user `postgres`/`postgres`

**Step 3: [DONE] Switch to SQLite**
- Update settings.py ✓
- Remove db.sqlite3 ✓
- Run migrations ✓

**Step 4: [DONE] Migrations**
- All api/admin/auth migrations applied OK ✓

**Step 5: [PENDING] Test server**
- `python manage.py runserver`
- Create superuser if needed

**Current Status:** Ready for Step 1. Updates will mark [DONE].
