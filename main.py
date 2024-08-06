import tkinter as tk
from tkinter import messagebox
import sqlite3

# Veritabanı bağlantısı
conn = sqlite3.connect('game_results.db')
c = conn.cursor()

# Veritabanı tabloları oluşturma
c.execute('''CREATE TABLE IF NOT EXISTS games
             (game_id INTEGER PRIMARY KEY, player1 TEXT, player2 TEXT, player1_gold INTEGER, player2_gold INTEGER, round INTEGER)''')
c.execute('''CREATE TABLE IF NOT EXISTS rounds
             (game_id INTEGER, round INTEGER, player1_move TEXT, player2_move TEXT, player1_gold INTEGER, player2_gold INTEGER)''')

conn.commit()

# Karakter sınıfları
class Oyuncu:
    def __init__(self, name):
        self.name = name
        self.gold = 10
        self.move = None
        self.last_opponent_move = None
        self.history = []

    def karar_ver(self):
        pass

class Kopyacı(Oyuncu):
    def karar_ver(self):
        if not self.history:
            self.move = 'ver'
        else:
            self.move = self.last_opponent_move

class Ponçik(Oyuncu):
    def karar_ver(self):
        self.move = 'ver'

class Çakal(Oyuncu):
    def karar_ver(self):
        self.move = 'alma'

class Gözükara(Oyuncu):
    def karar_ver(self):
        if 'alma' in self.history:
            self.move = 'alma'
        else:
            self.move = 'ver'

class Sinsi(Oyuncu):
    def karar_ver(self):
        if len(self.history) < 2:
            self.move = 'ver'
        elif len(self.history) == 2:
            self.move = 'alma'
        elif len(self.history) == 3:
            self.move = 'ver'
        else:
            if self.history[3] == 'ver':
                self.move = 'alma'
            else:
                self.move = 'ver'


# Oyuncu oluşturma fonksiyonu
def oyuncu_olustur(name, oyuncu_turu):
    if oyuncu_turu == "Kopyacı":
        return Kopyacı(name)
    elif oyuncu_turu == "Ponçik":
        return Ponçik(name)
    elif oyuncu_turu == "Çakal":
        return Çakal(name)
    elif oyuncu_turu == "Gözükara":
        return Gözükara(name)
    elif oyuncu_turu == "Sinsi":
        return Sinsi(name)

# Oyun sınıfı
class Oyun:
    def __init__(self, oyuncu1, oyuncu2):
        self.oyuncu1 = oyuncu1
        self.oyuncu2 = oyuncu2
        self.round = 0
        self.oyun_id = self.save_oyun_start()

    def save_oyun_start(self):
        c.execute('INSERT INTO games (player1, player2, player1_gold, player2_gold, round) VALUES (?, ?, ?, ?, ?)',
                  (self.oyuncu1.name, self.oyuncu2.name, self.oyuncu1.gold, self.oyuncu2.gold, self.round))
        conn.commit()
        return c.lastrowid

    def round_oyna(self):
        self.round += 1
        self.oyuncu1.karar_ver()
        self.oyuncu2.karar_ver()

        o1_move = self.oyuncu1.move
        o2_move = self.oyuncu2.move

        if o1_move == 'ver' and o2_move == 'ver':
            self.oyuncu1.gold += 2
            self.oyuncu2.gold += 2
        elif o1_move == 'ver' and o2_move == 'alma':
            self.oyuncu1.gold -= 1
            self.oyuncu2.gold += 3
        elif o1_move == 'alma' and o2_move == 'ver':
            self.oyuncu1.gold += 3
            self.oyuncu2.gold -= 1

        self.oyuncu1.history.append(o2_move)
        self.oyuncu2.history.append(o1_move)
        self.oyuncu1.last_opponent_move = o2_move
        self.oyuncu2.last_opponent_move = o1_move

        self.save_round()

    def save_round(self):
        c.execute('INSERT INTO rounds (game_id, round, player1_move, player2_move, player1_gold, player2_gold) VALUES (?, ?, ?, ?, ?, ?)',
                  (self.oyun_id, self.round, self.oyuncu1.move, self.oyuncu2.move, self.oyuncu1.gold, self.oyuncu2.gold))
        conn.commit()

