import json
from typing import List
from unittest.mock import AsyncMock, Mock

import pytest

from payroc.core.custom_pagination import AsyncPayrocPager, Page, SyncPayrocPager


class MockLink:
    def __init__(self, rel: str, href: str):
        self.rel = rel
        self.href = href


class MockResponse:
    def __init__(self, data: List[str], links: List[MockLink]):
        self.data = data
        self.links = links


class MockHttpClient:
    def __init__(self, responses: List[MockResponse]):
        self.responses = responses
        self.call_count = 0

    def request(self, path: str, method: str, base_url: str = "", **kwargs):
        if self.call_count < len(self.responses):
            response_data = self.responses[self.call_count]
            self.call_count += 1
            mock_http_response = Mock()
            response_dict = {
                "data": response_data.data,
                "links": [{"rel": link.rel, "href": link.href} for link in response_data.links]
            }
            mock_http_response.text = json.dumps(response_dict)
            return mock_http_response
        mock_http_response = Mock()
        mock_http_response.text = '{"data": [], "links": []}'
        return mock_http_response


class MockAsyncHttpClient:
    def __init__(self, responses: List[MockResponse]):
        self.responses = responses
        self.call_count = 0

    async def request(self, path: str, method: str, base_url: str = "", **kwargs):
        if self.call_count < len(self.responses):
            response_data = self.responses[self.call_count]
            self.call_count += 1
            mock_http_response = Mock()
            response_dict = {
                "data": response_data.data,
                "links": [{"rel": link.rel, "href": link.href} for link in response_data.links]
            }
            mock_http_response.text = json.dumps(response_dict)
            return mock_http_response
        mock_http_response = Mock()
        mock_http_response.text = '{"data": [], "links": []}'
        return mock_http_response


class MockClientWrapper:
    def __init__(self, httpx_client):
        self.httpx_client = httpx_client


def test_page_creation():
    items = ["item1", "item2", "item3"]
    page = Page(items=items)
    
    assert len(page) == 3
    assert list(page) == items


def test_page_empty():
    empty_page = Page.empty()
    
    assert len(empty_page) == 0
    assert list(empty_page) == []


def test_sync_pager_initialization():
    initial_response = MockResponse(
        data=["item1", "item2"],
        links=[
            MockLink(rel="next", href="https://api.example.com/page2"),
            MockLink(rel="previous", href="https://api.example.com/page0")
        ]
    )
    
    client_wrapper = MockClientWrapper(Mock())
    pager = SyncPayrocPager(initial_response=initial_response, client_wrapper=client_wrapper)
    
    assert pager.has_next_page is True
    assert pager.has_previous_page is True
    assert len(pager.current_page) == 2
    assert list(pager.current_page) == ["item1", "item2"]


def test_sync_pager_no_next_page():
    initial_response = MockResponse(
        data=["item1", "item2"],
        links=[]
    )
    
    client_wrapper = MockClientWrapper(Mock())
    pager = SyncPayrocPager(initial_response=initial_response, client_wrapper=client_wrapper)
    
    assert pager.has_next_page is False
    assert pager.has_previous_page is False


def test_sync_pager_get_next_page():
    initial_response = MockResponse(
        data=["item1", "item2"],
        links=[MockLink(rel="next", href="https://api.example.com/page2")]
    )
    
    next_response = MockResponse(
        data=["item3", "item4"],
        links=[]
    )
    
    http_client = MockHttpClient([next_response])
    client_wrapper = MockClientWrapper(http_client)
    pager = SyncPayrocPager(initial_response=initial_response, client_wrapper=client_wrapper)
    
    assert pager.has_next_page is True
    
    next_page = pager.get_next_page()
    
    assert len(next_page) == 2
    assert list(next_page) == ["item3", "item4"]
    assert pager.has_next_page is False


def test_sync_pager_get_previous_page():
    initial_response = MockResponse(
        data=["item3", "item4"],
        links=[MockLink(rel="previous", href="https://api.example.com/page1")]
    )
    
    previous_response = MockResponse(
        data=["item1", "item2"],
        links=[]
    )
    
    http_client = MockHttpClient([previous_response])
    client_wrapper = MockClientWrapper(http_client)
    pager = SyncPayrocPager(initial_response=initial_response, client_wrapper=client_wrapper)
    
    assert pager.has_previous_page is True
    
    previous_page = pager.get_previous_page()
    
    assert len(previous_page) == 2
    assert list(previous_page) == ["item1", "item2"]
    assert pager.has_previous_page is False


