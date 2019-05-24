# Engine Outbox

## Deskripsi

Engine yang melakukan pengecekan database ketika ada request untuk invoke fungsi dari
cloud scheduler (1 menit). Jika menemukan data dengan flag 1, maka akan dibuatkan request ke gate, kemudian mengeset flag dari data tersebut menjadi 2. Jika data yang ditemukan hanya memiliki flag 2 saja, maka print "Tidak ada pesan untuk dikirim".

## Deploy outbox function to Google Cloud Function

```
gcloud functions deploy outbox --runtime python37 --trigger-http --memory=128
```

outbox adalah nama fungsi, bukan nama file
