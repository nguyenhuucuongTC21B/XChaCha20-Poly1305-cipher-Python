# XChaCha20-Poly1305-cipher-Python
XChaCha20-Poly1305 cipher Python


Stream cipher simple application for 2022 year which uses XChaCha20-Poly1305
Ứng dụng mã hóa dòng đơn giản cho năm 2022 sử dụng XChaCha20-Poly1305

Sử dụng mật mã XChaCha20-Poly1305 cung cấp:

    Toàn vẹn dữ liệu
    Mã hóa xác thực
    Bảo mật
    Cho phép xử lý luồng
    nhanh hơn gấp ba lần so với AES trên các nền tảng thiếu phần cứng AES chuyên dụng
    Khóa 256 bit
    192-bit nonce giảm xác suất sử dụng sai nonce


1. Rationale

Lack of ready to use simple application for encryption with modern cipher.
2. Installation

    Installed Python 3.6 or higher is required.
    Type in the console pip3 install cipher21.

3. Usage Guide

    
    thông số chi tiết mô tả:cipher21 -h
    cipher21 chỉ hỗ trợ 64 khóa thập lục phân mà bạn có thể tạo thông qua:
        > python -c "from os import urandom; print(urandom(32).hex())" > key.hex
        https://www.random.org/integers/?num=8&min=0&max=65535&col=8&base=16&format=html&rnd=new
    mã hóa tệp bằng khóa hex tìm nạp từ tệp:cipher21 -e -k file:key.hex < plain.txt > encrypted.c21
    mã hóa tệp bằng tìm nạp khóa hex từ env:cipher21 -e -k env:KEY64 < plain.txt > encrypted.c21
    giải mã tệp với tìm nạp khóa hex từ tệp:cipher21 -d -k file:key.hex < encrypted.c21 > plain.txt
    nén và mã hóa:mysqldump --all-databases | xz -zc | cipher21 -e -k file:key.hex > db-dump.sql.xz.c21
    giải mã và giải nén:cat db-dump.sql.xz.c21 | cipher21 -d -k file:key.hex | xz -dc | mysql


4. Recommended Designations

    .c21 is a recommended file name extension
    application/cipher21 ia a recommended internet media type

5. Technical details
5.1. Stream Structure

    Độ dài luồng phải luôn là bội số của M == 2 ^ 14 == 16384 byte để ẩn độ dài chính xác của trọng tải..

 offset | len | description
--------+-----+---------------------------------------------------
      0 |   8 | stream signature: "c21\x1A\x00\xFF\x19\x82"
      8 |  24 | nonce
     32 |   E | XChaCha20-Poly1305 encrypted block (see below)
    -16 |  16 | MAC

constraints:
(8 + 24 + E + 16) % M == 0   =>   E % M == M - 48 == 16336

5.2. Encrypted Block

 offset | len | description
--------+-----+---------------------------------------------
      0 |   8 | little endian unsigned integer of an encryption time in nanoseconds
        |     | since the January 1, 1970, 00:00:00 (UTC), not counting leap seconds
      8 |   D | payload
 -2 - P |   P | randomized padding bytes
     -2 |   2 | little endian unsigned integer P - the padding length

constraints:
(8 + D + P + 2) % M == M - 48
    => (D + P) % M == M - 58
    => P % M == (M - 58 - D) % M
    => P == (2*M - 58 - (D % M)) % M
