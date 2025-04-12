# WRNL Volunteer Attendance Portal WebApp - Change Log

## Overview
This page tracks the changes made to the WRNL Volunteer Attendance Portal WebApp. It provides a log of updates, bug fixes, and new features.
Current Version: **v2.1** (deployed on Vercel)

## Change Log
### 12 April 2025
- **Major Update:** New Version of WebApp (v2)
  1. Refined Google Apps Script to function as an API server.
  2. Migrated frontend and backend code from Google Apps Script to GitHub.
  3. Refactored HTML file to shift backend JavaScript functions into Python functions, separated into a distinct file.
  4. Implemented Python Flask to power the web application.
  5. Deployed the web application on Render.
  6. Deploymed the web application on Vercel (v2.1)
- **Miscellaneous:** Added a favicon to improve site branding.

### 11 April 2025
- **Update:** Transferred GitHub Repository Ownership and Updated URL
  1. Transferred ownership of the GitHub repository to the WRNL GitHub account.
  2. Updated all relevant links to reflect the new URL redirect link.

### 7 April 2025
- **Feature:** User Interface and User Experience Enhancements
  1. Integrated a header image into the website, hosted on GitHub.
  2. Disabled the submit button during the data loading process to prevent user interaction and visually indicate that attendance information is being processed.
  3. Enabled the use of the Enter key to submit user input, in addition to the existing functionality of clicking the submit button
  4. Standardised the display of output names to proper case formatting, enhancing readability and consistency.

- **Feature:** URL Redirect
  1. Implemented a URL redirect using a GitHub Pages link to seamlessly redirect users to the longer Google Apps Script URL


### 6 April 2025
- **Bug fix:** Resolved issues related to duplicate and missing records. 
  1. Performed a comprehensive cleanup of the database (extraneous whitespace, incomplete/inconsistent name entries).
  2. Cross-referenced the current database with the legacy database to ensure all participant entries are accurately recorded.

- **Feature:** Initial Version of the WebApp (v1)
  1. Migrated attendance data for Sessions 11 and 12 into the current database.
  2. Developed the frontend using Google Apps Script with JavaScript and HTML.
 
## Repository links:
- v2.2: https://github.com/wearenotlemons/wrnl-vercel
- v2: https://github.com/wearenotlemons/wearenotlemons
