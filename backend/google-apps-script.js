/**
 * Fresh Math Contact Form Handler
 * Google Apps Script for handling contact form submissions
 *
 * This script:
 * 1. Receives form submissions from your website
 * 2. Stores them in a Google Sheet
 * 3. Sends email notifications
 * 4. Returns a JSON response to the form
 */

// CONFIGURATION - UPDATE THESE VALUES
const CONFIG = {
  // The email address where notifications should be sent
  NOTIFICATION_EMAIL: 'your-email@example.com',

  // The name of your Google Sheet (will be created automatically)
  SHEET_NAME: 'Contact Form Submissions',

  // Subject line for notification emails
  EMAIL_SUBJECT_PREFIX: '[Fresh Math Contact]',

  // Allow these domains to submit forms (CORS)
  ALLOWED_ORIGINS: [
    'https://mathskillsforkids.com',
    'http://localhost',
    'http://127.0.0.1'
  ]
};

/**
 * Handles POST requests from the contact form
 */
function doPost(e) {
  try {
    // Parse the form data
    const formData = JSON.parse(e.postData.contents);

    // Validate required fields
    if (!formData.name || !formData.email || !formData.message || !formData.subject) {
      return createResponse(false, 'Missing required fields');
    }

    // Validate email format
    if (!isValidEmail(formData.email)) {
      return createResponse(false, 'Invalid email address');
    }

    // Add timestamp
    formData.timestamp = new Date();

    // Save to Google Sheet
    saveToSheet(formData);

    // Send email notification
    sendNotificationEmail(formData);

    // Return success response
    return createResponse(true, 'Thank you for contacting us! We will respond within 24-48 hours.');

  } catch (error) {
    Logger.log('Error processing form: ' + error.toString());
    return createResponse(false, 'An error occurred. Please try again or email us directly.');
  }
}

/**
 * Handles GET requests (for testing)
 */
function doGet(e) {
  return ContentService.createTextOutput(
    JSON.stringify({
      status: 'ok',
      message: 'Fresh Math Contact Form Backend is running'
    })
  ).setMimeType(ContentService.MimeType.JSON);
}

/**
 * Saves form submission to Google Sheet
 */
function saveToSheet(data) {
  const spreadsheet = getOrCreateSpreadsheet();
  const sheet = spreadsheet.getSheetByName(CONFIG.SHEET_NAME) || createSheet(spreadsheet);

  // Append the data as a new row
  sheet.appendRow([
    data.timestamp,
    data.name,
    data.email,
    data.subject,
    data.grade || 'N/A',
    data.message,
    'New' // Status column
  ]);
}

/**
 * Gets or creates the spreadsheet
 */
function getOrCreateSpreadsheet() {
  const files = DriveApp.getFilesByName(CONFIG.SHEET_NAME);

  if (files.hasNext()) {
    return SpreadsheetApp.open(files.next());
  }

  // Create new spreadsheet
  const spreadsheet = SpreadsheetApp.create(CONFIG.SHEET_NAME);
  createSheet(spreadsheet);
  return spreadsheet;
}

/**
 * Creates and formats the sheet with headers
 */
function createSheet(spreadsheet) {
  const sheet = spreadsheet.getSheets()[0];
  sheet.setName(CONFIG.SHEET_NAME);

  // Set up headers
  const headers = ['Timestamp', 'Name', 'Email', 'Subject', 'Grade Level', 'Message', 'Status'];
  sheet.getRange(1, 1, 1, headers.length).setValues([headers]);

  // Format headers
  sheet.getRange(1, 1, 1, headers.length)
    .setFontWeight('bold')
    .setBackground('#8B5CF6')
    .setFontColor('#FFFFFF');

  // Set column widths
  sheet.setColumnWidth(1, 150); // Timestamp
  sheet.setColumnWidth(2, 150); // Name
  sheet.setColumnWidth(3, 200); // Email
  sheet.setColumnWidth(4, 150); // Subject
  sheet.setColumnWidth(5, 100); // Grade Level
  sheet.setColumnWidth(6, 400); // Message
  sheet.setColumnWidth(7, 100); // Status

  // Freeze header row
  sheet.setFrozenRows(1);

  return sheet;
}

