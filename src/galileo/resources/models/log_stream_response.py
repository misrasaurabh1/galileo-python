import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LogStreamResponse")


@_attrs_define
class LogStreamResponse:
    """
    Attributes:
        created_at (datetime.datetime):
        id (str):
        name (str):
        project_id (str):
        updated_at (datetime.datetime):
        created_by (Union[None, Unset, str]):
    """

    created_at: datetime.datetime
    id: str
    name: str
    project_id: str
    updated_at: datetime.datetime
    created_by: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        name = self.name

        project_id = self.project_id

        updated_at = self.updated_at.isoformat()

        created_by: Union[None, Unset, str]
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {"created_at": created_at, "id": id, "name": name, "project_id": project_id, "updated_at": updated_at}
        )
        if created_by is not UNSET:
            field_dict["created_by"] = created_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        # Avoid copying the dict, just access each field directly
        d = src_dict

        created_at = _fast_isoparse(d["created_at"])
        id = d["id"]
        name = d["name"]
        project_id = d["project_id"]
        updated_at = _fast_isoparse(d["updated_at"])
        created_by = _parse_created_by(d.get("created_by", UNSET))

        # Build using fields, and for extra fields use a dict comprehension
        known_keys = {"created_at", "id", "name", "project_id", "updated_at", "created_by"}
        # Extract the additional properties directly
        extra = {k: v for k, v in d.items() if k not in known_keys}

        log_stream_response = cls(
            created_at=created_at, id=id, name=name, project_id=project_id, updated_at=updated_at, created_by=created_by
        )
        log_stream_response.additional_properties = extra  # type: ignore
        return log_stream_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties


# Fast ISO format parse falls back to dateutil only if strictly needed
def _fast_isoparse(s: str) -> datetime.datetime:
    try:
        return datetime.datetime.fromisoformat(s.replace("Z", "+00:00"))
    except Exception:
        from dateutil.parser import isoparse

        return isoparse(s)


def _parse_created_by(data: object) -> Union[None, Unset, str]:
    # Fast path, branch quickly
    if data is None or isinstance(data, Unset) or isinstance(data, str):
        return data
    return cast(Union[None, Unset, str], data)
