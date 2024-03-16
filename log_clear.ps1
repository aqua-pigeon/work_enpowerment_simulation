# log/ディレクトリ内のファイルを順に処理する
Get-ChildItem -Path "log\" -Filter "*.json" | ForEach-Object {
    # ファイルが.jsonであれば削除する
    Remove-Item $_.FullName
    Write-Output "Removed: $($_.FullName)"
}
