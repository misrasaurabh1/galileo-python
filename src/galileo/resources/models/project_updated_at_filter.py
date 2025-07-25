import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.project_updated_at_filter_operator import ProjectUpdatedAtFilterOperator
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectUpdatedAtFilter")


@_attrs_define
class ProjectUpdatedAtFilter:
    """
    Attributes:
        operator (ProjectUpdatedAtFilterOperator):
        value (datetime.datetime):
        name (Union[Literal['updated_at'], Unset]):  Default: 'updated_at'.
    """

    operator: ProjectUpdatedAtFilterOperator
    value: datetime.datetime
    name: Union[Literal["updated_at"], Unset] = "updated_at"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operator = self.operator.value

        value = self.value.isoformat()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({"operator": operator, "value": value})
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operator = ProjectUpdatedAtFilterOperator(d.pop("operator"))

        value = isoparse(d.pop("value"))

        name = cast(Union[Literal["updated_at"], Unset], d.pop("name", UNSET))
        if name != "updated_at" and not isinstance(name, Unset):
            raise ValueError(f"name must match const 'updated_at', got '{name}'")

        project_updated_at_filter = cls(operator=operator, value=value, name=name)

        project_updated_at_filter.additional_properties = d
        return project_updated_at_filter

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
