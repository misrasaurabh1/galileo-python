from collections.abc import Mapping
from typing import Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.scorer_name_filter_operator import ScorerNameFilterOperator
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScorerNameFilter")


@_attrs_define
class ScorerNameFilter:
    """
    Attributes:
        operator (ScorerNameFilterOperator):
        value (Union[list[str], str]):
        case_sensitive (Union[Unset, bool]):  Default: False.
        name (Union[Literal['name'], Unset]):  Default: 'name'.
    """

    operator: ScorerNameFilterOperator
    value: Union[list[str], str]
    case_sensitive: Union[Unset, bool] = False
    name: Union[Literal["name"], Unset] = "name"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operator = self.operator.value

        value: Union[list[str], str]
        if isinstance(self.value, list):
            value = self.value

        else:
            value = self.value

        case_sensitive = self.case_sensitive

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({"operator": operator, "value": value})
        if case_sensitive is not UNSET:
            field_dict["case_sensitive"] = case_sensitive
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operator = ScorerNameFilterOperator(d.pop("operator"))

        def _parse_value(data: object) -> Union[list[str], str]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_1 = cast(list[str], data)

                return value_type_1
            except:  # noqa: E722
                pass
            return cast(Union[list[str], str], data)

        value = _parse_value(d.pop("value"))

        case_sensitive = d.pop("case_sensitive", UNSET)

        name = cast(Union[Literal["name"], Unset], d.pop("name", UNSET))
        if name != "name" and not isinstance(name, Unset):
            raise ValueError(f"name must match const 'name', got '{name}'")

        scorer_name_filter = cls(operator=operator, value=value, case_sensitive=case_sensitive, name=name)

        scorer_name_filter.additional_properties = d
        return scorer_name_filter

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
