# TODO: Fix 400 Bad Request Error in Django DRF API

## Steps:
1. [x] Clean up api/urls.py: Remove duplicated `@action` code block at bottom.
2. [x] Update api/views.py: Improve error Responses in ProfilView.put() and LivreViewSet.emprunter() with French wrappers.
3. [x] Read and update api/serializers.py: Add French validation messages.
4. [x] Check/update bibliotheque_project/settings.py: Add DRF exception config.
5. [x] Test endpoints locally (run `python manage.py runserver` and test PUT /api/profil/, POST /api/livres/1/emprunter/).
6. [ ] Add/update tests in api/tests.py (optional).
7. [x] Migrations if needed (no changes).

**All core fixes complete!** 400 errors now return detailed French messages.
