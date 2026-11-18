param(
    [ValidateSet("all", "mahasiswa", "matakuliah")]
    [string]$Resource = "all"
)

$ErrorActionPreference = "Stop"
$BaseUrl = "http://127.0.0.1:6543"

function Invoke-Api {
    param(
        [Parameter(Mandatory = $true)][string]$Label,
        [Parameter(Mandatory = $true)][ValidateSet("GET", "POST", "PUT", "DELETE")][string]$Method,
        [Parameter(Mandatory = $true)][string]$Path,
        [object]$Body = $null,
        [Parameter(Mandatory = $true)][int]$ExpectedStatus
    )

    Write-Host "`n=== $Label ===" -ForegroundColor Cyan
    $curlArgs = @("-sS", "-X", $Method, "-w", "`n__STATUS__%{http_code}")
    $payloadFile = $null
    if ($null -ne $Body) {
        $jsonBody = $Body | ConvertTo-Json -Compress -Depth 8
        $payloadFile = Join-Path $env:TEMP ("pyramid-api-" + [guid]::NewGuid().ToString("N") + ".json")
        [System.IO.File]::WriteAllText(
            $payloadFile,
            $jsonBody,
            [System.Text.UTF8Encoding]::new($false)
        )
        $curlArgs += @(
            "-H",
            "Content-Type: application/json",
            "--data-binary",
            ("@" + $payloadFile)
        )
    }
    $curlArgs += "$BaseUrl$Path"

    try {
        $rawOutput = (& curl.exe @curlArgs | Out-String).TrimEnd()
    }
    finally {
        if ($payloadFile -and (Test-Path $payloadFile)) {
            Remove-Item $payloadFile -Force
        }
    }
    if ($LASTEXITCODE -ne 0) {
        throw "curl.exe gagal untuk $Method $Path. Pastikan server Pyramid berjalan."
    }

    $marker = "`n__STATUS__"
    $markerIndex = $rawOutput.LastIndexOf($marker)
    if ($markerIndex -lt 0) {
        throw "Status HTTP tidak ditemukan untuk $Method $Path."
    }

    $responseBody = $rawOutput.Substring(0, $markerIndex).Trim()
    $statusText = $rawOutput.Substring($markerIndex + $marker.Length).Trim()
    $statusCode = [int]$statusText
    Write-Host "HTTP $statusCode"

    $responseObject = $null
    if ($responseBody) {
        try {
            $responseObject = $responseBody | ConvertFrom-Json
            Write-Host ($responseObject | ConvertTo-Json -Depth 8)
        }
        catch {
            Write-Host $responseBody
        }
    }

    if ($statusCode -ne $ExpectedStatus) {
        throw "Status untuk $Method $Path adalah $statusCode; diharapkan $ExpectedStatus."
    }
    return $responseObject
}

function Test-MahasiswaApi {
    Write-Host "`n######## API MAHASISWA ########" -ForegroundColor Green
    Invoke-Api "Daftar mahasiswa" GET "/api/mahasiswa" -ExpectedStatus 200 | Out-Null

    $uniqueSuffix = Get-Date -Format "yyyyMMddHHmmss"
    $nim = "TEST$uniqueSuffix"
    $created = Invoke-Api "Tambah mahasiswa" POST "/api/mahasiswa" -Body @{
        nim = $nim
        nama = "Dewi Lestari"
        jurusan = "Teknik Informatika"
        tanggal_lahir = "2002-06-10"
        alamat = "Bandar Lampung"
    } -ExpectedStatus 201
    $itemId = $created.mahasiswa.id

    Invoke-Api "Detail mahasiswa" GET "/api/mahasiswa/$itemId" -ExpectedStatus 200 | Out-Null
    Invoke-Api "Ubah mahasiswa" PUT "/api/mahasiswa/$itemId" -Body @{
        jurusan = "Teknik Informatika"
    } -ExpectedStatus 200 | Out-Null
    Invoke-Api "Validasi field wajib mahasiswa" POST "/api/mahasiswa" -Body @{
        nama = "Tanpa NIM"
        jurusan = "Teknik Informatika"
    } -ExpectedStatus 400 | Out-Null
    Invoke-Api "Hapus mahasiswa" DELETE "/api/mahasiswa/$itemId" -ExpectedStatus 200 | Out-Null
    Invoke-Api "Pastikan mahasiswa terhapus" GET "/api/mahasiswa/$itemId" -ExpectedStatus 404 | Out-Null
}

function Test-MatakuliahApi {
    Write-Host "`n######## API MATAKULIAH ########" -ForegroundColor Green
    Invoke-Api "Daftar matakuliah" GET "/api/matakuliah" -ExpectedStatus 200 | Out-Null

    $uniqueSuffix = Get-Date -Format "yyMMddHHmmss"
    $kodeMk = "T$uniqueSuffix"
    $created = Invoke-Api "Tambah matakuliah" POST "/api/matakuliah" -Body @{
        kode_mk = $kodeMk
        nama_mk = "Pengujian API Pyramid"
        sks = 3
        semester = 5
    } -ExpectedStatus 201
    $itemId = $created.matakuliah.id

    Invoke-Api "Detail matakuliah" GET "/api/matakuliah/$itemId" -ExpectedStatus 200 | Out-Null
    Invoke-Api "Ubah matakuliah" PUT "/api/matakuliah/$itemId" -Body @{
        sks = 4
        semester = 6
    } -ExpectedStatus 200 | Out-Null
    Invoke-Api "Validasi SKS positif" POST "/api/matakuliah" -Body @{
        kode_mk = "INVALID$uniqueSuffix"
        nama_mk = "Data tidak valid"
        sks = 0
        semester = 3
    } -ExpectedStatus 400 | Out-Null
    Invoke-Api "Hapus matakuliah" DELETE "/api/matakuliah/$itemId" -ExpectedStatus 200 | Out-Null
    Invoke-Api "Pastikan matakuliah terhapus" GET "/api/matakuliah/$itemId" -ExpectedStatus 404 | Out-Null
}

if ($Resource -in @("all", "mahasiswa")) {
    Test-MahasiswaApi
}
if ($Resource -in @("all", "matakuliah")) {
    Test-MatakuliahApi
}

Write-Host "`nSemua pengujian $Resource berhasil." -ForegroundColor Green
