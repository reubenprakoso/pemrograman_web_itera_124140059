// Latihan Modul Pertemuan 1 - JavaScript Dasar

// 1. Variabel dan Output
const nama = "Reuben Prakoso";
let nim = "124140059";
let nilai = 85;

console.log("Nama: " + nama);
console.log("NIM: " + nim);

document.getElementById("result").innerHTML = `
  <p>Nama: <strong>${nama}</strong></p>
  <p>NIM: <strong>${nim}</strong></p>
`;

// 2. Kondisional (Grade)
let grade = "";
if (nilai >= 80) {
  grade = "A";
} else if (nilai >= 70) {
  grade = "B";
} else {
  grade = "C";
}

document.getElementById("result").innerHTML += `
  <p>Nilai: <strong>${nilai}</strong> (Grade: <strong>${grade}</strong>)</p>
`;