def test_sync_pager_get_next_page_when_none():
    initial_response = MockResponse(
        data=["item1", "item2"],
        links=[]
    )
    
    client_wrapper = MockClientWrapper(Mock())
    pager = SyncPayrocPager(initial_response=initial_response, client_wrapper=client_wrapper)
    
    next_page = pager.get_next_page()
    
    assert len(next_page) == 0


def test_sync_pager_get_previous_page_when_none():
    initial_response = MockResponse(
        data=["item1", "item2"],
        links=[]
    )
    
    client_wrapper = MockClientWrapper(Mock())
    pager = SyncPayrocPager(initial_response=initial_response, client_wrapper=client_wrapper)
    
    previous_page = pager.get_previous_page()
    
    assert len(previous_page) == 0


def test_sync_pager_iteration():
    initial_response = MockResponse(
        data=["item1", "item2"],
        links=[MockLink(rel="next", href="https://api.example.com/page2")]
    )
    
    next_response = MockResponse(
        data=["item3", "item4"],
        links=[]
    )
    
    http_client = MockHttpClient([next_response])
    client_wrapper = MockClientWrapper(http_client)
    pager = SyncPayrocPager(initial_response=initial_response, client_wrapper=client_wrapper)
    
    items = list(pager)
    
    assert items == ["item1", "item2", "item3", "item4"]


def test_sync_pager_get_next_pages():
    initial_response = MockResponse(
        data=["item1", "item2"],
        links=[MockLink(rel="next", href="https://api.example.com/page2")]
    )
    
    page2_response = MockResponse(
        data=["item3", "item4"],
        links=[MockLink(rel="next", href="https://api.example.com/page3")]
    )
    
    page3_response = MockResponse(
        data=["item5", "item6"],
        links=[]
    )
    
    http_client = MockHttpClient([page2_response, page3_response])
    client_wrapper = MockClientWrapper(http_client)
    pager = SyncPayrocPager(initial_response=initial_response, client_wrapper=client_wrapper)
    
    pages = list(pager.get_next_pages())
    
    assert len(pages) == 2
    assert list(pages[0]) == ["item3", "item4"]
    assert list(pages[1]) == ["item5", "item6"]


def test_sync_pager_get_previous_pages():
    initial_response = MockResponse(
        data=["item5", "item6"],
        links=[MockLink(rel="previous", href="https://api.example.com/page2")]
    )
    
    page2_response = MockResponse(
        data=["item3", "item4"],
        links=[MockLink(rel="previous", href="https://api.example.com/page1")]
    )
    
    page1_response = MockResponse(
        data=["item1", "item2"],
        links=[]
    )
    
    http_client = MockHttpClient([page2_response, page1_response])
    client_wrapper = MockClientWrapper(http_client)
    pager = SyncPayrocPager(initial_response=initial_response, client_wrapper=client_wrapper)
    
    pages = list(pager.get_previous_pages())
    
    assert len(pages) == 2
    assert list(pages[0]) == ["item3", "item4"]
    assert list(pages[1]) == ["item1", "item2"]


@pytest.mark.asyncio
async def test_async_pager_initialization():
    initial_response = MockResponse(
        data=["item1", "item2"],
        links=[
            MockLink(rel="next", href="https://api.example.com/page2"),
            MockLink(rel="previous", href="https://api.example.com/page0")
        ]
    )
    
    client_wrapper = MockClientWrapper(AsyncMock())
    pager = AsyncPayrocPager(initial_response=initial_response, client_wrapper=client_wrapper)
    
    assert pager.has_next_page is True
    assert pager.has_previous_page is True
    assert len(pager.current_page) == 2
    assert list(pager.current_page) == ["item1", "item2"]


@pytest.mark.asyncio
async def test_async_pager_get_next_page():
    initial_response = MockResponse(
        data=["item1", "item2"],
        links=[MockLink(rel="next", href="https://api.example.com/page2")]
    )
    
    next_response = MockResponse(
        data=["item3", "item4"],
        links=[]
    )
    
    http_client = MockAsyncHttpClient([next_response])
    client_wrapper = MockClientWrapper(http_client)
    pager = AsyncPayrocPager(initial_response=initial_response, client_wrapper=client_wrapper)
    
    assert pager.has_next_page is True
    
    next_page = await pager.get_next_page_async()
    
    assert len(next_page) == 2
    assert list(next_page) == ["item3", "item4"]
    assert pager.has_next_page is False


