# QA Test Report: TennistMate

## Bugs Discovered During Testing

1. **Profile Save Bug**: 
   - **Issue**: The player's name is not saved when updating the profile.
   - **Root Cause**: The input field for the player's name (`#profile-name`) is positioned outside of the `#tab-stats` div. The `saveProfile()` function only selects elements within `#tab-stats`, effectively ignoring the user's name entirely upon both save and load.
   
2. **Gated Content Email Override Bug**:
   - **Issue**: When unlocking the AI insights, a user could enter an arbitrary email address.
   - **Root Cause**: The unlock form asks for an email, which gets sent to `/api/auth/login`. Because this endpoint performs an upsert, it could log the user into a completely different account silently. The phone number would then be associated with the wrong account, causing desynchronization with the frontend `localStorage`.

3. **Critical Security Flaw in Admin APIs**:
   - **Issue**: The entire Coach Admin backend is unauthenticated.
   - **Root Cause**: `admin.html` uses frontend-only gates (a hardcoded email check and a hardcoded PIN `1743`). However, the API functions (`/api/admin/roster`, `/api/admin/delete_user`, `/api/admin/lessons`, `/api/admin/generate`) perform ZERO authentication checks. Anyone with the API URLs can view the entire database, delete any user, and trigger AI prompts.

## Proposed Solutions (In Development)
- Fix the DOM selectors in `profile.html` to correctly serialize and deserialize `#profile-name`.
- Pre-fill and lock the email field in the AI unlock form using the active session's email.
- Require an `X-Admin-Pin` header on all `/api/admin/*` endpoints and validate it on the server. Update `admin.html` to pass this header in all requests.