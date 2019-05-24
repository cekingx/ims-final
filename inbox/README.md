# Engine Inbox

## Deskripsi

Engine yang menerima request dari engine gate kemudian menyimpan ke database

## Bentuk data request

```
{
  "chat_id": 542xxx,
  "in_msg": "lorem ipsum"
  "flag": "0"
}
```

tipe-tipe flag:

- 0 = undefined
- 1 = text
- 2 = file
- 3 = loc
- 4 = img

## Deploy inbox function to Google Cloud Function

```
gcloud functions deploy inbox --runtime python37 --trigger-http --memory=128
```

inbox adalah nama fungsi, bukan nama file