# Tkinter GUI

class OyunGUI:
    def __init__(self, master):
        self.master = master
        master.title("Altın Oyunu")
        master.geometry("400x300")
        master.configure(bg="#f0f0f0")

        self.oyuncu1_label = tk.Label(master, text="1. Oyuncu Karakter Seçimi:", font=("Helvetica", 12), bg="#f0f0f0")
        self.oyuncu1_label.pack(pady=5)

        self.oyuncu1_var = tk.StringVar(master)
        self.oyuncu1_var.set("Kopyacı")
        self.oyuncu1_menu = tk.OptionMenu(master, self.oyuncu1_var, "Kopyacı", "Ponçik", "Çakal", "Gözükara", "Sinsi")
        self.oyuncu1_menu.pack(pady=5)

        self.oyuncu2_label = tk.Label(master, text="2. Oyuncu Karakter Seçimi:", font=("Helvetica", 12), bg="#f0f0f0")
        self.oyuncu2_label.pack(pady=5)

        self.oyuncu2_var = tk.StringVar(master)
        self.oyuncu2_var.set("Kopyacı")
        self.oyuncu2_menu = tk.OptionMenu(master, self.oyuncu2_var, "Kopyacı", "Ponçik", "Çakal", "Gözükara", "Sinsi")
        self.oyuncu2_menu.pack(pady=5)

        self.start_button = tk.Button(master, text="Oyunu Başlat", command=self.oyun_baslat, font=("Helvetica", 12))
        self.start_button.pack(pady=10)

        self.round_button = tk.Button(master, text="1. Tura Başla", state='disabled', command=self.round_oyna, font=("Helvetica", 12))
        self.round_button.pack(pady=10)

        self.sonuc_label = tk.Label(master, text="", font=("Helvetica", 12), bg="#f0f0f0")
        self.sonuc_label.pack(pady=10)

        self.oyun = None

    def oyun_baslat(self):
        oyuncu1_turu = self.oyuncu1_var.get()
        oyuncu2_turu = self.oyuncu2_var.get()
        self.oyuncu1 = oyuncu_olustur("Oyuncu 1", oyuncu1_turu)
        self.oyuncu2 = oyuncu_olustur("Oyuncu 2", oyuncu2_turu)

        # Daha önce oynandı mı kontrolü
        c.execute('SELECT * FROM games WHERE player1 = ? AND player2 = ? OR player1 = ? AND player2 = ?', 
                  (self.oyuncu1.name, self.oyuncu2.name, self.oyuncu2.name, self.oyuncu1.name))
        if c.fetchone():
            response = messagebox.askyesno("Dikkat", "Bu karakterler daha önce karşı karşıya geldi. Yine de başlatmak istiyor musunuz?")
            if not response:
                return
        
        self.oyun = Oyun(self.oyuncu1, self.oyuncu2)
        self.round_button.config(state='normal')
        self.sonuc_label.config(text="Oyun başladı!")

    def round_oyna(self):
        self.oyun.round_oyna()
        o1_gold = self.oyun.oyuncu1.gold
        o2_gold = self.oyun.oyuncu2.gold
        o1_move = self.oyun.oyuncu1.move
        o2_move = self.oyun.oyuncu2.move

        self.sonuc_label.config(text=f"1. Oyuncu: {o1_gold} altın ({o1_move}), 2. Oyuncu: {o2_gold} altın ({o2_move})")

        if self.oyun.round < 10:
            self.round_button.config(text=f"{self.oyun.round + 1}. Tura Başla")
        else:
            self.round_button.config(state='disabled')
            messagebox.showinfo("Oyun Bitti", f"Oyun bitti! 1. Oyuncu: {o1_gold} altın, 2. Oyuncu: {o2_gold} altın.")

root = tk.Tk()
gui = OyunGUI(root)
root.mainloop()

conn.close()