/**
 * Sends email notification
 */
function sendNotificationEmail(data) {
  const subject = `${CONFIG.EMAIL_SUBJECT_PREFIX} ${data.subject}`;

  const htmlBody = `
    <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
      <div style="background-color: #8B5CF6; color: white; padding: 20px; text-align: center;">
        <h2>New Contact Form Submission</h2>
      </div>

      <div style="padding: 20px; background-color: #f9fafb;">
        <h3 style="color: #374151;">Contact Details</h3>
        <table style="width: 100%; border-collapse: collapse;">
          <tr>
            <td style="padding: 8px; border-bottom: 1px solid #e5e7eb; font-weight: bold; width: 150px;">Name:</td>
            <td style="padding: 8px; border-bottom: 1px solid #e5e7eb;">${data.name}</td>
          </tr>
          <tr>
            <td style="padding: 8px; border-bottom: 1px solid #e5e7eb; font-weight: bold;">Email:</td>
            <td style="padding: 8px; border-bottom: 1px solid #e5e7eb;">
              <a href="mailto:${data.email}">${data.email}</a>
            </td>
          </tr>
          <tr>
            <td style="padding: 8px; border-bottom: 1px solid #e5e7eb; font-weight: bold;">Subject:</td>
            <td style="padding: 8px; border-bottom: 1px solid #e5e7eb;">${data.subject}</td>
          </tr>
          <tr>
            <td style="padding: 8px; border-bottom: 1px solid #e5e7eb; font-weight: bold;">Grade Level:</td>
            <td style="padding: 8px; border-bottom: 1px solid #e5e7eb;">${data.grade || 'Not specified'}</td>
          </tr>
          <tr>
            <td style="padding: 8px; border-bottom: 1px solid #e5e7eb; font-weight: bold;">Submitted:</td>
            <td style="padding: 8px; border-bottom: 1px solid #e5e7eb;">${data.timestamp}</td>
          </tr>
        </table>

        <h3 style="color: #374151; margin-top: 20px;">Message</h3>
        <div style="background-color: white; padding: 15px; border-left: 4px solid #8B5CF6; white-space: pre-wrap;">
${data.message}
        </div>

        <div style="margin-top: 20px; padding: 15px; background-color: #FEF3C7; border-radius: 4px;">
          <p style="margin: 0; color: #92400E;">
            <strong>Quick Reply:</strong>
            <a href="mailto:${data.email}?subject=Re: ${encodeURIComponent(data.subject)}"
               style="color: #8B5CF6;">Click here to reply</a>
          </p>
        </div>
      </div>

      <div style="background-color: #374151; color: white; padding: 15px; text-align: center; font-size: 12px;">
        Fresh Math Contact Form - Automated Notification
      </div>
    </div>
  `;

  const plainBody = `
New Contact Form Submission - Fresh Math

Name: ${data.name}
Email: ${data.email}
Subject: ${data.subject}
Grade Level: ${data.grade || 'Not specified'}
Submitted: ${data.timestamp}

Message:
${data.message}

---
Reply to: ${data.email}
  `;

  try {
    MailApp.sendEmail({
      to: CONFIG.NOTIFICATION_EMAIL,
      subject: subject,
      body: plainBody,
      htmlBody: htmlBody,
      replyTo: data.email
    });
  } catch (error) {
    Logger.log('Error sending email: ' + error.toString());
  }
}

/**
 * Validates email format
 */
function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

/**
 * Creates a JSON response with CORS headers
 */
function createResponse(success, message, data = {}) {
  const response = {
    success: success,
    message: message,
    data: data
  };

  return ContentService
    .createTextOutput(JSON.stringify(response))
    .setMimeType(ContentService.MimeType.JSON);
}

/**
 * Test function - run this to verify setup
 */
function testFormSubmission() {
  const testData = {
    postData: {
      contents: JSON.stringify({
        name: 'Test User',
        email: 'test@example.com',
        subject: 'general',
        grade: 'grade3',
        message: 'This is a test message to verify the contact form is working correctly.'
      })
    }
  };

  const result = doPost(testData);
  Logger.log(result.getContent());
}
