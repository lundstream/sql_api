$apiBase = "http://192.168.1.20:8011"

# MSSQL credentials
$body = @{
    server   = "192.168.1.20,1433"  # or your SQL Server IP/hostname
    database = "TestDB"
    username = "sa"
    password = "password" # Change this
} | ConvertTo-Json


$response = Invoke-RestMethod -Uri "$apiBase/connect" -Method Post -Body $body -ContentType "application/json"

if ($response.status -eq "connected") {
    Write-Host "Connected. Tables:"
    $response.tables
} else {
    Write-Host "Connection failed: $($response.detail)"
}

$tableName = "Products"
$tableData = Invoke-RestMethod -Uri "$apiBase/tables/$tableName" -Method Post -Body $body -ContentType "application/json"

# Show the results
$tableData | Format-Table
