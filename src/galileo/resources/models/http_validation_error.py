import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from galileo.resources.models.validation_error import ValidationError

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.validation_error import ValidationError


T = TypeVar("T", bound="HTTPValidationError")


@_attrs_define
class HTTPValidationError:
    """
    Attributes:
        detail (Union[Unset, list['ValidationError']]):
    """

    detail: Union[Unset, list["ValidationError"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        detail: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.detail, Unset):
            detail = []
            for detail_item_data in self.detail:
                detail_item = detail_item_data.to_dict()
                detail.append(detail_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        # Local import for avoid cycle
        from galileo.resources.models.validation_error import ValidationError

        d = src_dict
        _detail = d.get("detail", UNSET)
        if isinstance(_detail, list):
            # List comprehension is always faster in CPython
            detail = [ValidationError.from_dict(item) for item in _detail]
        else:
            detail = UNSET

        # Known keys only 'detail'
        extra = {k: v for k, v in d.items() if k != "detail"}
        http_validation_error = cls(detail=detail)
        http_validation_error.additional_properties = extra  # type: ignore
        return http_validation_error

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
