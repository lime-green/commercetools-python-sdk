from commercetools.platform import models


def test_non_equality():
    obj = models.Message.deserialize(
        {
            "id": "174adf2f-783f-4ce5-a2d5-ee7d3ee7caf4",
            "version": 1,
            "sequenceNumber": 1,
            "resource": {
                "typeId": "category",
                "id": "45251684-d693-409d-9864-f93f486adb95",
            },
            "resourceVersion": 1,
            "type": "CategoryCreated",
            "category": {
                "id": "45251684-d693-409d-9864-f93f486adb95",
                "version": 1,
                "name": {"en": "myCategory"},
                "slug": {"en": "my-category"},
                "ancestors": [],
                "orderHint": "0.000014556311799451762128695",
                "createdAt": "2016-02-16T13:59:39.945Z",
                "lastModifiedAt": "2016-02-16T13:59:39.945Z",
                "assets": [],
                "lastMessageSequenceNumber": 1,
            },
            "createdAt": "2016-02-16T13:59:39.945Z",
            "lastModifiedAt": "2016-02-16T13:59:39.945Z",
        }
    )
    assert isinstance(obj, models.CategoryCreatedMessage)
