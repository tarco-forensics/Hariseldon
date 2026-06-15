$lines = Get-Content "B:\Hariseldon\dashboards\betting_analyzer.html"
for($i=0; $i -lt $lines.Length; $i++) {
    $l = $lines[$i]
    if ($l -match 'Pipeline|pipeline|Form.*l|Overround|overround|Ingestion|Normalize') {
        Write-Output "$(($i+1)): $l"
    }
}
