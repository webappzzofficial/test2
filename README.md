# NDT — Nabeel Dar Transport LLC
### Corporate Company Profile & Digital Visiting Card Suite

A complete corporate branding and digital presence suite for **NABEEL DAR TRANSPORT LLC (NDT)** — Dubai, United Arab Emirates.

---

## 📁 Repository Contents (What to Add to GitHub)

| File / Folder | Purpose |
| :--- | :--- |
| **`index.html`** / **`digital-card.html`** | Interactive mobile-first digital visiting card web application. |
| **`NDT_Company_Profile_2026_Digital.pdf`** | Optimized 16-page digital company brochure (~14.6MB) ready for web/email. |
| **`NDT_Company_Profile_2026_Print.pdf`** | High-resolution 16-page print-ready brochure (~24.2MB) with CMYK-ready assets. |
| **`NDT_Digital_Visiting_Card.pdf`** | Double-sided executive business card PDF (85mm × 55mm format, ~207KB). |
| **`ndt-contact.vcf`** | vCard 3.0 file that adds NDT directly to phone address books with one tap. |
| **`brochure.html`** | Master source code for the 16-page company profile. |
| **`brochure.css`** | Luxury monochrome and gold print styling rules (Inter font, A4 grid). |
| **`business-card.html`** | Source code for the double-sided executive business card. |
| **`ndt-logo-white.png`** | Official transparent white vector-quality logo. |
| **`ndt-logo.jpg`** | Official dark logo on solid white background. |
| **`assets/`** | Sourced and generated high-resolution crane, transport, and equipment imagery. |
| **`compile.py`** | Python build script to compile all PDFs using headless Microsoft Edge. |
| **`.gitignore`** | Excludes temporary browser profiles and OS cache files. |

---

## 🚀 How to Host on GitHub Pages (Free Live Digital Card)

By hosting this repository on **GitHub Pages**, your digital visiting card becomes instantly accessible worldwide at `https://<your-username>.github.io/<repository-name>/`.

### Step 1: Initialize Git and Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit: NDT Company Profile & Digital Card Suite"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo-name>.git
git push -u origin main
```

### Step 2: Enable GitHub Pages
1. Go to your repository on **GitHub.com**.
2. Click **Settings** (top navigation).
3. In the left sidebar, click **Pages**.
4. Under **Build and deployment > Branch**:
   - Select **`main`** branch.
   - Select **`/ (root)`** folder.
5. Click **Save**.
6. Within 1–2 minutes, GitHub will provide your live URL (e.g., `https://<username>.github.io/<repo>/`).

---

## 📲 How Downloads Work Inside the Digital Card

When someone visits your digital card link on their phone:
1. **Downloading the 16-Page Company Profile PDF**:
   - Tapping the **"DOWNLOAD COMPANY PROFILE PDF"** button automatically downloads `NDT_Company_Profile_2026_Digital.pdf` directly from your GitHub repository onto their device.
   - No external file hosting or Dropbox/Drive link is required.
2. **One-Tap "Save to Contacts" (vCard)**:
   - Tapping the **"SAVE TO CONTACTS"** button downloads `ndt-contact.vcf` (or opens it directly), instantly prompting iOS or Android to add NDT with verified phone (+971 55 295 2354), WhatsApp, emails, website, and Dubai location.
3. **One-Tap Actions**:
   - **Call**: Directly triggers the phone dialer.
   - **WhatsApp**: Opens WhatsApp directly with a prefilled enquiry message.
   - **Email**: Opens the default mail client addressed to `salesenquiry@nabeeldartransport.com`.
   - **Share Card**: Opens a modal with a scannable QR code and a button to copy the live link.

---

## 🏗️ Build & Compilation

To recompile the PDFs locally at any time:
```bash
python compile.py
```
This runs the dual-pipeline that downscales web JPEGs for the digital version and retains full uncompressed resolution for the print version.

---

&copy; 2026 **NABEEL DAR TRANSPORT LLC (NDT)** &bull; Dubai, United Arab Emirates
