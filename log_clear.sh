# log/ディレクトリ内のファイルを順に処理する
ls log/ | grep '\.json$' | while IFS= read -r file; do
    # ファイルが.jsonであれば削除する
    rm "log/$file"
    echo "Removed: log/$file"
done