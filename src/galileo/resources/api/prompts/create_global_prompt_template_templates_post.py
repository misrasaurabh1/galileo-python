from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_prompt_template_response import BasePromptTemplateResponse
from ...models.create_prompt_template_with_version_request_body import CreatePromptTemplateWithVersionRequestBody
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(*, body: CreatePromptTemplateWithVersionRequestBody) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {"method": "post", "url": "/templates"}

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BasePromptTemplateResponse, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = BasePromptTemplateResponse.from_dict(response.json())

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
) -> Response[Union[BasePromptTemplateResponse, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *, client: AuthenticatedClient, body: CreatePromptTemplateWithVersionRequestBody
) -> Response[Union[BasePromptTemplateResponse, HTTPValidationError]]:
    """Create Global Prompt Template

     Create a global prompt template.

    Parameters
    ----------
    ctx : Context
        Request context including authentication information
    create_request : CreatePromptTemplateWithVersionRequestBody
        Request body containing template name and content

    Returns
    -------
    BasePromptTemplateResponse
        Details about the created prompt template.

    Args:
        body (CreatePromptTemplateWithVersionRequestBody): Body to create a new prompt template
            with version.

            This is only used for parsing the body from the request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BasePromptTemplateResponse, HTTPValidationError]]
    """

    kwargs = _get_kwargs(body=body)

    response = client.get_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


def sync(
    *, client: AuthenticatedClient, body: CreatePromptTemplateWithVersionRequestBody
) -> Optional[Union[BasePromptTemplateResponse, HTTPValidationError]]:
    """Create Global Prompt Template

     Create a global prompt template.

    Parameters
    ----------
    ctx : Context
        Request context including authentication information
    create_request : CreatePromptTemplateWithVersionRequestBody
        Request body containing template name and content

    Returns
    -------
    BasePromptTemplateResponse
        Details about the created prompt template.

    Args:
        body (CreatePromptTemplateWithVersionRequestBody): Body to create a new prompt template
            with version.

            This is only used for parsing the body from the request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BasePromptTemplateResponse, HTTPValidationError]
    """

    return sync_detailed(client=client, body=body).parsed


async def asyncio_detailed(
    *, client: AuthenticatedClient, body: CreatePromptTemplateWithVersionRequestBody
) -> Response[Union[BasePromptTemplateResponse, HTTPValidationError]]:
    """Create Global Prompt Template

     Create a global prompt template.

    Parameters
    ----------
    ctx : Context
        Request context including authentication information
    create_request : CreatePromptTemplateWithVersionRequestBody
        Request body containing template name and content

    Returns
    -------
    BasePromptTemplateResponse
        Details about the created prompt template.

    Args:
        body (CreatePromptTemplateWithVersionRequestBody): Body to create a new prompt template
            with version.

            This is only used for parsing the body from the request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BasePromptTemplateResponse, HTTPValidationError]]
    """

    kwargs = _get_kwargs(body=body)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *, client: AuthenticatedClient, body: CreatePromptTemplateWithVersionRequestBody
) -> Optional[Union[BasePromptTemplateResponse, HTTPValidationError]]:
    """Create Global Prompt Template

     Create a global prompt template.

    Parameters
    ----------
    ctx : Context
        Request context including authentication information
    create_request : CreatePromptTemplateWithVersionRequestBody
        Request body containing template name and content

    Returns
    -------
    BasePromptTemplateResponse
        Details about the created prompt template.

    Args:
        body (CreatePromptTemplateWithVersionRequestBody): Body to create a new prompt template
            with version.

            This is only used for parsing the body from the request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BasePromptTemplateResponse, HTTPValidationError]
    """

    return (await asyncio_detailed(client=client, body=body)).parsed
