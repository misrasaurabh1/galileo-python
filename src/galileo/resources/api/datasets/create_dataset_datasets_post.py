from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_create_dataset_datasets_post import BodyCreateDatasetDatasetsPost
from ...models.dataset_db import DatasetDB
from ...models.dataset_format import DatasetFormat
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BodyCreateDatasetDatasetsPost,
    format_: Union[Unset, DatasetFormat] = UNSET,
    hidden: Union[Unset, bool] = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params["hidden"] = hidden

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {"method": "post", "url": "/datasets", "params": params}

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DatasetDB, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = DatasetDB.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[DatasetDB, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyCreateDatasetDatasetsPost,
    format_: Union[Unset, DatasetFormat] = UNSET,
    hidden: Union[Unset, bool] = False,
) -> Response[Union[DatasetDB, HTTPValidationError]]:
    """Create Dataset

     Creates a standalone dataset.

    Args:
        format_ (Union[Unset, DatasetFormat]):
        hidden (Union[Unset, bool]):  Default: False.
        body (BodyCreateDatasetDatasetsPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DatasetDB, HTTPValidationError]]
    """

    kwargs = _get_kwargs(body=body, format_=format_, hidden=hidden)

    response = client.get_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BodyCreateDatasetDatasetsPost,
    format_: Union[Unset, DatasetFormat] = UNSET,
    hidden: Union[Unset, bool] = False,
) -> Optional[Union[DatasetDB, HTTPValidationError]]:
    """Create Dataset

     Creates a standalone dataset.

    Args:
        format_ (Union[Unset, DatasetFormat]):
        hidden (Union[Unset, bool]):  Default: False.
        body (BodyCreateDatasetDatasetsPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DatasetDB, HTTPValidationError]
    """

    return sync_detailed(client=client, body=body, format_=format_, hidden=hidden).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyCreateDatasetDatasetsPost,
    format_: Union[Unset, DatasetFormat] = UNSET,
    hidden: Union[Unset, bool] = False,
) -> Response[Union[DatasetDB, HTTPValidationError]]:
    """Create Dataset

     Creates a standalone dataset.

    Args:
        format_ (Union[Unset, DatasetFormat]):
        hidden (Union[Unset, bool]):  Default: False.
        body (BodyCreateDatasetDatasetsPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DatasetDB, HTTPValidationError]]
    """

    kwargs = _get_kwargs(body=body, format_=format_, hidden=hidden)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BodyCreateDatasetDatasetsPost,
    format_: Union[Unset, DatasetFormat] = UNSET,
    hidden: Union[Unset, bool] = False,
) -> Optional[Union[DatasetDB, HTTPValidationError]]:
    """Create Dataset

     Creates a standalone dataset.

    Args:
        format_ (Union[Unset, DatasetFormat]):
        hidden (Union[Unset, bool]):  Default: False.
        body (BodyCreateDatasetDatasetsPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DatasetDB, HTTPValidationError]
    """

    return (await asyncio_detailed(client=client, body=body, format_=format_, hidden=hidden)).parsed
