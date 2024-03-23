# log/ディレクトリ内のファイルを順に処理する
ls log/ | grep '\.json$' | while IFS= read -r file; do
    # ファイルが.jsonであれば削除する
    rm "log/$file"
    echo "Removed: log/$file"
done

ls log/ | grep '\.mp4$' | while IFS= read -r file; do
    # ファイルが.mp4であれば削除する
    rm "log/$file"
    echo "Removed: log/$file"
done
