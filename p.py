import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
from datetime import datetime
from tkinter import filedialog

class Barang:
    def __init__(self, kode, nama, harga, stok=0, kategori="", created_at=None):
        self.kode = kode
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.kategori = kategori
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class InventarisMinimarket:
    def __init__(self):
        self.daftar_barang = []
        self.load_data()

    def cek_kode_duplikat(self, kode):
        return any(barang.kode == kode for barang in self.daftar_barang)

    def tambah_barang(self, kode, nama, harga, stok=0, kategori=""):
        if self.cek_kode_duplikat(kode):
            return False, "Kode barang sudah ada"
        
        barang_baru = Barang(kode, nama, harga, stok, kategori)
        self.daftar_barang.append(barang_baru)
        self.save_data()
        return True, f"Barang '{nama}' berhasil ditambahkan"

    def cari_barang(self, keyword):
        return [barang for barang in self.daftar_barang 
                if keyword.lower() in barang.nama.lower() 
                or keyword.lower() in barang.kode.lower()]

    def save_data(self):
        """Rekomendasi 1: Penyimpanan data persistent menggunakan JSON"""
        try:
            data = []
            for barang in self.daftar_barang:
                data.append({
                    'kode': barang.kode,
                    'nama': barang.nama,
                    'harga': barang.harga,
                    'stok': barang.stok,
                    'kategori': barang.kategori,
                    'created_at': barang.created_at
                })
            
            with open('data_inventaris.json', 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self):
        """Rekomendasi 1: Load data dari JSON"""
        try:
            if os.path.exists('data_inventaris.json'):
                with open('data_inventaris.json', 'r') as f:
                    data = json.load(f)
                    for item in data:
                        self.daftar_barang.append(Barang(
                            item['kode'],
                            item['nama'],
                            item['harga'],
                            item.get('stok', 0),
                            item.get('kategori', ''),
                            item.get('created_at')
                        ))
        except Exception as e:
            print(f"Error loading data: {e}")

    def export_to_csv(self):
        """Rekomendasi 2: Ekspor data ke CSV"""
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
            )
            if filename:
                with open(filename, 'w') as f:
                    f.write("Kode,Nama,Harga,Stok,Kategori,Tanggal Input\n")
                    for barang in self.daftar_barang:
                        f.write(f'"{barang.kode}","{barang.nama}",{barang.harga},{barang.stok},"{barang.kategori}","{barang.created_at}"\n')
                return True, f"Data berhasil diekspor ke {filename}"
        except Exception as e:
            return False, f"Error exporting data: {e}"

class LoginSystem:
    """Rekomendasi 3: Sistem login dan autentikasi"""
    def __init__(self):
        self.users = {
            'sudo': {'password': 'admin123', 'role': 'admin'},
            'karyawan': {'password': 'jangankoson', 'role': 'kasir'}
        }

    def authenticate(self, username, password):
        if username in self.users and self.users[username]['password'] == password:
            return True, self.users[username]['role']
        return False, None

class BarangGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Inventaris Minimarket - Enhanced")
        self.root.geometry("800x600")
        
        # Rekomendasi 3: Sistem login
        self.login_system = LoginSystem()
        self.current_user = None
        self.user_role = None
        
        self.inventaris = InventarisMinimarket()
        self.show_login_screen()

    def show_login_screen(self):
        """Rekomendasi 3: Form login"""
        self.clear_screen()
        
        login_frame = ttk.Frame(self.root, padding="20")
        login_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        ttk.Label(login_frame, text="Login Sistem Inventaris", 
                 font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
        
        ttk.Label(login_frame, text="Username:").grid(row=1, column=0, sticky="w", pady=5)
        self.username_entry = ttk.Entry(login_frame, width=20)
        self.username_entry.grid(row=1, column=1, pady=5)
        
        ttk.Label(login_frame, text="Password:").grid(row=2, column=0, sticky="w", pady=5)
        self.password_entry = ttk.Entry(login_frame, width=20, show="*")
        self.password_entry.grid(row=2, column=1, pady=5)
        
        ttk.Button(login_frame, text="Login", 
                  command=self.do_login).grid(row=3, column=0, columnspan=2, pady=10)
        

    def do_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        success, role = self.login_system.authenticate(username, password)
        if success:
            self.current_user = username
            self.user_role = role
            messagebox.showinfo("Success", f"Login berhasil sebagai {role}")
            self.setup_main_ui()
        else:
            messagebox.showerror("Error", "Username atau password salah")

    def setup_main_ui(self):
        self.clear_screen()
        
        # Header dengan info user
        header_frame = ttk.Frame(self.root, padding="10")
        header_frame.pack(fill="x")
        
        ttk.Label(header_frame, text=f"Sistem Inventaris Minimarket", 
                 font=('Arial', 16, 'bold')).pack(side="left")
        
        ttk.Label(header_frame, text=f"User: {self.current_user} ({self.user_role})", 
                 foreground="blue").pack(side="right")
        
        # Notebook untuk tabs (Rekomendasi 4: Multiple features)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Tab 1: Kelola Barang
        self.setup_kelola_tab()
        
        # Tab 2: Cari Barang (Rekomendasi 5: Fitur pencarian)
        self.setup_cari_tab()
        
        # Tab 3: Laporan (Rekomendasi 6: Reporting)
        self.setup_laporan_tab()
        
        # Tab 4: Backup (Hanya untuk admin)
        if self.user_role == 'admin':
            self.setup_backup_tab()

    def setup_kelola_tab(self):
        kelola_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(kelola_frame, text="Kelola Barang")
        
        # Input frame
        input_frame = ttk.LabelFrame(kelola_frame, text="Tambah Barang Baru", padding="10")
        input_frame.pack(fill="x", pady=5)
        
        # Form input dengan lebih banyak field
        fields = [
            ("Kode Barang*:", "kode_entry"),
            ("Nama Barang*:", "nama_entry"), 
            ("Harga Rp*:", "harga_entry"),
            ("Stok:", "stok_entry"),
            ("Kategori:", "kategori_entry")
        ]
        
        for i, (label, attr_name) in enumerate(fields):
            ttk.Label(input_frame, text=label).grid(row=i, column=0, sticky="w", padx=5, pady=5)
            entry = ttk.Entry(input_frame, width=25)
            entry.grid(row=i, column=1, padx=5, pady=5)
            setattr(self, attr_name, entry)
        
        # Tombol aksi
        btn_frame = ttk.Frame(input_frame)
        btn_frame.grid(row=len(fields), column=0, columnspan=2, pady=10)
        
        ttk.Button(btn_frame, text="Tambah Barang", 
                  command=self.tambah_barang).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Clear Form", 
                  command=self.clear_form).pack(side="left", padx=5)
        
        # Daftar barang dengan Treeview (Rekomendasi 7: Tabel yang lebih baik)
        list_frame = ttk.LabelFrame(kelola_frame, text="Daftar Barang", padding="10")
        list_frame.pack(fill="both", expand=True, pady=5)
        
        columns = ("Kode", "Nama", "Harga", "Stok", "Kategori", "Tanggal")
        self.treeview = ttk.Treeview(list_frame, columns=columns, show="headings", height=15)
        
        for col in columns:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, width=100)
        
        self.treeview.pack(fill="both", expand=True)
        
        # Scrollbar untuk treeview
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        
        self.refresh_data()

    def setup_cari_tab(self):
        """Rekomendasi 5: Fitur pencarian lanjutan"""
        cari_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(cari_frame, text="Cari Barang")
        
        # Search box
        search_frame = ttk.Frame(cari_frame)
        search_frame.pack(fill="x", pady=5)
        
        ttk.Label(search_frame, text="Kata kunci:").pack(side="left", padx=5)
        self.search_entry = ttk.Entry(search_frame, width=30)
        self.search_entry.pack(side="left", padx=5)
        ttk.Button(search_frame, text="Cari", 
                  command=self.cari_barang).pack(side="left", padx=5)
        
        # Results treeview
        self.search_tree = ttk.Treeview(cari_frame, 
                                       columns=("Kode", "Nama", "Harga", "Stok", "Kategori"),
                                       show="headings", height=10)
        for col in ("Kode", "Nama", "Harga", "Stok", "Kategori"):
            self.search_tree.heading(col, text=col)
        self.search_tree.pack(fill="both", expand=True, pady=5)

    def setup_laporan_tab(self):
        """Rekomendasi 6: Sistem laporan"""
        laporan_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(laporan_frame, text="Laporan")
        
        # Statistik
        stats_frame = ttk.LabelFrame(laporan_frame, text="Statistik Inventaris", padding="10")
        stats_frame.pack(fill="x", pady=5)
        
        self.stats_label = ttk.Label(stats_frame, text="", font=('Arial', 10))
        self.stats_label.pack(anchor="w")
        
        # Tombol export
        ttk.Button(laporan_frame, text="Export ke CSV", 
                  command=self.export_data).pack(pady=10)
        
        self.update_stats()

    def setup_backup_tab(self):
        """Rekomendasi 8: Backup data (admin only)"""
        backup_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(backup_frame, text="Backup Data")
        
        ttk.Label(backup_frame, text="Fitur Backup & Restore Data", 
                 font=('Arial', 12, 'bold')).pack(pady=10)
        
        ttk.Button(backup_frame, text="Backup Data ke CSV", 
                  command=self.export_data).pack(pady=5)
        
        ttk.Button(backup_frame, text="Restore Data", 
                  command=self.restore_data).pack(pady=5)

    def tambah_barang(self):
        # Validasi input
        kode = self.kode_entry.get().strip().upper()
        nama = self.nama_entry.get().strip().title()
        harga = self.harga_entry.get().strip()
        stok = self.stok_entry.get().strip() or "0"
        kategori = self.kategori_entry.get().strip()
        
        if not all([kode, nama, harga]):
            messagebox.showerror("Error", "Field bertanda * harus diisi!")
            return
        
        if not harga.isdigit():
            messagebox.showerror("Error", "Harga harus berupa angka!")
            return
        
        if not stok.isdigit():
            messagebox.showerror("Error", "Stok harus berupa angka!")
            return
        
        # Tambahkan barang
        success, message = self.inventaris.tambah_barang(kode, nama, int(harga), int(stok), kategori)
        
        if success:
            messagebox.showinfo("Success", message)
            self.clear_form()
            self.refresh_data()
            self.update_stats()
        else:
            messagebox.showerror("Error", message)

    def cari_barang(self):
        keyword = self.search_entry.get().strip()
        if not keyword:
            messagebox.showwarning("Peringatan", "Masukkan kata kunci pencarian")
            return
        
        results = self.inventaris.cari_barang(keyword)
        
        # Clear previous results
        for item in self.search_tree.get_children():
            self.search_tree.delete(item)
        
        # Add new results
        for barang in results:
            self.search_tree.insert("", "end", values=(
                barang.kode, barang.nama, f"Rp {barang.harga:,}", 
                barang.stok, barang.kategori
            ))

    def export_data(self):
        success, message = self.inventaris.export_to_csv()
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)

    def restore_data(self):
        # Implementasi restore data dari backup
        messagebox.showinfo("Info", "Fitur restore dalam pengembangan")

    def refresh_data(self):
        # Refresh treeview data
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        
        for barang in self.inventaris.daftar_barang:
            self.treeview.insert("", "end", values=(
                barang.kode, barang.nama, f"Rp {barang.harga:,}", 
                barang.stok, barang.kategori, barang.created_at
            ))

    def update_stats(self):
        total_barang = len(self.inventaris.daftar_barang)
        total_nilai = sum(barang.harga * barang.stok for barang in self.inventaris.daftar_barang)
        kategori_count = len(set(barang.kategori for barang in self.inventaris.daftar_barang if barang.kategori))
        
        stats_text = f"""Total Barang: {total_barang}
Total Nilai Inventaris: Rp {total_nilai:,}
Jumlah Kategori: {kategori_count}"""
        
        self.stats_label.config(text=stats_text)

    def clear_form(self):
        self.kode_entry.delete(0, tk.END)
        self.nama_entry.delete(0, tk.END)
        self.harga_entry.delete(0, tk.END)
        self.stok_entry.delete(0, tk.END)
        self.kategori_entry.delete(0, tk.END)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BarangGUI(root)
    root.mainloop()