import os
import shutil
import subprocess
from PIL import Image

workspace_dir = r"c:\Users\shibi\Desktop\antigravity company profile"
assets_dir = os.path.join(workspace_dir, "assets")
backup_dir = os.path.join(workspace_dir, "assets_backup")
html_file = os.path.join(workspace_dir, "brochure.html")
print_pdf = os.path.join(workspace_dir, "NDT_Company_Profile_2026_Print.pdf")
digital_pdf = os.path.join(workspace_dir, "NDT_Company_Profile_2026_Digital.pdf")
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

def run_edge(output_pdf):
    print(f"Compiling PDF via Edge to: {output_pdf}")
    user_data_dir = os.path.join(workspace_dir, "edge_profile")
    cmd = [
        edge_path,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        f"--print-to-pdf={output_pdf}",
        "--no-margins",
        f"--user-data-dir={user_data_dir}",
        html_file
    ]
    # Spawning process
    subprocess.run(cmd, check=True)
    print(f"Successfully created: {output_pdf} (size: {os.path.getsize(output_pdf)} bytes)")

def compress_images_in_place():
    print("Compressing image assets for web-optimized digital PDF...")
    for root, dirs, files in os.walk(assets_dir):
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in ['.jpg', '.jpeg', '.png', '.webp']:
                file_path = os.path.join(root, f)
                try:
                    with Image.open(file_path) as img:
                        # Convert to RGB if RGBA (JPEG doesn't support transparency)
                        if img.mode in ('RGBA', 'LA') or (ext in ['.jpg', '.jpeg'] and img.mode != 'RGB'):
                            img = img.convert('RGB')
                        
                        # Downscale if larger than 1200px
                        max_size = 1200
                        if img.width > max_size or img.height > max_size:
                            img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
                        
                        # Compress and overwrite
                        if ext == '.webp':
                            img.save(file_path, 'WEBP', quality=70)
                        else:
                            img.save(file_path, 'JPEG', quality=75, optimize=True)
                        print(f"Optimized image: {f}")
                except Exception as e:
                    print(f"Skipped/Failed compressing {f}: {e}")

def main():
    print("==================================================")
    print("NDT Company Profile Python Compilation Pipeline")
    print("==================================================")

    # 1. Back up original high-res assets
    print("Backing up high-resolution assets to temporary folder...")
    if os.path.exists(backup_dir):
        shutil.rmtree(backup_dir)
    shutil.copytree(assets_dir, backup_dir)

    try:
        # 2. Compile the Print version using original high-res assets
        print("\n--- STEP 1: Compiling Print Version (High-Res) ---")
        run_edge(print_pdf)

        # 3. Compress assets in-place
        print("\n--- STEP 2: Downscaling & Compressing Assets ---")
        compress_images_in_place()

        # 4. Compile the Digital version using compressed assets
        print("\n--- STEP 3: Compiling Digital Version (Web-Optimized) ---")
        run_edge(digital_pdf)

    except Exception as e:
        print(f"\nError occurred during execution: {e}")
    finally:
        # 5. Restore original assets
        print("\n--- STEP 4: Restoring High-Resolution Assets ---")
        if os.path.exists(backup_dir):
            if os.path.exists(assets_dir):
                shutil.rmtree(assets_dir)
            shutil.copytree(backup_dir, assets_dir)
            shutil.rmtree(backup_dir)
            print("Original high-resolution assets successfully restored.")
        print("\nPipeline Complete!")
        print("==================================================")

if __name__ == "__main__":
    main()
