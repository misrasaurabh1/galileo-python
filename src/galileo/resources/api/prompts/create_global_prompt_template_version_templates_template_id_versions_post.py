from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_prompt_template_version import BasePromptTemplateVersion
from ...models.base_prompt_template_version_response import BasePromptTemplateVersionResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(template_id: str, *, body: BasePromptTemplateVersion) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {"method": "post", "url": f"/templates/{template_id}/versions"}

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BasePromptTemplateVersionResponse, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = BasePromptTemplateVersionResponse.from_dict(response.json())

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
) -> Response[Union[BasePromptTemplateVersionResponse, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    template_id: str, *, client: AuthenticatedClient, body: BasePromptTemplateVersion
) -> Response[Union[BasePromptTemplateVersionResponse, HTTPValidationError]]:
    """Create Global Prompt Template Version

     Create a prompt template version for a given prompt template.

    Parameters
    ----------
    template_id : UUID4
        Prompt template ID.
    ctx : Context
        Request context including authentication information
    base_prompt_template_version : BasePromptTemplateVersion
        Version details to create

    Returns
    -------
    BasePromptTemplateVersionResponse
        Response with details about the created prompt template version.

    Args:
        template_id (str):
        body (BasePromptTemplateVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BasePromptTemplateVersionResponse, HTTPValidationError]]
    """

    kwargs = _get_kwargs(template_id=template_id, body=body)

    response = client.get_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


def sync(
    template_id: str, *, client: AuthenticatedClient, body: BasePromptTemplateVersion
) -> Optional[Union[BasePromptTemplateVersionResponse, HTTPValidationError]]:
    """Create Global Prompt Template Version

     Create a prompt template version for a given prompt template.

    Parameters
    ----------
    template_id : UUID4
        Prompt template ID.
    ctx : Context
        Request context including authentication information
    base_prompt_template_version : BasePromptTemplateVersion
        Version details to create

    Returns
    -------
    BasePromptTemplateVersionResponse
        Response with details about the created prompt template version.

    Args:
        template_id (str):
        body (BasePromptTemplateVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BasePromptTemplateVersionResponse, HTTPValidationError]
    """

    return sync_detailed(template_id=template_id, client=client, body=body).parsed


async def asyncio_detailed(
    template_id: str, *, client: AuthenticatedClient, body: BasePromptTemplateVersion
) -> Response[Union[BasePromptTemplateVersionResponse, HTTPValidationError]]:
    """Create Global Prompt Template Version

     Create a prompt template version for a given prompt template.

    Parameters
    ----------
    template_id : UUID4
        Prompt template ID.
    ctx : Context
        Request context including authentication information
    base_prompt_template_version : BasePromptTemplateVersion
        Version details to create

    Returns
    -------
    BasePromptTemplateVersionResponse
        Response with details about the created prompt template version.

    Args:
        template_id (str):
        body (BasePromptTemplateVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BasePromptTemplateVersionResponse, HTTPValidationError]]
    """

    kwargs = _get_kwargs(template_id=template_id, body=body)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    template_id: str, *, client: AuthenticatedClient, body: BasePromptTemplateVersion
) -> Optional[Union[BasePromptTemplateVersionResponse, HTTPValidationError]]:
    """Create Global Prompt Template Version

     Create a prompt template version for a given prompt template.

    Parameters
    ----------
    template_id : UUID4
        Prompt template ID.
    ctx : Context
        Request context including authentication information
    base_prompt_template_version : BasePromptTemplateVersion
        Version details to create

    Returns
    -------
    BasePromptTemplateVersionResponse
        Response with details about the created prompt template version.

    Args:
        template_id (str):
        body (BasePromptTemplateVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BasePromptTemplateVersionResponse, HTTPValidationError]
    """

    return (await asyncio_detailed(template_id=template_id, client=client, body=body)).parsed
