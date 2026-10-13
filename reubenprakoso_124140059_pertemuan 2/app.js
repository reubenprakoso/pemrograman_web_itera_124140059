// ==========================================
// 1. CLASS: TaskItem (Memodelkan struktur data)
// ==========================================
class TaskItem {
    constructor(id, text, category, completed = false) {
        this.id = id;
        this.text = text;
        this.category = category;
        this.completed = completed;
        this.createdAt = new Date().toLocaleDateString('id-ID', { 
            day: 'numeric', 
            month: 'short', 
            year: 'numeric' 
        });
    }
}

// ==========================================
// 2. CLASS: DashboardApp (Mengelola state & aksi)
// ==========================================
class DashboardApp {
    constructor() {
        this.tasks = [];
        this.init();
    }

    // Inisialisasi Aplikasi
    async init() {
        this.loadFromLocalStorage();
        this.setupEventListeners();
        this.renderTasks();
        
        // Memanggil Async Functions untuk API Publik secara paralel
        await this.fetchWeatherData();
        await this.fetchRandomQuote();
    }

    // Mengambil data dari localStorage
    loadFromLocalStorage() {
        const storedTasks = localStorage.getItem('itera_dashboard_tasks');
        if (storedTasks) {
            // Destructuring parameter objek di dalam map untuk instansiasi class
            this.tasks = JSON.parse(storedTasks).map(
                ({ id, text, category, completed }) => 
                new TaskItem(id, text, category, completed)
            );
        } else {
            // Data awal default simulasi
            this.tasks = [
                new TaskItem(1, 'Laporan Praktikum Pemrograman Web', 'Praktikum', false),
                new TaskItem(2, 'Commit GitHub repository Siskom', 'Tugas', true)
            ];
            this.saveToLocalStorage();
        }
    }

    // Menyimpan data ke localStorage
    saveToLocalStorage() {
        localStorage.setItem('itera_dashboard_tasks', JSON.stringify(this.tasks));
    }

    // Event Listener Form Submit & Modal Edit
    setupEventListeners() {
        const form = document.getElementById('task-form');
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const input = document.getElementById('task-input');
            const categorySelect = document.getElementById('task-category');
            
            this.addTask(input.value, categorySelect.value);
            input.value = '';
        });

        // Event listener untuk form edit di modal
        const editForm = document.getElementById('edit-form');
        editForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const id = Number(document.getElementById('edit-id').value);
            const newText = document.getElementById('edit-input').value;
            const newCategory = document.getElementById('edit-category').value;

            this.updateTask(id, newText, newCategory);
            this.closeEditModal();
        });

        // Tombol batal edit
        document.getElementById('cancel-edit').addEventListener('click', () => {
            this.closeEditModal();
        });
    }

    // Menambah Task (Immutable update menggunakan Spread Operator)
    addTask(text, category) {
        const newTask = new TaskItem(Date.now(), text, category);
        this.tasks = [newTask, ...this.tasks];
        this.saveToLocalStorage();
        this.renderTasks();
    }

    // Menghapus Task berdasarkan ID
    deleteTask(id) {
        this.tasks = this.tasks.filter(task => task.id !== id);
        this.saveToLocalStorage();
        this.renderTasks();
    }

    // Mengubah Status Selesai Task (Toggle Completed)
    toggleTaskStatus(id) {
        this.tasks = this.tasks.map(task => {
            if (task.id === id) {
                // Menggunakan spread operator untuk immutability
                return { ...task, completed: !task.completed };
            }
            return task;
        });
        this.saveToLocalStorage();
        this.renderTasks();
    }

    // Membuka modal edit dan mengisi data awal
    openEditModal(id) {
        const taskToEdit = this.tasks.find(task => task.id === id);
        if (!taskToEdit) return;

        document.getElementById('edit-id').value = taskToEdit.id;
        document.getElementById('edit-input').value = taskToEdit.text;
        document.getElementById('edit-category').value = taskToEdit.category;

        document.getElementById('edit-modal').classList.add('active');
    }

    // Menutup modal edit
    closeEditModal() {
        document.getElementById('edit-modal').classList.remove('active');
    }

    // Memperbarui data Task yang diedit
    updateTask(id, newText, newCategory) {
        this.tasks = this.tasks.map(task => {
            if (task.id === id) {
                return { ...task, text: newText, category: newCategory };
            }
            return task;
        });
        this.saveToLocalStorage();
        this.renderTasks();
    }

    // Arrow Function 1: Render daftar tugas ke DOM menggunakan Template Literals
    renderTasks = () => {
        const taskListContainer = document.getElementById('task-list');
        
        if (this.tasks.length === 0) {
            taskListContainer.innerHTML = `
                <p class="empty-state">Belum ada tugas atau catatan tersimpan.</p>
            `;
            return;
        }

        taskListContainer.innerHTML = this.tasks.map(({ id, text, category, completed, createdAt }) => `
            <div class="task-item ${completed ? 'completed' : ''}">
                <div class="task-left">
                    <input 
                        type="checkbox" 
                        onclick="app.toggleTaskStatus(${id})" 
                        ${completed ? 'checked' : ''}
                        class="task-checkbox"
                    >
                    <div>
                        <p class="task-text">${text}</p>
                        <div class="task-meta">
                            <span class="badge">${category}</span>
                            <span class="date-text">${createdAt}</span>
                        </div>
                    </div>
                </div>
                <div class="task-actions">
                    <button 
                        onclick="app.openEditModal(${id})" 
                        class="edit-btn"
                    >
                        Edit
                    </button>
                    <button 
                        onclick="app.deleteTask(${id})" 
                        class="delete-btn"
                    >
                        Hapus
                    </button>
                </div>
            </div>
        `).join('');
    };

    // Arrow Function 2: Async Await untuk Mengambil Cuaca Real-time Open-Meteo (Lokasi ITERA, Lampung Selatan)
    fetchWeatherData = async () => {
        const weatherWidget = document.getElementById('weather-widget');
        try {
            const response = await fetch('https://api.open-meteo.com/v1/forecast?latitude=-5.36&longitude=105.31&current_weather=true');
            const data = await response.json();
            
            // Destructuring data cuaca
            const { temperature } = data.current_weather;
            
            weatherWidget.innerHTML = `
                <span>📍 ITERA: <strong>${temperature}°C</strong> (Cerah/Berawan)</span>
            `;
        } catch (error) {
            console.error('Gagal memuat cuaca:', error);
            weatherWidget.innerHTML = `<span>⚠️ Gagal memuat cuaca lokal</span>`;
        }
    };

    // Arrow Function 3: Async Await untuk Mengambil Kutipan Acak dari DummyJSON Quotes
    fetchRandomQuote = async () => {
        const quoteContainer = document.getElementById('quote-container');
        try {
            const response = await fetch('https://dummyjson.com/quotes/random');
            const data = await response.json();
            
            // Destructuring quote & author
            const { quote, author } = data;
            quoteContainer.innerHTML = `&ldquo;${quote}&rdquo;<br><span style="display: block; font-size: 0.75rem; font-weight: 600; margin-top: 0.25rem; color: #065f46;">— ${author}</span>`;
        } catch (error) {
            console.error('Gagal memuat kutipan:', error);
            quoteContainer.innerHTML = `"Tetap semangat menjalani hari perkuliahan di kampus tercinta."`;
        }
    }
}

// Inisialisasi Global Instance Aplikasi
const app = new DashboardApp();