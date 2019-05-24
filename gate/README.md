# Engine Gate

## Bentuk json

Dari engine outbox

```
{
  "update_id: 999,
  "from_outbox": true,
  "chat": {
    "id": 372880228,
    "tipe": "loc"
  }
}
```

Dari bot type msg

```
{
  "update_id": 518409044,
  "message": {
    "message_id": 119,
    "from": {
      "id": 372880228,
      "is_bot": false,
      "first_name": "Dirga",
      "last_name": "Yasa",
      "username": "cekingx",
      "language_code": "id"
    },
    "chat": {
      "id": 372880228,
      "first_name": "Dirga",
      "last_name": "Yasa",
      "username": "cekingx",
      "type": "private",
      "photo": null,
      "pinned_message": null
    },
    "date": 1557203925,
    "text": "Pesan"

  }
```

Dari bot type file

```
{
  "update_id": 518409042,
  "message": {
    "message_id": 115,
    "from": {
      "id": 372880228,
      "is_bot": false,
      "first_name": "Dirga",
      "last_name": "Yasa",
      "username": "cekingx",
      "language_code": "en"
    },
    "chat": {
      "id": 372880228,
      "first_name": "Dirga",
      "last_name": "Yasa",
      "username": "cekingx",
      "type": "private",
      "photo": null,
      "pinned_message": null
    },
    "date": 1557203862,
    "document": {
      "file_name": "Instruction.pdf",
      "mime_type": "application/pdf",
      "file_id": "BQADBQADbwADENOQVqoud5DwqE6QAg",
      "file_size": 6149
    }
  }
}
```

Dari bot type loc

```
{
  "update_id": 518409043,
  "message": {
    "message_id": 117,
    "from": {
      "id": 372880228,
      "is_bot": false,
      "first_name": "Dirga",
      "last_name": "Yasa",
      "username": "cekingx",
      "language_code": "id"
    },
    "chat": {
      "id": 372880228,
      "first_name": "Dirga",
      "last_name": "Yasa",
      "username": "cekingx",
      "type": "private",
      "photo": null,
      "pinned_message": null
    },
    "date": 1557203908,
    "location": { "latitude": -8.799618, "longitude": 115.172838 }
  }
}
```

Dari bot type img

```
{
  "update_id": 518409045,
  "message": {
    "message_id": 121,
    "from": {
      "id": 372880228,
      "is_bot": false,
      "first_name": "Dirga",
      "last_name": "Yasa",
      "username": "cekingx",
      "language_code": "id"
    },
    "chat": {
      "id": 372880228,
      "first_name": "Dirga",
      "last_name": "Yasa",
      "username": "cekingx",
      "type": "private",
      "photo": null,
      "pinned_message": null
    },
    "date": 1557203954,
    "photo": [
      {
        "file_id": "AgADBQADq6gxGxDTkFabwMPFv8bXdJZL9jIABPIVOK8xJ-cqDEEDAAEC",
        "file_size": 1114,
        "width": 51,
        "height": 90
      },
      {
        "file_id": "AgADBQADq6gxGxDTkFabwMPFv8bXdJZL9jIABMt24IprSlXXDUEDAAEC",
        "file_size": 12756,
        "width": 180,
        "height": 320
      },
      {
        "file_id": "AgADBQADq6gxGxDTkFabwMPFv8bXdJZL9jIABCZ_sZ4oe8PYC0EDAAEC",
        "file_size": 58046,
        "width": 450,
        "height": 800
      },
      {
        "file_id": "AgADBQADq6gxGxDTkFabwMPFv8bXdJZL9jIABH3UOzRPw_29CkEDAAEC",
        "file_size": 103582,
        "width": 720,
        "height": 1280
      }
    ]
  }
}
```

## Deploy gate function to Google Cloud Function

```
gcloud functions deploy gate --runtime python37 --trigger-http --memory=128
```

gate adalah nama fungsi, bukan nama file
