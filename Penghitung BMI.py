import customtkinter as ctk
from tkinter import messagebox

class BMICalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🏃 Kalkulator BMI, Workout & Meal Planner")
        self.root.geometry("1100x800")
        
        # Set theme
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        # Variables
        self.bmi = None
        self.category = None
        self.workout_key = None
        
        # Data
        self.workout_plans = {
            'underweight': [
                {'day': 'Senin', 'focus': 'Strength Training', 
                 'exercises': ['Push-ups: 3x8', 'Squats: 3x10', 'Plank: 3x30 detik']},
                {'day': 'Rabu', 'focus': 'Upper Body', 
                 'exercises': ['Dumbbell Press: 3x10', 'Bicep Curls: 3x12', 'Shoulder Press: 3x10']},
                {'day': 'Jumat', 'focus': 'Lower Body', 
                 'exercises': ['Lunges: 3x10', 'Leg Raises: 3x12', 'Calf Raises: 3x15']},
                {'day': 'Sabtu', 'focus': 'Core & Cardio', 
                 'exercises': ['Sit-ups: 3x15', 'Mountain Climbers: 3x12', 'Jogging: 20 menit']}
            ],
            'normal': [
                {'day': 'Senin', 'focus': 'Full Body', 
                 'exercises': ['Push-ups: 3x12', 'Squats: 3x15', 'Plank: 3x45 detik']},
                {'day': 'Rabu', 'focus': 'Cardio & Core', 
                 'exercises': ['Running: 30 menit', 'Crunches: 3x20', 'Bicycle Crunches: 3x15']},
                {'day': 'Jumat', 'focus': 'Strength', 
                 'exercises': ['Pull-ups: 3x8', 'Deadlifts: 3x10', 'Dumbbell Rows: 3x12']},
                {'day': 'Minggu', 'focus': 'Active Recovery', 
                 'exercises': ['Yoga: 30 menit', 'Stretching: 15 menit', 'Walking: 30 menit']}
            ],
            'overweight': [
                {'day': 'Senin', 'focus': 'Low Impact Cardio', 
                 'exercises': ['Walking: 30 menit', 'Cycling: 20 menit', 'Stretching: 10 menit']},
                {'day': 'Rabu', 'focus': 'Strength (Light)', 
                 'exercises': ['Wall Push-ups: 3x10', 'Chair Squats: 3x12', 'Arm Circles: 3x15']},
                {'day': 'Jumat', 'focus': 'Cardio', 
                 'exercises': ['Swimming: 30 menit', 'atau Walking: 40 menit', 'Stretching: 10 menit']},
                {'day': 'Sabtu', 'focus': 'Core', 
                 'exercises': ['Modified Plank: 3x20 detik', 'Leg Raises: 3x10', 'Cat-Cow Stretch: 10x']}
            ],
            'obese': [
                {'day': 'Senin', 'focus': 'Gentle Cardio', 
                 'exercises': ['Walking: 20 menit', 'Arm Movements: 10 menit', 'Breathing Exercise: 5 menit']},
                {'day': 'Rabu', 'focus': 'Chair Exercises', 
                 'exercises': ['Seated Marching: 3x30 detik', 'Chair Squats: 2x8', 'Arm Raises: 3x10']},
                {'day': 'Jumat', 'focus': 'Low Impact', 
                 'exercises': ['Water Walking: 25 menit', 'atau Slow Walking: 25 menit', 'Stretching: 10 menit']},
                {'day': 'Minggu', 'focus': 'Flexibility', 
                 'exercises': ['Gentle Yoga: 20 menit', 'Stretching: 15 menit', 'Relaxation: 10 menit']}
            ]
        }
        
        self.meal_plans = {
            'underweight': {
                'breakfast': ['Nasi goreng + telur + alpukat', 'Roti gandum + selai kacang + pisang + susu', 
                            'Oatmeal + kacang almond + madu + buah'],
                'lunch': ['Nasi putih + ayam bakar + sayur + tempe goreng', 'Nasi + ikan + tumis brokoli + tahu', 
                         'Pasta + daging sapi + salad + jus buah'],
                'dinner': ['Nasi + rendang + sayur bayam + pisang', 'Nasi merah + salmon + capcay + yogurt', 
                          'Quinoa + ayam panggang + kentang + buah'],
                'snacks': ['Smoothie pisang + susu + oat', 'Kacang-kacangan + buah kering', 
                          'Roti isi daging + keju', 'Protein shake'],
                'tips': 'Fokus pada makanan tinggi kalori & protein. Makan 5-6x sehari dalam porsi sedang.'
            },
            'normal': {
                'breakfast': ['Oatmeal + buah + kacang', 'Roti gandum + telur + sayuran', 'Nasi merah + ikan + tumis sayur'],
                'lunch': ['Nasi merah + ayam panggang + sayur + buah', 'Quinoa bowl + sayuran + tahu/tempe', 
                         'Nasi + ikan bakar + gado-gado'],
                'dinner': ['Sup ayam + roti gandum + salad', 'Nasi merah + pepes ikan + tumis kangkung', 
                          'Kentang panggang + daging + salad'],
                'snacks': ['Buah segar', 'Yogurt plain + granola', 'Kacang almond', 'Smoothie sayur & buah'],
                'tips': 'Pertahankan pola makan seimbang. Porsi karbohidrat, protein, dan sayur seimbang.'
            },
            'overweight': {
                'breakfast': ['Oatmeal + buah tanpa gula', 'Telur rebus + roti gandum + alpukat', 
                            'Smoothie sayur hijau + pisang'],
                'lunch': ['Nasi merah (porsi kecil) + ikan kukus + banyak sayur', 'Salad ayam panggang + quinoa', 
                         'Sup sayur + tempe/tahu + buah'],
                'dinner': ['Sup ayam + sayuran hijau', 'Ikan bakar + salad + kentang rebus sedikit', 
                          'Pepes tahu + tumis sayur + buah'],
                'snacks': ['Buah potong (apel, pepaya)', 'Kacang rebus', 'Yogurt plain tanpa gula', 'Telur rebus'],
                'tips': 'Kurangi porsi karbohidrat, perbanyak protein & sayur. Hindari gorengan & makanan tinggi gula.'
            },
            'obese': {
                'breakfast': ['Oatmeal + kayu manis (no sugar)', 'Telur rebus 2 butir + sayur', 
                            'Smoothie hijau (bayam, timun, apel)'],
                'lunch': ['Sayur banyak + protein (ikan/ayam rebus) + karbohidrat minimal', 
                         'Salad besar + dada ayam panggang', 'Sup sayur + tahu kukus + buah'],
                'dinner': ['Sayur kukus + ikan bakar', 'Sup bening + tempe panggang + buah', 
                          'Salad + telur rebus + sedikit nasi merah'],
                'snacks': ['Buah rendah kalori (semangka, melon)', 'Timun/wortel potong', 
                          'Teh hijau tanpa gula', 'Air lemon'],
                'tips': 'Fokus pada sayuran & protein tanpa lemak. Minimal karbohidrat. Konsultasi ahli gizi sangat disarankan.'
            }
        }
        
        self.create_widgets()
    
    def create_widgets(self):
        # Header
        header_frame = ctk.CTkFrame(self.root, fg_color=("#3b82f6", "#2563eb"), 
                                   corner_radius=0, height=100)
        header_frame.pack(fill="x", side="top")
        header_frame.pack_propagate(False)
        
        title_label = ctk.CTkLabel(header_frame, 
                                   text="🏃 Kalkulator BMI, Workout & Meal Planner",
                                   font=ctk.CTkFont(size=26, weight="bold"),
                                   text_color="white")
        title_label.pack(pady=30)
        
        # Tab View
        self.tabview = ctk.CTkTabview(self.root, corner_radius=0)
        self.tabview.pack(fill="both", expand=True)
        
        # Create tabs
        self.tabview.add("🧮 Kalkulator BMI")
        self.tabview.add("📊 Hasil & Kategori")
        self.tabview.add("🍽️ Menu Makanan")
        self.tabview.add("💪 Jadwal Workout")
        
        # Set default tab
        self.tabview.set("🧮 Kalkulator BMI")
        
        # Create tab contents
        self.create_calculator_tab()
        self.create_results_tab()
        self.create_meal_tab()
        self.create_workout_tab()
    
    def create_calculator_tab(self):
        tab = self.tabview.tab("🧮 Kalkulator BMI")
        
        # Center frame
        center_frame = ctk.CTkFrame(tab, fg_color="transparent")
        center_frame.pack(expand=True)
        
        # Input Frame
        input_frame = ctk.CTkFrame(center_frame, corner_radius=15, width=500)
        input_frame.pack(padx=40, pady=40)
        
        ctk.CTkLabel(input_frame, text="Masukkan Data Anda",
                    font=ctk.CTkFont(size=20, weight="bold")).pack(pady=(30, 20))
        
        # Weight Input
        weight_frame = ctk.CTkFrame(input_frame, fg_color="transparent")
        weight_frame.pack(pady=15, padx=40, fill="x")
        
        ctk.CTkLabel(weight_frame, text="Berat Badan (kg):",
                    font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", pady=(0, 8))
        
        self.weight_entry = ctk.CTkEntry(weight_frame, width=400, height=45,
                                        font=ctk.CTkFont(size=14),
                                        placeholder_text="Contoh: 70")
        self.weight_entry.pack()
        
        # Height Input
        height_frame = ctk.CTkFrame(input_frame, fg_color="transparent")
        height_frame.pack(pady=15, padx=40, fill="x")
        
        ctk.CTkLabel(height_frame, text="Tinggi Badan (cm):",
                    font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", pady=(0, 8))
        
        self.height_entry = ctk.CTkEntry(height_frame, width=400, height=45,
                                        font=ctk.CTkFont(size=14),
                                        placeholder_text="Contoh: 170")
        self.height_entry.pack()
        
        # Buttons
        button_frame = ctk.CTkFrame(input_frame, fg_color="transparent")
        button_frame.pack(pady=30)
        
        calc_btn = ctk.CTkButton(button_frame, text="🧮 Hitung BMI",
                                font=ctk.CTkFont(size=15, weight="bold"),
                                width=180, height=50,
                                command=self.calculate_bmi)
        calc_btn.pack(side="left", padx=10)
        
        reset_btn = ctk.CTkButton(button_frame, text="🔄 Reset",
                                 font=ctk.CTkFont(size=15, weight="bold"),
                                 width=180, height=50,
                                 fg_color="#6b7280",
                                 hover_color="#4b5563",
                                 command=self.reset)
        reset_btn.pack(side="left", padx=10)
    
    def create_results_tab(self):
        tab = self.tabview.tab("📊 Hasil & Kategori")
        
        # Scrollable frame
        self.results_scroll = ctk.CTkScrollableFrame(tab, fg_color="transparent")
        self.results_scroll.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Placeholder
        self.results_placeholder = ctk.CTkFrame(self.results_scroll, fg_color="transparent")
        self.results_placeholder.pack(expand=True)
        
        ctk.CTkLabel(self.results_placeholder, 
                    text="📊",
                    font=ctk.CTkFont(size=80)).pack(pady=(100, 20))
        
        ctk.CTkLabel(self.results_placeholder,
                    text="Belum ada hasil",
                    font=ctk.CTkFont(size=24, weight="bold"),
                    text_color="gray").pack()
        
        ctk.CTkLabel(self.results_placeholder,
                    text="Silakan hitung BMI Anda terlebih dahulu di tab Kalkulator BMI",
                    font=ctk.CTkFont(size=14),
                    text_color="gray").pack(pady=(10, 0))
    
    def create_meal_tab(self):
        tab = self.tabview.tab("🍽️ Menu Makanan")
        
        # Scrollable frame
        self.meal_scroll = ctk.CTkScrollableFrame(tab, fg_color="transparent")
        self.meal_scroll.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Placeholder
        self.meal_placeholder = ctk.CTkFrame(self.meal_scroll, fg_color="transparent")
        self.meal_placeholder.pack(expand=True)
        
        ctk.CTkLabel(self.meal_placeholder, 
                    text="🍽️",
                    font=ctk.CTkFont(size=80)).pack(pady=(100, 20))
        
        ctk.CTkLabel(self.meal_placeholder,
                    text="Menu makanan belum tersedia",
                    font=ctk.CTkFont(size=24, weight="bold"),
                    text_color="gray").pack()
        
        ctk.CTkLabel(self.meal_placeholder,
                    text="Silakan hitung BMI Anda terlebih dahulu untuk mendapatkan rekomendasi menu",
                    font=ctk.CTkFont(size=14),
                    text_color="gray").pack(pady=(10, 0))
    
    def create_workout_tab(self):
        tab = self.tabview.tab("💪 Jadwal Workout")
        
        # Scrollable frame
        self.workout_scroll = ctk.CTkScrollableFrame(tab, fg_color="transparent")
        self.workout_scroll.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Placeholder
        self.workout_placeholder = ctk.CTkFrame(self.workout_scroll, fg_color="transparent")
        self.workout_placeholder.pack(expand=True)
        
        ctk.CTkLabel(self.workout_placeholder, 
                    text="💪",
                    font=ctk.CTkFont(size=80)).pack(pady=(100, 20))
        
        ctk.CTkLabel(self.workout_placeholder,
                    text="Jadwal workout belum tersedia",
                    font=ctk.CTkFont(size=24, weight="bold"),
                    text_color="gray").pack()
        
        ctk.CTkLabel(self.workout_placeholder,
                    text="Silakan hitung BMI Anda terlebih dahulu untuk mendapatkan jadwal workout",
                    font=ctk.CTkFont(size=14),
                    text_color="gray").pack(pady=(10, 0))
    
    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get()) / 100
            
            if weight <= 0 or height <= 0:
                messagebox.showerror("Error", "Masukkan nilai yang valid!")
                return
            
            self.bmi = weight / (height * height)
            
            # Determine category
            if self.bmi < 18.5:
                self.category = "Kekurangan Berat Badan"
                self.color = "#3b82f6"
                self.workout_key = 'underweight'
            elif 18.5 <= self.bmi < 25:
                self.category = "Normal (Ideal)"
                self.color = "#10b981"
                self.workout_key = 'normal'
            elif 25 <= self.bmi < 30:
                self.category = "Kelebihan Berat Badan"
                self.color = "#f59e0b"
                self.workout_key = 'overweight'
            else:
                self.category = "Obesitas"
                self.color = "#ef4444"
                self.workout_key = 'obese'
            
            # Update all tabs
            self.update_results_tab()
            self.update_meal_tab()
            self.update_workout_tab()
            
            # Switch to results tab
            self.tabview.set("📊 Hasil & Kategori")
            
            messagebox.showinfo("Sukses", "BMI berhasil dihitung! Lihat hasil di tab 'Hasil & Kategori'")
            
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid!")
    
    def update_results_tab(self):
        # Clear placeholder
        if self.results_placeholder:
            self.results_placeholder.destroy()
        
        # Clear previous content
        for widget in self.results_scroll.winfo_children():
            widget.destroy()
        
        # BMI Result
        result_frame = ctk.CTkFrame(self.results_scroll, fg_color=self.color, corner_radius=15)
        result_frame.pack(fill="x", pady=(0, 20))
        
        ctk.CTkLabel(result_frame, text="BMI Anda",
                    font=ctk.CTkFont(size=18),
                    text_color="white").pack(pady=(25, 5))
        
        ctk.CTkLabel(result_frame, text=f"{self.bmi:.1f}",
                    font=ctk.CTkFont(size=64, weight="bold"),
                    text_color="white").pack(pady=5)
        
        ctk.CTkLabel(result_frame, text=self.category,
                    font=ctk.CTkFont(size=20, weight="bold"),
                    text_color="white").pack(pady=(5, 25))
        
        # BMI Categories
        cat_frame = ctk.CTkFrame(self.results_scroll, corner_radius=15)
        cat_frame.pack(fill="x", pady=(0, 20))
        
        ctk.CTkLabel(cat_frame, text="📊 Kategori BMI",
                    font=ctk.CTkFont(size=20, weight="bold")).pack(anchor="w", padx=25, pady=(25, 15))
        
        categories = [
            ("Kekurangan Berat Badan", "< 18.5", "#e0f2fe"),
            ("Normal (Ideal)", "18.5 - 24.9", "#dcfce7"),
            ("Kelebihan Berat Badan", "25.0 - 29.9", "#fef3c7"),
            ("Obesitas", "≥ 30.0", "#fee2e2")
        ]
        
        for name, range_val, bg in categories:
            cat_box = ctk.CTkFrame(cat_frame, fg_color=bg, corner_radius=10)
            cat_box.pack(fill="x", padx=25, pady=8)
            
            content = ctk.CTkFrame(cat_box, fg_color="transparent")
            content.pack(fill="x", padx=20, pady=15)
            
            ctk.CTkLabel(content, text=name, font=ctk.CTkFont(size=14),
                        text_color="#1f2937").pack(side="left")
            ctk.CTkLabel(content, text=range_val, font=ctk.CTkFont(size=14, weight="bold"),
                        text_color="#1f2937").pack(side="right")
        
        cat_frame.pack(pady=(0, 20), padx=0, fill="x")
        
        # Note
        note_frame = ctk.CTkFrame(self.results_scroll, fg_color="#dbeafe", corner_radius=15)
        note_frame.pack(fill="x", pady=(0, 20))
        
        ctk.CTkLabel(note_frame, text="💡 Catatan Penting",
                    font=ctk.CTkFont(size=15, weight="bold"),
                    text_color="#1e40af").pack(anchor="w", padx=25, pady=(20, 8))
        
        ctk.CTkLabel(note_frame,
                    text="Program ini adalah panduan umum. Untuk hasil optimal dan aman, konsultasikan dengan dokter, ahli gizi, atau personal trainer untuk program yang disesuaikan dengan kondisi kesehatan Anda.",
                    font=ctk.CTkFont(size=13),
                    text_color="#1e3a8a",
                    wraplength=900,
                    justify="left").pack(anchor="w", padx=25, pady=(0, 20))
    
    def update_meal_tab(self):
        # Clear placeholder
        if self.meal_placeholder:
            self.meal_placeholder.destroy()
        
        # Clear previous content
        for widget in self.meal_scroll.winfo_children():
            widget.destroy()
        
        meals = self.meal_plans[self.workout_key]
        
        # Header
        ctk.CTkLabel(self.meal_scroll, text="🍽️ Menu Makanan Rekomendasi",
                    font=ctk.CTkFont(size=24, weight="bold")).pack(anchor="w", pady=(0, 20))
        
        meal_types = [
            ("☕ Sarapan", meals['breakfast'], "#fff7ed"),
            ("☀️ Makan Siang", meals['lunch'], "#fef3c7"),
            ("🌙 Makan Malam", meals['dinner'], "#dbeafe"),
            ("🥤 Cemilan Sehat", meals['snacks'], "#fce7f3")
        ]
        
        for title, items, bg in meal_types:
            meal_frame = ctk.CTkFrame(self.meal_scroll, fg_color=bg, corner_radius=15)
            meal_frame.pack(fill="x", pady=(0, 15))
            
            ctk.CTkLabel(meal_frame, text=title,
                        font=ctk.CTkFont(size=18, weight="bold")).pack(anchor="w", padx=25, pady=(20, 12))
            
            for item in items:
                ctk.CTkLabel(meal_frame, text=f"  • {item}",
                            font=ctk.CTkFont(size=13)).pack(anchor="w", padx=25, pady=3)
            
            ctk.CTkLabel(meal_frame, text="").pack(pady=10)
        
        # Tips
        tips_frame = ctk.CTkFrame(self.meal_scroll, fg_color="#dcfce7", corner_radius=15)
        tips_frame.pack(fill="x", pady=(5, 0))
        
        ctk.CTkLabel(tips_frame, text=f"💡 Tips Nutrisi",
                    font=ctk.CTkFont(size=15, weight="bold"),
                    text_color="#065f46").pack(anchor="w", padx=25, pady=(20, 8))
        
        ctk.CTkLabel(tips_frame, text=meals['tips'],
                    font=ctk.CTkFont(size=13),
                    text_color="#064e3b",
                    wraplength=900,
                    justify="left").pack(anchor="w", padx=25, pady=(0, 20))
    
    def update_workout_tab(self):
        # Clear placeholder
        if self.workout_placeholder:
            self.workout_placeholder.destroy()
        
        # Clear previous content
        for widget in self.workout_scroll.winfo_children():
            widget.destroy()
        
        workouts = self.workout_plans[self.workout_key]
        
        # Header
        ctk.CTkLabel(self.workout_scroll, text="💪 Jadwal Workout Rekomendasi",
                    font=ctk.CTkFont(size=24, weight="bold")).pack(anchor="w", pady=(0, 20))
        
        colors = ["#fef3c7", "#dbeafe", "#fce7f3", "#dcfce7"]
        
        for i, workout in enumerate(workouts):
            workout_frame = ctk.CTkFrame(self.workout_scroll, fg_color=colors[i % 4], corner_radius=15)
            workout_frame.pack(fill="x", pady=(0, 15))
            
            ctk.CTkLabel(workout_frame, text=f"📅 {workout['day']}",
                        font=ctk.CTkFont(size=18, weight="bold")).pack(anchor="w", padx=25, pady=(20, 5))
            
            ctk.CTkLabel(workout_frame, text=workout['focus'],
                        font=ctk.CTkFont(size=14, weight="bold"),
                        text_color="#f59e0b").pack(anchor="w", padx=25, pady=(0, 12))
            
            for exercise in workout['exercises']:
                ctk.CTkLabel(workout_frame, text=f"  • {exercise}",
                            font=ctk.CTkFont(size=13)).pack(anchor="w", padx=25, pady=3)
            
            ctk.CTkLabel(workout_frame, text="").pack(pady=10)
        
        # Tips
        tips_frame = ctk.CTkFrame(self.workout_scroll, fg_color="#fde68a", corner_radius=15)
        tips_frame.pack(fill="x", pady=(5, 0))
        
        ctk.CTkLabel(tips_frame, text="⚡ Tips Workout",
                    font=ctk.CTkFont(size=15, weight="bold"),
                    text_color="#92400e").pack(anchor="w", padx=25, pady=(20, 8))
        
        ctk.CTkLabel(tips_frame,
                    text="Mulai dengan intensitas ringan dan tingkatkan bertahap. Pemanasan 5-10 menit sebelum workout!",
                    font=ctk.CTkFont(size=13),
                    text_color="#78350f",
                    wraplength=900,
                    justify="left").pack(anchor="w", padx=25, pady=(0, 20))
    
    def reset(self):
        self.weight_entry.delete(0, 'end')
        self.height_entry.delete(0, 'end')
        self.bmi = None
        self.category = None
        self.workout_key = None
        
        # Reset all tabs to placeholder
        self.create_results_tab()
        self.create_meal_tab()
        self.create_workout_tab()
        
        # Switch to calculator tab
        self.tabview.set("🧮 Kalkulator BMI")

if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    
    root = ctk.CTk()
    app = BMICalculatorApp(root)
    root.mainloop()