import tkinter as tk
from tkinter import ttk, messagebox
import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature


class CryptoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CryptoGuard - Hash & Digital Signature Analyzer")
        self.root.geometry("1050x720")
        self.root.minsize(900, 650)

        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.public_key = self.private_key.public_key()
        self.signature = None
        self.original_sha256 = ""
        self.original_sha512 = ""

        self.setup_style()
        self.build_ui()

    def setup_style(self):
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure("Title.TLabel", font=("Segoe UI", 24, "bold"))
        style.configure("Subtitle.TLabel", font=("Segoe UI", 11))
        style.configure("Card.TLabelframe", padding=14)
        style.configure("Card.TLabelframe.Label", font=("Segoe UI", 12, "bold"))
        style.configure("Accent.TButton", font=("Segoe UI", 11, "bold"), padding=10)
        style.configure("Normal.TButton", font=("Segoe UI", 10), padding=8)

    def build_ui(self):
        header = ttk.Frame(self.root, padding=(24, 18))
        header.pack(fill="x")

        ttk.Label(header, text="🔐 CryptoGuard",
                  style="Title.TLabel").pack(anchor="w")
        ttk.Label(
            header,
            text="Cryptographic Hash Algorithms & RSA Digital Signature Analyzer",
            style="Subtitle.TLabel"
        ).pack(anchor="w", pady=(4, 0))

        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=20, pady=(0, 15))

        self.hash_tab = ttk.Frame(notebook, padding=18)
        self.verify_tab = ttk.Frame(notebook, padding=18)
        self.about_tab = ttk.Frame(notebook, padding=18)

        notebook.add(self.hash_tab, text="  Hash & Sign  ")
        notebook.add(self.verify_tab, text="  Verify Modification  ")
        notebook.add(self.about_tab, text="  About Project  ")

        self.build_hash_tab()
        self.build_verify_tab()
        self.build_about_tab()

        footer = ttk.Label(
            self.root,
            text="Assignment 5 • SHA-256 • SHA-512 • RSA Digital Signature",
            anchor="center"
        )
        footer.pack(fill="x", pady=(0, 8))

    def build_hash_tab(self):
        input_card = ttk.LabelFrame(
            self.hash_tab, text="1. Enter Original Message",
            style="Card.TLabelframe"
        )
        input_card.pack(fill="x", pady=(0, 12))

        self.message_text = tk.Text(
            input_card, height=5, font=("Consolas", 11), wrap="word"
        )
        self.message_text.pack(fill="x", padx=4, pady=4)
        self.message_text.insert("1.0", "Transfer amount: 5000")

        buttons = ttk.Frame(input_card)
        buttons.pack(fill="x", pady=(8, 0))
        ttk.Button(
            buttons, text="Generate Hashes & RSA Signature",
            command=self.generate, style="Accent.TButton"
        ).pack(side="left")
        ttk.Button(
            buttons, text="Clear", command=self.clear_all,
            style="Normal.TButton"
        ).pack(side="left", padx=8)

        result = ttk.LabelFrame(
            self.hash_tab, text="2. Cryptographic Results",
            style="Card.TLabelframe"
        )
        result.pack(fill="both", expand=True)

        grid = ttk.Frame(result)
        grid.pack(fill="both", expand=True)

        ttk.Label(grid, text="SHA-256 Hash",
                  font=("Segoe UI", 10, "bold")).grid(
            row=0, column=0, sticky="w", pady=(0, 4))
        self.sha256_var = tk.StringVar(value="—")
        ttk.Entry(grid, textvariable=self.sha256_var,
                  state="readonly", font=("Consolas", 9)).grid(
            row=1, column=0, sticky="ew", padx=(0, 12), pady=(0, 14))

        ttk.Label(grid, text="SHA-512 Hash",
                  font=("Segoe UI", 10, "bold")).grid(
            row=2, column=0, sticky="w", pady=(0, 4))
        self.sha512_var = tk.StringVar(value="—")
        ttk.Entry(grid, textvariable=self.sha512_var,
                  state="readonly", font=("Consolas", 8)).grid(
            row=3, column=0, sticky="ew", padx=(0, 12), pady=(0, 14))

        ttk.Label(grid, text="RSA Digital Signature",
                  font=("Segoe UI", 10, "bold")).grid(
            row=4, column=0, sticky="w", pady=(0, 4))
        self.signature_text = tk.Text(
            grid, height=5, font=("Consolas", 8), wrap="char"
        )
        self.signature_text.grid(row=5, column=0, sticky="nsew")

        self.status_var = tk.StringVar(value="Status: Waiting for input")
        ttk.Label(
            grid, textvariable=self.status_var,
            font=("Segoe UI", 11, "bold")
        ).grid(row=6, column=0, sticky="w", pady=(12, 0))

        grid.columnconfigure(0, weight=1)
        grid.rowconfigure(5, weight=1)

    def build_verify_tab(self):
        card = ttk.LabelFrame(
            self.verify_tab, text="Test Message Integrity",
            style="Card.TLabelframe"
        )
        card.pack(fill="x", pady=(0, 15))

        ttk.Label(
            card,
            text="Enter a message after changing the original content.\n"
                 "The RSA signature was created for the original message."
        ).pack(anchor="w", pady=(0, 8))

        self.modified_text = tk.Text(
            card, height=5, font=("Consolas", 11), wrap="word"
        )
        self.modified_text.pack(fill="x")
        self.modified_text.insert("1.0", "Transfer amount: 9000")

        ttk.Button(
            card, text="Verify Modified Message",
            command=self.verify_modified, style="Accent.TButton"
        ).pack(anchor="w", pady=10)

        result = ttk.LabelFrame(
            self.verify_tab, text="Verification Result",
            style="Card.TLabelframe"
        )
        result.pack(fill="both", expand=True)

        self.verify_title = ttk.Label(
            result, text="No verification performed",
            font=("Segoe UI", 20, "bold")
        )
        self.verify_title.pack(anchor="center", pady=(30, 15))

        self.verify_details = tk.Text(
            result, height=12, font=("Consolas", 10),
            wrap="word", state="disabled"
        )
        self.verify_details.pack(fill="both", expand=True, padx=10, pady=10)

    def build_about_tab(self):
        frame = ttk.Frame(self.about_tab, padding=25)
        frame.pack(fill="both", expand=True)

        ttk.Label(
            frame, text="Assignment 5",
            font=("Segoe UI", 20, "bold")
        ).pack(anchor="w")

        text = (
            "\nEvaluation of Cryptographic Hash Algorithms and Digital Signature Schemes\n\n"
            "This application demonstrates:\n"
            "• SHA-256 message hashing\n"
            "• SHA-512 message hashing\n"
            "• RSA-2048 digital signature generation\n"
            "• Signature verification\n"
            "• Effect of modifying the original message\n"
            "• Integrity and authentication observation\n\n"
            "Recommended demonstration:\n"
            "Original:  Transfer amount: 5000\n"
            "Modified:  Transfer amount: 9000\n\n"
            "Expected result:\n"
            "Original signature verification → VALID\n"
            "Modified message verification → INVALID\n"
        )
        ttk.Label(
            frame, text=text, justify="left",
            font=("Segoe UI", 12)
        ).pack(anchor="w")

    def generate(self):
        message = self.message_text.get("1.0", "end-1c").strip()
        if not message:
            messagebox.showwarning("Input Required", "Please enter a message.")
            return

        data = message.encode("utf-8")
        self.original_sha256 = hashlib.sha256(data).hexdigest()
        self.original_sha512 = hashlib.sha512(data).hexdigest()

        self.sha256_var.set(self.original_sha256)
        self.sha512_var.set(self.original_sha512)

        self.signature = self.private_key.sign(
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        self.signature_text.delete("1.0", "end")
        self.signature_text.insert("1.0", self.signature.hex())

        valid = self.verify_signature(message)
        self.status_var.set(
            "Status: ✓ Original signature is VALID"
            if valid else
            "Status: ✗ Original signature is INVALID"
        )

        self.verify_title.config(text="Original message signed successfully")
        self.set_verify_details(
            "Original message:\n" + message +
            "\n\nSHA-256:\n" + self.original_sha256 +
            "\n\nSHA-512:\n" + self.original_sha512 +
            "\n\nRSA signature generated successfully."
        )

    def verify_signature(self, message):
        if self.signature is None:
            return False
        try:
            self.public_key.verify(
                self.signature,
                message.encode("utf-8"),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except InvalidSignature:
            return False

    def verify_modified(self):
        if self.signature is None:
            messagebox.showwarning(
                "Generate Signature First",
                "Go to the Hash & Sign tab and generate the signature first."
            )
            return

        modified = self.modified_text.get("1.0", "end-1c").strip()
        if not modified:
            messagebox.showwarning(
                "Input Required", "Please enter a modified message."
            )
            return

        data = modified.encode("utf-8")
        modified_sha256 = hashlib.sha256(data).hexdigest()
        modified_sha512 = hashlib.sha512(data).hexdigest()
        valid = self.verify_signature(modified)

        if valid:
            self.verify_title.config(text="✓ SIGNATURE VALID")
        else:
            self.verify_title.config(text="✗ SIGNATURE INVALID")

        details = (
            "Modified message:\n" + modified +
            "\n\nOriginal SHA-256:\n" + self.original_sha256 +
            "\n\nModified SHA-256:\n" + modified_sha256 +
            "\n\nOriginal SHA-512:\n" + self.original_sha512 +
            "\n\nModified SHA-512:\n" + modified_sha512 +
            "\n\nVerification result: " +
            ("VALID" if valid else "INVALID") +
            "\n\nObservation:\n"
        )

        if not valid:
            details += (
                "The modified message does not match the message for which "
                "the RSA signature was generated. The hash also changes, "
                "demonstrating message integrity and authentication."
            )
        else:
            details += "The signature remains valid for this message."

        self.set_verify_details(details)

    def set_verify_details(self, text):
        self.verify_details.config(state="normal")
        self.verify_details.delete("1.0", "end")
        self.verify_details.insert("1.0", text)
        self.verify_details.config(state="disabled")

    def clear_all(self):
        self.message_text.delete("1.0", "end")
        self.modified_text.delete("1.0", "end")
        self.sha256_var.set("—")
        self.sha512_var.set("—")
        self.signature_text.delete("1.0", "end")
        self.status_var.set("Status: Waiting for input")
        self.verify_title.config(text="No verification performed")
        self.set_verify_details("")
        self.signature = None


if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoApp(root)
    root.mainloop()
