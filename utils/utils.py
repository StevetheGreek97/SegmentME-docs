import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# The app itself (build.py, the release workflow) lives in the SegmentME
# repo, not this docs repo -- that's where CI actually publishes releases.
# "latest" rather than a pinned version/filename: build.py names archives
# with the version and CPU architecture baked in (e.g.
# SegmentME-Setup-2.0.0-windows-cpu-x64.exe,
# SegmentME-2.0.0-macos-cpu-arm64.dmg), and each platform ships only its
# native installer -- Setup.exe on Windows, .dmg on macOS -- except Linux,
# which also keeps a .tar.gz alongside the .deb for non-Debian distros.
# Linking the release page rather than one guessed filename lets the
# visitor pick the right one and never goes stale.
_RELEASES_URL = "https://github.com/StevetheGreek97/SegmentME/releases/latest"

_PLATFORM_NAMES = {"windows": "Windows", "macos": "macOS", "linux": "Linux"}

_BUILD_LABELS = {"cpu": "CPU", "cuda": "CUDA"}

_INSTALL_STEPS = {
    ("windows", "cpu"): """Download SegmentME-Setup-<version>-windows-cpu-x64.exe from the release page and run it.
Follow the installer prompts to finish. This build works on any computer, with or without an NVIDIA GPU.""",
    ("windows", "cuda"): """Download SegmentME-Setup-<version>-windows-cuda-x64.exe from the release page and run it.
Follow the installer prompts to finish. This build needs an NVIDIA GPU.""",
    ("macos", "cpu"): """Download SegmentME-<version>-macos-cpu-arm64.dmg from the release page and open it.
Drag SegmentME.app onto the Applications shortcut inside the window. This build is for Apple Silicon Macs only.""",
    ("linux", "cpu"): """Debian, Ubuntu, or Mint -- download segmentme_<version>_amd64.deb and install it:

    sudo apt install ./segmentme_<version>_amd64.deb

SegmentME then appears in the applications menu, and .SEproj project files open with it on
double-click. Remove it later with: sudo apt remove segmentme

Other distributions -- download SegmentME-<version>-linux-cpu-x64.tar.gz (or -arm64 on an ARM machine),
extract it, and run this inside the extracted folder:

    ./install-desktop.sh

From source -- clone the repository, then install and run:

    git clone https://github.com/StevetheGreek97/SegmentME.git
    cd SegmentME
    ./install.sh
    ./run.sh""",
    ("linux", "cuda"): """This build needs an NVIDIA GPU. It comes in parts, so download every
segmentme-cuda_<version>_amd64.deb.part-NN file from the release page, then join, verify, and install them:

    cat segmentme-cuda_<version>_amd64.deb.part-* > segmentme-cuda_<version>_amd64.deb
    sha256sum --ignore-missing -c SHA256SUMS
    sudo apt install ./segmentme-cuda_<version>_amd64.deb""",
}


def send_auto_reply(platform, name, last_name, recipient_email, smtp_user, smtp_pass, build="cpu"):
    platform = platform.lower()
    platform_name = _PLATFORM_NAMES[platform]
    build_label = _BUILD_LABELS[build]

    subject = "🎉 Your SegmentME Installer is Ready"
    body = f"""
Hi {name} {last_name},

Thanks for your interest in SegmentME! Your {platform_name} {build_label} download is ready on the latest release page:
🔗 {_RELEASES_URL}

Each release lists several files -- pick the one for {platform_name} {build_label}.

How to install SegmentME on {platform_name} ({build_label} build):

{_INSTALL_STEPS[(platform, build)]}

If you have any questions or feedback, feel free to reply to this email.

Best regards,
PopGen Team
"""

    msg = MIMEMultipart()
    msg["From"] = smtp_user
    msg["To"] = recipient_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)


def is_valid_email(email):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

def notify_admin(name, last_name, user_email, comments, smtp_user, smtp_pass, recipient_email, build="cpu"):
    subject = "📥 New SegmentME Installer Request"
    body = f"""
You received a new request for the SegmentME installer.

👤 Name: {name} {last_name}
📧 Email: {user_email}
📦 Build: {_BUILD_LABELS[build]}
📝 Comments: {comments or 'None provided'}

Please follow up manually with the download link.
"""

    msg = MIMEMultipart()
    msg["From"] = smtp_user
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)


def get_text(section, file_path='assets/text.yaml'
):
    """
    Get the text for a given section from the text.yaml file.
    
    Args:
        section (str): The section to retrieve text for.
        
    Returns:
        str: The text for the specified section.
    """
    import yaml
    from pathlib import Path

    # Load the YAML file
    text_file = Path(__file__).parent.parent / file_path
    with open(text_file, 'r') as file:
        text_data = yaml.safe_load(file)

    # Return the requested section
    return text_data.get(section, '')


if __name__ == "__main__":
    # Example usage
    section = 'intro'
    text = get_text(section)
    print(f"Text for section '{section}': {text}")
    # Output: Text for section 'intro': SegmentME is a powerful image annotation and segmentation tool designed for high-throughput phenotyping, object instance analysis, and smart annotation workflows using models like
