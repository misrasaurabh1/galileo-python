from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.list_prompt_template_params import ListPromptTemplateParams
from ...models.list_prompt_template_response import ListPromptTemplateResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *, body: ListPromptTemplateParams, starting_token: Union[Unset, int] = 0, limit: Union[Unset, int] = 100
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["starting_token"] = starting_token

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {"method": "post", "url": "/templates/query", "params": params}

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, ListPromptTemplateResponse]]:
    if response.status_code == 200:
        response_200 = ListPromptTemplateResponse.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, ListPromptTemplateResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ListPromptTemplateParams,
    starting_token: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
) -> Response[Union[HTTPValidationError, ListPromptTemplateResponse]]:
    """Query Templates

     Query prompt templates the user has access to.

    Parameters
    ----------
    params : ListPromptTemplateParams
        Query parameters for filtering and sorting
    pagination : PaginationRequestMixin
        Pagination parameters
    ctx : Context
        User context containing database session and user information

    Returns
    -------
    ListPromptTemplateResponse
        Paginated list of prompt template responses that the user has access to.

    Args:
        starting_token (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.
        body (ListPromptTemplateParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ListPromptTemplateResponse]]
    """

    kwargs = _get_kwargs(body=body, starting_token=starting_token, limit=limit)

    response = client.get_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ListPromptTemplateParams,
    starting_token: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
) -> Optional[Union[HTTPValidationError, ListPromptTemplateResponse]]:
    """Query Templates

     Query prompt templates the user has access to.

    Parameters
    ----------
    params : ListPromptTemplateParams
        Query parameters for filtering and sorting
    pagination : PaginationRequestMixin
        Pagination parameters
    ctx : Context
        User context containing database session and user information

    Returns
    -------
    ListPromptTemplateResponse
        Paginated list of prompt template responses that the user has access to.

    Args:
        starting_token (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.
        body (ListPromptTemplateParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ListPromptTemplateResponse]
    """

    return sync_detailed(client=client, body=body, starting_token=starting_token, limit=limit).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ListPromptTemplateParams,
    starting_token: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
) -> Response[Union[HTTPValidationError, ListPromptTemplateResponse]]:
    """Query Templates

     Query prompt templates the user has access to.

    Parameters
    ----------
    params : ListPromptTemplateParams
        Query parameters for filtering and sorting
    pagination : PaginationRequestMixin
        Pagination parameters
    ctx : Context
        User context containing database session and user information

    Returns
    -------
    ListPromptTemplateResponse
        Paginated list of prompt template responses that the user has access to.

    Args:
        starting_token (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.
        body (ListPromptTemplateParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ListPromptTemplateResponse]]
    """

    kwargs = _get_kwargs(body=body, starting_token=starting_token, limit=limit)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ListPromptTemplateParams,
    starting_token: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
) -> Optional[Union[HTTPValidationError, ListPromptTemplateResponse]]:
    """Query Templates

     Query prompt templates the user has access to.

    Parameters
    ----------
    params : ListPromptTemplateParams
        Query parameters for filtering and sorting
    pagination : PaginationRequestMixin
        Pagination parameters
    ctx : Context
        User context containing database session and user information

    Returns
    -------
    ListPromptTemplateResponse
        Paginated list of prompt template responses that the user has access to.

    Args:
        starting_token (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.
        body (ListPromptTemplateParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ListPromptTemplateResponse]
    """

    return (await asyncio_detailed(client=client, body=body, starting_token=starting_token, limit=limit)).parsed
