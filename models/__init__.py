""" Models Module """
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
cls_list = ["BaseModel"]
cls_attr =
{
    "BaseModel":
    {
        "id": str,
        "created_at": datetime.datetime,
        "updated_at": datetime.datetime
    },
}
