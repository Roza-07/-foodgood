import tkinter as tk
from tkinter import ttk, messagebox
from producti import get_all_products, get_calories, search_products
from calculator import calculate

class CalorieApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Счетчик Калорий")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.configure(bg='#f0f0f0')
        
        #Заголовок
        title = tk.Label(root, text="Счетчик калорий", 
                         font=("Arial", 18, "bold"), 
                         bg='#f0f0f0', fg='#333333')
        title.pack(pady=15)
      
        self.status = tk.Label(root, text="Готов к работе", 
                               bd=1, relief=tk.SUNKEN, anchor=tk.W,
                               bg='#e0e0e0', fg='#555555')
        self.status.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        #Расчёт
        self.tab_calc = tk.Frame(self.notebook, bg='#f0f0f0')
        self.notebook.add(self.tab_calc, text="Расчёт")
        self.setup_calc_tab()
        
        #Список продуктов
        self.tab_list = tk.Frame(self.notebook, bg='#f0f0f0')
        self.notebook.add(self.tab_list, text="Список продуктов")
        self.setup_list_tab()
        
        #Поиск
        self.tab_search = tk.Frame(self.notebook, bg='#f0f0f0')
        self.notebook.add(self.tab_search, text="Поиск")
        self.setup_search_tab()
    
    def setup_calc_tab(self):
        #Рамка для формы
        frame = tk.Frame(self.tab_calc, bg='#f0f0f0')
        frame.pack(pady=40)
        
        #Продукт
        tk.Label(frame, text="Продукт:", font=("Arial", 12), 
                 bg='#f0f0f0', fg='#333333').grid(row=0, column=0, pady=10, sticky='e')
        self.product_entry = tk.Entry(frame, width=25, font=("Arial", 12))
        self.product_entry.grid(row=0, column=1, pady=10, padx=10)
        self.product_entry.bind('<Return>', lambda e: self.calculate())
        
        #Вес
        tk.Label(frame, text="Вес (граммы):", font=("Arial", 12), 
                 bg='#f0f0f0', fg='#333333').grid(row=1, column=0, pady=10, sticky='e')
        self.weight_entry = tk.Entry(frame, width=25, font=("Arial", 12))
        self.weight_entry.grid(row=1, column=1, pady=10, padx=10)
        self.weight_entry.bind('<Return>', lambda e: self.calculate())
        
        #Кнопка рассчитать
        self.calc_btn = tk.Button(frame, text="Рассчитать", 
                                   command=self.calculate,
                                   bg='#4CAF50', fg='white', 
                                   font=("Arial", 12), padx=20, pady=5)
        self.calc_btn.grid(row=2, column=0, columnspan=2, pady=20)
        
        #Результат
        self.result_label = tk.Label(self.tab_calc, text="", 
                                      font=("Arial", 14, "bold"), 
                                      bg='#f0f0f0', fg='#2196F3')
        self.result_label.pack(pady=20)
    
    def setup_list_tab(self):
        #Рамка с прокруткой
        frame = tk.Frame(self.tab_list, bg='#f0f0f0')
        frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.list_text = tk.Text(frame, yscrollcommand=scrollbar.set, 
                                  font=("Courier", 10), bg='white', fg='#333333')
        self.list_text.pack(fill='both', expand=True)
        scrollbar.config(command=self.list_text.yview)
        
        #Кнопка обновления
        refresh_btn = tk.Button(self.tab_list, text="Обновить список", 
                                 command=self.refresh_list,
                                 bg='#2196F3', fg='white', 
                                 font=("Arial", 10), padx=10, pady=5)
        refresh_btn.pack(pady=10)
        
        #Загружаем список
        self.refresh_list()
    
    def setup_search_tab(self):
        frame = tk.Frame(self.tab_search, bg='#f0f0f0')
        frame.pack(pady=40)
        
        tk.Label(frame, text="Поиск продукта:", font=("Arial", 12), 
                 bg='#f0f0f0', fg='#333333').grid(row=0, column=0, pady=10)
        
        self.search_entry = tk.Entry(frame, width=30, font=("Arial", 12))
        self.search_entry.grid(row=0, column=1, pady=10, padx=10)
        self.search_entry.bind('<Return>', lambda e: self.search())
        
        search_btn = tk.Button(frame, text="Найти", 
                                command=self.search,
                                bg='#FF9800', fg='white', 
                                font=("Arial", 10), padx=15, pady=5)
        search_btn.grid(row=0, column=2, pady=10)
        
        #Результаты поиска
        self.search_result = tk.Text(self.tab_search, height=15, width=50, 
                                      font=("Courier", 10), bg='white', fg='#333333')
        self.search_result.pack(pady=20, padx=20)
    
    def calculate(self):
        product = self.product_entry.get()
        weight_str = self.weight_entry.get()
        
        if not product or not weight_str:
            messagebox.showwarning("Ошибка", "Заполните оба поля")
            return
        
        try:
            weight = float(weight_str)
        except ValueError:
            messagebox.showwarning("Ошибка", "Вес должен быть числом")
            return
        
        calories, error = calculate(product, weight)
        
        if error:
            messagebox.showwarning("Ошибка", error)
            self.result_label.config(text="")
        else:
            self.result_label.config(text=f"{product} ({weight} г) = {calories} ккал")
            self.status.config(text=f"Последний расчёт: {product} - {calories} ккал")
    
    def refresh_list(self):
        self.list_text.delete(1.0, tk.END)
        products = get_all_products()
        
        self.list_text.insert(tk.END, "="*35 + "\n")
        self.list_text.insert(tk.END, " Продукт              ккал/100г\n")
        self.list_text.insert(tk.END, "="*35 + "\n")
        
        for product in products:
            kcal = get_calories(product)
            self.list_text.insert(tk.END, f" {product:<20} {kcal:>6}\n")
        
        self.status.config(text=f"Загружено {len(products)} продуктов")
    
    def search(self):
        query = self.search_entry.get()
        
        if not query:
            messagebox.showwarning("Ошибка", "Введите поисковый запрос")
            return
        
        self.search_result.delete(1.0, tk.END)
        results = search_products(query)
        
        if not results:
            self.search_result.insert(tk.END, "Ничего не найдено")
            self.status.config(text=f"Поиск: '{query}' - ничего не найдено")
        else:
            self.search_result.insert(tk.END, "="*35 + "\n")
            self.search_result.insert(tk.END, " Продукт              ккал/100г\n")
            self.search_result.insert(tk.END, "="*35 + "\n")
            
            for name, kcal in results:
                self.search_result.insert(tk.END, f" {name:<20} {kcal:>6}\n")
            
            self.status.config(text=f"Найдено {len(results)} продуктов по запросу '{query}'")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalorieApp(root)
    root.mainloop()  