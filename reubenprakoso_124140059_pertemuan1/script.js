// Variable State
let keranjang = [];

// DOM Elements - Form Input
const formBarang = document.getElementById("form-barang");
const inputNama = document.getElementById("nama-barang");
const inputHarga = document.getElementById("harga-barang");
const inputQty = document.getElementById("qty-barang");

// DOM Elements - Errors
const errorNama = document.getElementById("error-nama");
const errorHarga = document.getElementById("error-harga");
const errorQty = document.getElementById("error-qty");
const errorBayar = document.getElementById("error-bayar");

// DOM Elements - Table & Summary
const tbodyKeranjang = document.getElementById("tbody-keranjang");
const textTotal = document.getElementById("text-total");
const textDiskon = document.getElementById("text-diskon");
const textTotalAkhir = document.getElementById("text-total-akhir");
const inputKodePromo = document.getElementById("kode-promo");
const inputUangBayar = document.getElementById("uang-bayar");
const textKembalian = document.getElementById("text-kembalian");
const btnReset = document.getElementById("btn-reset");

// Format Rupiah Helper
function formatRupiah(angka) {
    return new Intl.NumberFormat("id-ID", {
        style: "currency",
        currency: "IDR",
        maximumFractionDigits: 0
    }).format(angka);
}

// Inisialisasi Aplikasi dari LocalStorage
function initApp() {
    const savedData = localStorage.getItem("pos_keranjang");
    if (savedData) {
        try {
            keranjang = JSON.parse(savedData);
        } catch (e) {
            keranjang = [];
        }
    }
    renderKeranjang();
}

// Simpan State ke LocalStorage
function saveToLocalStorage() {
    localStorage.setItem("pos_keranjang", JSON.stringify(keranjang));
}

// Clear Error Messages
function clearErrors() {
    errorNama.innerText = "";
    errorHarga.innerText = "";
    errorQty.innerText = "";
    errorBayar.innerText = "";
}

// Validasi Form Input
function validateForm() {
    clearErrors();
    let isValid = true;

    const namaVal = inputNama.value.trim();
    const hargaVal = parseFloat(inputHarga.value);
    const qtyVal = parseInt(inputQty.value, 10);

    // Validasi Nama Barang: minimal 3 karakter
    if (!namaVal || namaVal.length < 3) {
        errorNama.innerText = "Nama barang wajib diisi (minimal 3 karakter).";
        isValid = false;
    }

    // Validasi Harga: minimal Rp 500
    if (isNaN(hargaVal) || hargaVal < 500) {
        errorHarga.innerText = "Harga satuan minimal Rp 500.";
        isValid = false;
    }

    // Validasi Qty: minimal 1
    if (isNaN(qtyVal) || qtyVal < 1) {
        errorQty.innerText = "Jumlah barang minimal 1.";
        isValid = false;
    }

    return isValid;
}

// Tambah Barang ke Keranjang
formBarang.addEventListener("submit", function (e) {
    e.preventDefault();

    if (!validateForm()) return;

    const itemBaru = {
        id: Date.now(),
        nama: inputNama.value.trim(),
        harga: parseFloat(inputHarga.value),
        qty: parseInt(inputQty.value, 10)
    };

    keranjang.push(itemBaru);
    saveToLocalStorage();
    renderKeranjang();

    // Reset Form Input
    formBarang.reset();
    inputQty.value = "1";
    clearErrors();
});

// Hapus Item dari Keranjang
function hapusItem(id) {
    keranjang = keranjang.filter((item) => item.id !== id);
    saveToLocalStorage();
    renderKeranjang();
}

// Hitung Total Belanja & Diskon
function hitungKalkulasi() {
    let totalBelanja = keranjang.reduce((sum, item) => sum + item.harga * item.qty, 0);

    const kodePromoVal = inputKodePromo.value.trim().toUpperCase();
    let diskonPercent = 0;

    // Diskon otomatis 10% jika total >= Rp 50.000 ATAU kode promo "HEMAT10"
    if (totalBelanja >= 50000 || kodePromoVal === "HEMAT10") {
        diskonPercent = 0.1;
    }

    const nominalDiskon = totalBelanja * diskonPercent;
    const totalAkhir = totalBelanja - nominalDiskon;

    // Update Tampilan Ringkasan
    textTotal.innerText = formatRupiah(totalBelanja);
    textDiskon.innerText = formatRupiah(nominalDiskon);
    textTotalAkhir.innerText = formatRupiah(totalAkhir);

    // Hitung Kembalian
    hitungKembalian(totalAkhir);
}

// Hitung Uang Kembalian
function hitungKembalian(totalAkhir) {
    const bayarVal = parseFloat(inputUangBayar.value);
    errorBayar.innerText = "";

    if (isNaN(bayarVal) || inputUangBayar.value === "") {
        textKembalian.innerText = "-";
        textKembalian.className = "";
        return;
    }

    if (bayarVal < totalAkhir) {
        const kurang = totalAkhir - bayarVal;
        textKembalian.innerText = `Uang Kurang (${formatRupiah(kurang)})`;
        textKembalian.className = "text-insufficient";
    } else {
        const kembalian = bayarVal - totalAkhir;
        textKembalian.innerText = formatRupiah(kembalian);
        textKembalian.className = "text-sufficient";
    }
}

// Render Tabel Keranjang & Refresh UI
function renderKeranjang() {
    tbodyKeranjang.innerHTML = "";

    if (keranjang.length === 0) {
        tbodyKeranjang.innerHTML = `
            <tr>
                <td colspan="6" style="text-align: center; color: #94a3b8; padding: 20px;">
                    Keranjang belanja masih kosong.
                </td>
            </tr>
        `;
    } else {
        keranjang.forEach((item, index) => {
            const subtotal = item.harga * item.qty;
            const tr = document.createElement("tr");

            tr.innerHTML = `
                <td>${index + 1}</td>
                <td><strong>${item.nama}</strong></td>
                <td>${formatRupiah(item.harga)}</td>
                <td>${item.qty}</td>
                <td>${formatRupiah(subtotal)}</td>
                <td>
                    <button class="btn btn-danger-sm" onclick="hapusItem(${item.id})">Hapus</button>
                </td>
            `;
            tbodyKeranjang.appendChild(tr);
        });
    }

    hitungKalkulasi();
}

// Event Listeners Tambahan
inputKodePromo.addEventListener("input", hitungKalkulasi);
inputUangBayar.addEventListener("input", () => {
    const totalBelanja = keranjang.reduce((sum, item) => sum + item.harga * item.qty, 0);
    const kodePromoVal = inputKodePromo.value.trim().toUpperCase();
    let diskonPercent = (totalBelanja >= 50000 || kodePromoVal === "HEMAT10") ? 0.1 : 0;
    const totalAkhir = totalBelanja - (totalBelanja * diskonPercent);
    hitungKembalian(totalAkhir);
});

// Reset Transaksi Baru
btnReset.addEventListener("click", () => {
    if (confirm("Apakah Anda yakin ingin mengosongkan keranjang belanja?")) {
        keranjang = [];
        localStorage.removeItem("pos_keranjang");
        inputKodePromo.value = "";
        inputUangBayar.value = "";
        clearErrors();
        renderKeranjang();
    }
});

// Jalankan Inisialisasi
document.addEventListener("DOMContentLoaded", initApp);