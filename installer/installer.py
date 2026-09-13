import os
import shutil
import subprocess
import sys
import tkinter as tk

from pathlib import Path
from tkinter import filedialog, messagebox, ttk


APP_NAME = "OrbitLang"
MIN_PYTHON = (3, 10)


class Installer:
    def __init__(self, root):
        self.root = root

        self.root.title(f"{APP_NAME} Installer")
        self.root.geometry("700x450")
        self.root.resizable(False, False)

        self.project_root = Path(__file__).resolve().parent.parent

        self.install_path = tk.StringVar(
            value=str(Path.home() / ".local" / "share" / "orbitlang")
        )

        self.page = 0

        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        self.buttons = tk.Frame(self.root)
        self.buttons.pack(fill="x", padx=25, pady=20)

        self.back_button = tk.Button(
            self.buttons,
            text="Back",
            width=10,
            command=self.previous_page,
            state="disabled",
        )
        self.back_button.pack(side="left")

        self.cancel_button = tk.Button(
            self.buttons,
            text="Cancel",
            width=10,
            command=self.cancel,
        )
        self.cancel_button.pack(side="right")

        self.next_button = tk.Button(
            self.buttons,
            text="Next",
            width=10,
            command=self.next_page,
        )
        self.next_button.pack(side="right", padx=(0, 10))

        self.show_page()

    # ---------------------------------------------------------
    # Page management
    # ---------------------------------------------------------

    def clear_page(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def show_page(self):
        self.clear_page()

        if self.page == 0:
            self.show_welcome()

        elif self.page == 1:
            self.show_python_check()

        elif self.page == 2:
            self.show_install_location()

        elif self.page == 3:
            self.show_install_page()

        elif self.page == 4:
            self.show_finished()

        self.update_buttons()

    def update_buttons(self):
        if self.page == 0:
            self.back_button.config(state="disabled")
        else:
            self.back_button.config(state="normal")

        if self.page == 3:
            self.next_button.config(
                text="Install",
                command=self.install,
            )
        elif self.page == 4:
            self.next_button.config(
                text="Finish",
                command=self.finish,
            )
        else:
            self.next_button.config(
                text="Next",
                command=self.next_page,
            )

    # ---------------------------------------------------------
    # UI helpers
    # ---------------------------------------------------------

    def create_title(self, text):
        return tk.Label(
            self.container,
            text=text,
            font=("TkDefaultFont", 22, "bold"),
        )

    def create_description(self, text):
        return tk.Label(
            self.container,
            text=text,
            justify="left",
            wraplength=600,
        )

    # ---------------------------------------------------------
    # Welcome
    # ---------------------------------------------------------

    def show_welcome(self):
        self.create_title(
            "Welcome to the OrbitLang Installer"
        ).pack(pady=(70, 25))

        self.create_description(
            "This installer will install OrbitLang on your system.\n\n"
            "OrbitLang is a small interpreted programming language "
            "implemented in Python."
        ).pack(pady=10)

        tk.Label(
            self.container,
            text="Click Next to continue.",
        ).pack(pady=30)

    # ---------------------------------------------------------
    # Python check
    # ---------------------------------------------------------

    def check_python(self):
        return (
            sys.version_info.major,
            sys.version_info.minor,
        ) >= MIN_PYTHON

    def show_python_check(self):
        self.create_title(
            "Python Check"
        ).pack(pady=(60, 25))

        if self.check_python():
            version = (
                f"{sys.version_info.major}."
                f"{sys.version_info.minor}."
                f"{sys.version_info.micro}"
            )

            tk.Label(
                self.container,
                text=f"✓ Python {version} detected.",
                font=("TkDefaultFont", 12),
            ).pack(pady=15)

            tk.Label(
                self.container,
                text="Python is required to run OrbitLang.",
            ).pack()

        else:
            tk.Label(
                self.container,
                text=(
                    "Python 3.10 or newer is required.\n\n"
                    f"Detected: "
                    f"{sys.version_info.major}."
                    f"{sys.version_info.minor}."
                    f"{sys.version_info.micro}"
                ),
                justify="center",
            ).pack(pady=20)

    # ---------------------------------------------------------
    # Install location
    # ---------------------------------------------------------

    def show_install_location(self):
        self.create_title(
            "Installation Location"
        ).pack(pady=(55, 25))

        tk.Label(
            self.container,
            text="Choose where OrbitLang should be installed:",
        ).pack(pady=10)

        frame = tk.Frame(self.container)
        frame.pack(pady=15, padx=50, fill="x")

        entry = tk.Entry(
            frame,
            textvariable=self.install_path,
        )
        entry.pack(side="left", fill="x", expand=True)

        tk.Button(
            frame,
            text="Browse...",
            command=self.choose_directory,
        ).pack(side="right", padx=(10, 0))

        tk.Label(
            self.container,
            text=(
                "The installer will create the OrbitLang package "
                "inside this directory."
            ),
            justify="center",
        ).pack(pady=20)

    def choose_directory(self):
        directory = filedialog.askdirectory()

        if directory:
            self.install_path.set(
                str(Path(directory) / "orbitlang")
            )

    # ---------------------------------------------------------
    # Installation preview
    # ---------------------------------------------------------

    def show_install_page(self):
        self.create_title(
            "Ready to Install"
        ).pack(pady=(60, 25))

        tk.Label(
            self.container,
            text="OrbitLang will be installed to:",
        ).pack(pady=10)

        tk.Label(
            self.container,
            text=self.install_path.get(),
            font=("TkDefaultFont", 10, "bold"),
            wraplength=600,
        ).pack(pady=10)

        tk.Label(
            self.container,
            text=(
                "\nThe installer will copy the OrbitLang package "
                "and project metadata, then create the `orbit` command."
            ),
            justify="center",
        ).pack(pady=15)

    # ---------------------------------------------------------
    # Installation
    # ---------------------------------------------------------

    def install(self):
        if not self.check_python():
            messagebox.showerror(
                APP_NAME,
                "Python 3.10 or newer is required.",
            )
            return

        destination = Path(
            self.install_path.get()
        ).expanduser()

        if not destination.is_absolute():
            messagebox.showerror(
                APP_NAME,
                "Installation path must be absolute.",
            )
            return

        try:
            destination.mkdir(
                parents=True,
                exist_ok=True,
            )

            self.clear_page()

            self.create_title(
                "Installing OrbitLang..."
            ).pack(pady=(70, 30))

            progress = ttk.Progressbar(
                self.container,
                mode="indeterminate",
                length=450,
            )
            progress.pack(pady=20)

            progress.start(10)

            status = tk.Label(
                self.container,
                text="Copying files...",
            )
            status.pack(pady=10)

            self.root.update()

            self.copy_project(destination)

            status.config(
                text="Installing Python package..."
            )
            self.root.update()

            self.install_package(destination)

            status.config(
                text="Creating launcher..."
            )
            self.root.update()

            self.create_launcher(destination)

            status.config(
                text="Updating PATH..."
            )
            self.root.update()

            self.configure_path(destination)

            progress.stop()

            self.page = 4
            self.show_page()

        except Exception as error:
            messagebox.showerror(
                "Installation Error",
                str(error),
            )

    def copy_project(self, destination):
        package_source = self.project_root / "orbit"

        if not package_source.exists():
            raise RuntimeError(
                "Could not find the OrbitLang package."
            )

        package_destination = destination / "orbit"

        if package_destination.exists():
            shutil.rmtree(package_destination)

        shutil.copytree(
            package_source,
            package_destination,
        )

        pyproject = self.project_root / "pyproject.toml"

        if pyproject.exists():
            shutil.copy2(
                pyproject,
                destination / "pyproject.toml",
            )

        readme = self.project_root / "README.md"

        if readme.exists():
            shutil.copy2(
                readme,
                destination / "README.md",
            )

    def install_package(self, destination):
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                ".",
                "--user",
            ],
            cwd=destination,
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            raise RuntimeError(
                "Could not install OrbitLang.\n\n"
                + result.stderr
            )

    # ---------------------------------------------------------
    # Launcher / PATH
    # ---------------------------------------------------------

    def create_launcher(self, destination):
        bin_directory = Path.home() / ".local" / "bin"
        bin_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        launcher = bin_directory / "orbit"

        launcher_content = f"""#!/bin/sh
exec "{sys.executable}" -m orbit.cli "$@"
"""

        launcher.write_text(
            launcher_content,
            encoding="utf-8",
        )

        launcher.chmod(0o755)

    def configure_path(self, destination):
        if os.name == "nt":
            return

        bin_directory = Path.home() / ".local" / "bin"

        shell = os.environ.get("SHELL", "")

        shell_files = []

        if shell.endswith("zsh"):
            shell_files.append(
                Path.home() / ".zshrc"
            )

        elif shell.endswith("bash"):
            shell_files.append(
                Path.home() / ".bashrc"
            )

        else:
            shell_files.append(
                Path.home() / ".profile"
            )

        path_line = (
            '\n# OrbitLang\n'
            'export PATH="$HOME/.local/bin:$PATH"\n'
        )

        for shell_file in shell_files:
            if shell_file.exists():
                content = shell_file.read_text(
                    encoding="utf-8"
                )

                if "$HOME/.local/bin" not in content:
                    with shell_file.open(
                        "a",
                        encoding="utf-8",
                    ) as file:
                        file.write(path_line)

    # ---------------------------------------------------------
    # Finished
    # ---------------------------------------------------------

    def show_finished(self):
        self.create_title(
            "Installation Complete"
        ).pack(pady=(65, 25))

        tk.Label(
            self.container,
            text="✓ OrbitLang was installed successfully.",
            font=("TkDefaultFont", 12),
        ).pack(pady=15)

        tk.Label(
            self.container,
            text=(
                "Open a new terminal and try:\n\n"
                "orbit repl\n\n"
                "or:\n\n"
                "orbit run your_file.orbit"
            ),
            justify="center",
        ).pack(pady=15)

        self.back_button.config(
            state="disabled"
        )

    # ---------------------------------------------------------
    # Navigation
    # ---------------------------------------------------------

    def next_page(self):
        if self.page == 1 and not self.check_python():
            messagebox.showerror(
                APP_NAME,
                "Python 3.10 or newer is required.",
            )
            return

        if self.page < 4:
            self.page += 1
            self.show_page()

    def previous_page(self):
        if self.page > 0:
            self.page -= 1
            self.show_page()

    def cancel(self):
        answer = messagebox.askyesno(
            APP_NAME,
            "Are you sure you want to cancel the installation?",
        )

        if answer:
            self.root.destroy()

    def finish(self):
        self.root.destroy()


def main():
    root = tk.Tk()

    try:
        ttk.Style().theme_use("clam")
    except tk.TclError:
        pass

    Installer(root)

    root.mainloop()


if __name__ == "__main__":
    main()