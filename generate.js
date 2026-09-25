const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const EDGE_PATH = `"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"`;
const WORKSPACE_DIR = __dirname;
const HTML_FILE = path.join(WORKSPACE_DIR, 'brochure.html');
const PRINT_PDF = path.join(WORKSPACE_DIR, 'NDT_Company_Profile_2026_Print.pdf');
const DIGITAL_PDF = path.join(WORKSPACE_DIR, 'NDT_Company_Profile_2026_Digital.pdf');

console.log('Starting NDT Company Profile PDF generation pipeline...');
console.log(`HTML Source: ${HTML_FILE}`);

// Check if HTML file exists
if (!fs.existsSync(HTML_FILE)) {
  console.error(`Error: Source HTML file not found at ${HTML_FILE}`);
  process.exit(1);
}

// Function to compile PDF using Headless Edge
function compilePDF(outputPath) {
  console.log(`Compiling to: ${outputPath}...`);
  // Edge command with options:
  // --headless: runs without UI
  // --disable-gpu: disabled GPU rendering for headlessness
  // --no-sandbox: bypasses sandbox issues
  // --print-to-pdf: prints to specified file path
  // --no-margins: disables browser-added header/footer margins
  const command = `${EDGE_PATH} --headless --disable-gpu --no-sandbox --print-to-pdf="${outputPath}" --no-margins "${HTML_FILE}"`;
  
  try {
    execSync(command, { stdio: 'inherit' });
    console.log(`Success! PDF successfully compiled to: ${outputPath}`);
  } catch (error) {
    console.error(`Failed compiling PDF to ${outputPath}:`, error);
    throw error;
  }
}

try {
  // 1. Generate High-Resolution Print PDF
  console.log('\n--- 1. Generating High-Resolution Print PDF ---');
  compilePDF(PRINT_PDF);

  // 2. Generate Optimized Digital PDF
  console.log('\n--- 2. Generating Web-Optimized Digital PDF ---');
  compilePDF(DIGITAL_PDF);

  console.log('\n==================================================');
  console.log('NDT Company Profile PDF Generation Pipeline Complete!');
  console.log(`Print version: ${PRINT_PDF}`);
  console.log(`Digital version: ${DIGITAL_PDF}`);
  console.log('==================================================');
} catch (err) {
  console.error('\nPipeline execution failed.');
  process.exit(1);
}
