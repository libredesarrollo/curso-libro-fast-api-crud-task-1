from schemes import StatusType

taskWithOutORM = {
    "normal1": {
        "summary":"A normal example 1",
        "description":"A normal example",
        "value":{
            "id" : 123,
            "name": "Salvar al mundo",
            "description": "Hola Mundo Desc",
            "status": StatusType.PENDING,
            "tag":["tag 1", "tag 2"],
            "category": {
                "id":1234,
                "name":"Cate 1"
            },
            "user": {
                "id":12,
                "name":"Andres",
                "email":"admin@admin.com",
                "surname":"Cruz",
                "website":"http://desarrollolibre.net",
            }
        }
    },
    "normal2":{
        "summary":"A normal example 2",
        "description":"A normal example",
        "value":{
            "id" : 12,
            "name": "Sacar la basura",
            "description": "Hola Mundo Desc",
            "status": StatusType.PENDING,
            "tag":["tag 1"],
            "category_id": {
                "id":1,
                "name":"Cate 1"
            },
            "user": {
                "id":12,
                "name":"Andres",
                "email":"admin@admin.com",
                "surname":"Cruz",
                "website":"http://desarrollolibre.net",
            }
        }
    },
    "invalid":{
        "summary":"A invalid example 1",
        "description":"A invalid example",
        "value":{
            "id" : 12,
            "name": "Sacar la basura",
            "description": "Hola Mundo Desc",
            "status": StatusType.PENDING,
            "tag":["tag 1"],
            "user": {
                "id":12,
                "name":"Andres",
                "email":"admin@admin.com",
                "surname":"Cruz",
                "website":"http://desarrollolibre.net",
            }
        }
    }
}

taskWithORM = {
    "normal1": {
        "summary":"A normal example 1",
        "description":"A normal example",
        "value":{
            "id" : 123,
            "name": "Salvar al mundo",
            "description": "Hola Mundo Desc",
            "status": StatusType.PENDING,
            "tag":["tag 1", "tag 2"],
            "category_id": 1,
            "user_id": 1
        }
    },
    "normal2":{
        "summary":"A normal example 2",
        "description":"A normal example",
        "value":{
            "id" : 12,
            "name": "Sacar la basura",
            "description": "Hola Mundo Desc",
            "status": StatusType.PENDING,
            "tag":["tag 1"],
            "category":2,
            "user_id": 1
        }
    },
    "invalid":{
        "summary":"A invalid example 1",
        "description":"A invalid example",
        "value":{
            "id" : 12,
            "name": "Sacar la basura",
            "description": "Hola Mundo Desc",
            "status": StatusType.PENDING,
            "tag":["tag 1"],
            "user_id": {
                "id":12,
                "name":"Andres",
                "email":"admin@admin.com",
                "surname":"Cruz",
                "website":"http://desarrollolibre.net",
            }
        }
    }
}