test

# Security Enhancements in Django Project

## Overview
This document outlines the security measures implemented in the Django project.

### Security Settings
- `DEBUG`: Disabled in production for better security.
- `SECURE_BROWSER_XSS_FILTER`: Protects against XSS attacks.
- `X_FRAME_OPTIONS`: Prevents clickjacking.
- `CSRF_COOKIE_SECURE` and `SESSION_COOKIE_SECURE`: Ensure cookies are only sent over HTTPS.

### CSRF Protection
All forms include the `{% csrf_token %}` tag to prevent cross-site request forgery attacks.

### Secure Data Handling
- User inputs are validated using Django forms.
- SQL injection is mitigated using Django’s ORM.

### Content Security Policy (CSP)
Implemented CSP to mitigate XSS risks:
- Default source: `'self'`
- Scripts and styles restricted to trusted domains.

### Testing
Manually tested for:
- CSRF protection.
- XSS vulnerabilities.
- SQL injection risks.
