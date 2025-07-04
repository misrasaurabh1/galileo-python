from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset_append_row_values import DatasetAppendRowValues


T = TypeVar("T", bound="DatasetAppendRow")


@_attrs_define
class DatasetAppendRow:
    """
    Attributes:
        values (DatasetAppendRowValues):
        edit_type (Union[Literal['append_row'], Unset]):  Default: 'append_row'.
        row_id (Union[None, Unset, str]):
    """

    values: "DatasetAppendRowValues"
    edit_type: Union[Literal["append_row"], Unset] = "append_row"
    row_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        values = self.values.to_dict()

        edit_type = self.edit_type

        row_id: Union[None, Unset, str]
        if isinstance(self.row_id, Unset):
            row_id = UNSET
        else:
            row_id = self.row_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({"values": values})
        if edit_type is not UNSET:
            field_dict["edit_type"] = edit_type
        if row_id is not UNSET:
            field_dict["row_id"] = row_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_append_row_values import DatasetAppendRowValues

        d = dict(src_dict)
        values = DatasetAppendRowValues.from_dict(d.pop("values"))

        edit_type = cast(Union[Literal["append_row"], Unset], d.pop("edit_type", UNSET))
        if edit_type != "append_row" and not isinstance(edit_type, Unset):
            raise ValueError(f"edit_type must match const 'append_row', got '{edit_type}'")

        def _parse_row_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        row_id = _parse_row_id(d.pop("row_id", UNSET))

        dataset_append_row = cls(values=values, edit_type=edit_type, row_id=row_id)

        dataset_append_row.additional_properties = d
        return dataset_append_row

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
