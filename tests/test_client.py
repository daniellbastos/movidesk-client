import pytest

from unittest import mock

from movidesk_client.client import MovideskClient


def test_resources():
    client = MovideskClient('super-token')

    assert 'https://api.movidesk.com/public/v1/example-path?token=super-token' == client._get_url('/example-path')


@mock.patch('movidesk_client.client.requests')
def test_call_person_create(mocked_request):
    client = MovideskClient('super-token')

    client.person_create({'foo': 'bar'})

    mocked_request.post.assert_called_once_with(
        'https://api.movidesk.com/public/v1/persons?token=super-token',
        {'foo': 'bar'},
        headers={'content-type': 'application/json'}
    )


@mock.patch('movidesk_client.client.requests')
def test_call_ticket_create(mocked_request):
    client = MovideskClient('super-token')

    client.ticket_create({'foo': 'bar'})

    mocked_request.post.assert_called_once_with(
        'https://api.movidesk.com/public/v1/tickets?token=super-token',
        {'foo': 'bar'},
        headers={'content-type': 'application/json'}
    )
