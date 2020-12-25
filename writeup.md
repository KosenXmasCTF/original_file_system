まずは仕様書に従って順にバイナリファイルを読んでいく。 
writeup.py というファイルの[35行目](https://github.com/KosenXmasCTF/original_file_system/blob/master/writeup.py#L35)ほどまで読むと、
内部的には1ディレクトリ1ファイルの構造であることがわかる。また、フラグが1なため、ファイル名は暗号化されている。鍵はわかっているのでxorで復号化してファイル名(フラグ)である `xm4s{you_find_a_file_name!}` を入手。