@pytest.mark.asyncio
async def test_async_pager_get_previous_page():
    initial_response = MockResponse(
        data=["item3", "item4"],
        links=[MockLink(rel="previous", href="https://api.example.com/page1")]
    )
    
    previous_response = MockResponse(
        data=["item1", "item2"],
        links=[]
    )
    
    http_client = MockAsyncHttpClient([previous_response])
    client_wrapper = MockClientWrapper(http_client)
    pager = AsyncPayrocPager(initial_response=initial_response, client_wrapper=client_wrapper)
    
    assert pager.has_previous_page is True
    
    previous_page = await pager.get_previous_page_async()
    
    assert len(previous_page) == 2
    assert list(previous_page) == ["item1", "item2"]
    assert pager.has_previous_page is False


@pytest.mark.asyncio
async def test_async_pager_iteration():
    initial_response = MockResponse(
        data=["item1", "item2"],
        links=[MockLink(rel="next", href="https://api.example.com/page2")]
    )
    
    next_response = MockResponse(
        data=["item3", "item4"],
        links=[]
    )
    
    http_client = MockAsyncHttpClient([next_response])
    client_wrapper = MockClientWrapper(http_client)
    pager = AsyncPayrocPager(initial_response=initial_response, client_wrapper=client_wrapper)
    
    items = []
    async for item in pager:
        items.append(item)
    
    assert items == ["item1", "item2", "item3", "item4"]


@pytest.mark.asyncio
async def test_async_pager_get_next_pages():
    initial_response = MockResponse(
        data=["item1", "item2"],
        links=[MockLink(rel="next", href="https://api.example.com/page2")]
    )
    
    page2_response = MockResponse(
        data=["item3", "item4"],
        links=[MockLink(rel="next", href="https://api.example.com/page3")]
    )
    
    page3_response = MockResponse(
        data=["item5", "item6"],
        links=[]
    )
    
    http_client = MockAsyncHttpClient([page2_response, page3_response])
    client_wrapper = MockClientWrapper(http_client)
    pager = AsyncPayrocPager(initial_response=initial_response, client_wrapper=client_wrapper)
    
    pages = []
    async for page in pager.get_next_pages_async():
        pages.append(page)
    
    assert len(pages) == 2
    assert list(pages[0]) == ["item3", "item4"]
    assert list(pages[1]) == ["item5", "item6"]


@pytest.mark.asyncio
async def test_async_pager_get_previous_pages():
    initial_response = MockResponse(
        data=["item5", "item6"],
        links=[MockLink(rel="previous", href="https://api.example.com/page2")]
    )
    
    page2_response = MockResponse(
        data=["item3", "item4"],
        links=[MockLink(rel="previous", href="https://api.example.com/page1")]
    )
    
    page1_response = MockResponse(
        data=["item1", "item2"],
        links=[]
    )
    
    http_client = MockAsyncHttpClient([page2_response, page1_response])
    client_wrapper = MockClientWrapper(http_client)
    pager = AsyncPayrocPager(initial_response=initial_response, client_wrapper=client_wrapper)
    
    pages = []
    async for page in pager.get_previous_pages_async():
        pages.append(page)
    
    assert len(pages) == 2
    assert list(pages[0]) == ["item3", "item4"]
    assert list(pages[1]) == ["item1", "item2"]


def test_sync_pager_empty_data():
    initial_response = MockResponse(
        data=[],
        links=[]
    )
    
    client_wrapper = MockClientWrapper(Mock())
    pager = SyncPayrocPager(initial_response=initial_response, client_wrapper=client_wrapper)
    
    assert len(pager.current_page) == 0
    assert pager.has_next_page is False
    assert pager.has_previous_page is False


@pytest.mark.asyncio
async def test_async_pager_empty_data():
    initial_response = MockResponse(
        data=[],
        links=[]
    )
    
    client_wrapper = MockClientWrapper(AsyncMock())
    pager = AsyncPayrocPager(initial_response=initial_response, client_wrapper=client_wrapper)
    
    assert len(pager.current_page) == 0
    assert pager.has_next_page is False
    assert pager.has_previous_page is False
