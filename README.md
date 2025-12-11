# Payroc API Python SDK

[![pypi](https://img.shields.io/pypi/v/payroc)](https://pypi.python.org/pypi/payroc)

The Payroc API Python SDK provides convenient access to the Payroc API from Python.

## Contents

- [Installation](#installation)
- [Usage](#usage)
  - [API Key](#api-key)
  - [Payroc Client](#payroc-client)
    - [Advanced Usage with Custom Environment](#advanced-usage-with-custom-environment)
- [Async Client](#async-client)
- [Exception Handling](#exception-handling)
- [Logging](#logging)
- [Pagination](#pagination)
- [Request Parameters](#request-parameters)
- [Polymorphic Types](#polymorphic-types)
- [Advanced](#advanced)
  - [Access Raw Response Data](#access-raw-response-data)
  - [Retries](#retries)
  - [Timeouts](#timeouts)
  - [Custom Client](#custom-client)
- [Contributing](#contributing)
- [References](#references)

## Installation

```sh
pip install payroc
```

## Usage

### API Key

You need to provide your API Key to the `Payroc` client constructor. In this example we read it from an environment variable named `PAYROC_API_KEY`. In your own code you should consider security and compliance best practices, likely retrieving this value from a secure vault on demand.

### Payroc Client

Instantiate and use the client with the following:

```python
import os
from payroc import (
    Address,
    CardPayloadCardDetails_Raw,
    Customer,
    CustomField,
    Device,
    PaymentOrderRequest,
    Payroc,
    Shipping,
)
from payroc.card_payments.payments import PaymentRequestPaymentMethod_Card

api_key = os.environ.get("PAYROC_API_KEY")
if not api_key:
    raise Exception("Payroc API Key not found")

client = Payroc(api_key=api_key)
```

Then you can access the various API endpoints through the `client` object. For example, to create a payment:

```python
client.card_payments.payments.create(
    idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
    channel="web",
    processing_terminal_id="1234001",
    operator="Jane",
    order=PaymentOrderRequest(
        order_id="OrderRef6543",
        description="Large Pepperoni Pizza",
        amount=4999,
        currency="USD",
    ),
    customer=Customer(
        first_name="Sarah",
        last_name="Hopper",
        billing_address=Address(
            address_1="1 Example Ave.",
            address_2="Example Address Line 2",
            address_3="Example Address Line 3",
            city="Chicago",
            state="Illinois",
            country="US",
            postal_code="60056",
        ),
        shipping_address=Shipping(
            recipient_name="Sarah Hopper",
            address=Address(
                address_1="1 Example Ave.",
                address_2="Example Address Line 2",
                address_3="Example Address Line 3",
                city="Chicago",
                state="Illinois",
                country="US",
                postal_code="60056",
            ),
        ),
    ),
    payment_method=PaymentRequestPaymentMethod_Card(
        card_details=CardPayloadCardDetails_Raw(
            device=Device(
                model="bbposChp",
                serial_number="1850010868",
            ),
            raw_data="A1B2C3D4E5F67890ABCD1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF",
        ),
    ),
    custom_fields=[
        CustomField(
            name="yourCustomField",
            value="abc123",
        )
    ],
)
```

### Advanced Usage with Custom Environment

If you wish to use the SDK against a custom URL, such as a mock API server, you can provide a custom `PayrocEnvironment` to the `Payroc` constructor:

```python
from payroc import Payroc, PayrocEnvironment

mock_environment = PayrocEnvironment(
    api="http://localhost:3000",
    identity="http://localhost:3001"
)

client = Payroc(
    api_key=api_key,
    environment=mock_environment
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API. Note that if you are constructing an Async httpx client class to pass into this client, use `httpx.AsyncClient()` instead of `httpx.Client()` (e.g. for the `httpx_client` parameter of this client).

```python
import asyncio
import os

from payroc import (
    Address,
    AsyncPayroc,
    CardPayloadCardDetails_Raw,
    Customer,
    CustomField,
    Device,
    PaymentOrderRequest,
    Shipping,
)
from payroc.card_payments.payments import PaymentRequestPaymentMethod_Card

api_key = os.environ.get("PAYROC_API_KEY")
if not api_key:
    raise Exception("Payroc API Key not found")

client = AsyncPayroc(api_key=api_key)


async def main() -> None:
    await client.card_payments.payments.create(
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        channel="web",
        processing_terminal_id="1234001",
        operator="Jane",
        order=PaymentOrderRequest(
            order_id="OrderRef6543",
            description="Large Pepperoni Pizza",
            amount=4999,
            currency="USD",
        ),
        customer=Customer(
            first_name="Sarah",
            last_name="Hopper",
            billing_address=Address(
                address_1="1 Example Ave.",
                address_2="Example Address Line 2",
                address_3="Example Address Line 3",
                city="Chicago",
                state="Illinois",
                country="US",
                postal_code="60056",
            ),
            shipping_address=Shipping(
                recipient_name="Sarah Hopper",
                address=Address(
                    address_1="1 Example Ave.",
                    address_2="Example Address Line 2",
                    address_3="Example Address Line 3",
                    city="Chicago",
                    state="Illinois",
                    country="US",
                    postal_code="60056",
                ),
            ),
        ),
        payment_method=PaymentRequestPaymentMethod_Card(
            card_details=CardPayloadCardDetails_Raw(
                device=Device(
                    model="bbposChp",
                    serial_number="1850010868",
                ),
                raw_data="A1B2C3D4E5F67890ABCD1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF",
            ),
        ),
        custom_fields=[
            CustomField(
                name="yourCustomField",
                value="abc123",
            )
        ],
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from payroc.core.api_error import ApiError

try:
    client.card_payments.payments.create(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Logging

> [!WARNING]  
> Be careful when configuring your logging not to log the headers of outbound HTTP requests, lest you leak an API key or access token.

## Pagination

List endpoints are paginated. The SDK provides a `SyncPayrocPager` (or `AsyncPayrocPager` for async clients) so that you can simply loop over the items:

```python
import datetime
import os

from payroc import Payroc

api_key = os.environ.get("PAYROC_API_KEY")
if not api_key:
    raise Exception("Payroc API Key not found")

client = Payroc(api_key=api_key)

pager = client.card_payments.payments.list(
    processing_terminal_id="1234001",
    order_id="OrderRef6543",
    operator="Jane",
    cardholder_name="Sarah%20Hazel%20Hopper",
    first_6="453985",
    last_4="7062",
    tender="ebt",
    date_from=datetime.datetime.fromisoformat(
        "2024-07-01 15:30:00+00:00",
    ),
    date_to=datetime.datetime.fromisoformat(
        "2024-07-03 15:30:00+00:00",
    ),
    settlement_state="settled",
    settlement_date=datetime.date.fromisoformat(
        "2024-07-02",
    ),
    payment_link_id="JZURRJBUPS",
    before="2571",
    after="8516",
    limit=1,
)

# Current page is always accessible
for item in pager.current_page:
    print(item)

# Iterate forward through all items across all pages
for item in pager:
    print(item)

# The pagers also expose bidirectional paging helpers:
# forward iteration, and explicit backwards navigation.

# Manually step forward or backward as needed
if pager.has_next_page:
    next_page = pager.get_next_page()
    for item in next_page:
        print(item)

# After moving forward you can walk backwards too
while pager.has_previous_page:
    previous_page = pager.get_previous_page()
    for item in previous_page:
        print(item)
```

Async clients expose the same helpers with async counterparts
```python
import os
from payroc import AsyncPayroc

api_key = os.environ.get("PAYROC_API_KEY")
if not api_key:
    raise Exception("Payroc API Key not found")

async_client = AsyncPayroc(api_key=api_key)

pager = await async_client.card_payments.payments.list(
    processing_terminal_id="1234001"
)

async for page in pager.get_next_pages_async():
    for item in page:
        ...

async for page in pager.get_previous_pages_async():
    for item in page:
        ...
```

## Request Parameters

Sometimes you need to filter results, for example, retrieving results from a given date. Raw API calls might use query parameters. The SDK equivalent pattern is setting the values in the request parameters.

Examples of setting different query parameters:

```python
import datetime

# Filter by date range
pager = client.card_payments.payments.list(
    processing_terminal_id="1234001",
    date_from=datetime.datetime(2024, 7, 1, 15, 30, 0, 0)
)

# Filter by date_to
pager = client.card_payments.payments.list(
    processing_terminal_id="1234001",
    date_to=datetime.datetime(2024, 7, 3, 15, 30, 0, 0)
)

# Pagination with after cursor
pager = client.card_payments.payments.list(
    processing_terminal_id="1234001",
    after="8516"
)

# Pagination with before cursor
pager = client.card_payments.payments.list(
    processing_terminal_id="1234001",
    before="2571"
)
```

Inspect the method signature in your IDE to see what parameters are available for filtering.

## Polymorphic Types

Our API makes frequent use of polymorphic data structures. This is when a value might be one of multiple types, and the type is determined at runtime. For example, a payment method can be a card, secure token, digital wallet, or single-use token. The SDK uses Pydantic's discriminated unions to handle this.

### Creating Polymorphic Data

When creating polymorphic types, you instantiate the specific variant class directly:

```python
from payroc.card_payments.payments import (
    PaymentRequestPaymentMethod_Card,
    PaymentRequestPaymentMethod_SecureToken,
)
from payroc import (
    CardPayloadCardDetails_Keyed,
    KeyedCardDetailsKeyedData_PlainText,
)

# Create a card payment method with keyed data
card_payment = PaymentRequestPaymentMethod_Card(
    card_details=CardPayloadCardDetails_Keyed(
        keyed_data=KeyedCardDetailsKeyedData_PlainText(
            card_number="4111111111111111",
            expiry_date="1225",
            cvv="123"
        )
    )
)

# Create a secure token payment method
token_payment = PaymentRequestPaymentMethod_SecureToken(
    token="your-secure-token-here"
)
```

The SDK uses a `type` discriminator field to determine which variant is being used. Each variant class has a literal type field that identifies it.

### Handling Polymorphic Data

When working with polymorphic types in responses, you can check the `type` field to determine which variant you're dealing with:

```python
import os
from payroc import Payroc

api_key = os.environ.get("PAYROC_API_KEY")
if not api_key:
    raise Exception("Payroc API Key not found")

client = Payroc(api_key=api_key)

# Retrieve an owner (which has polymorphic contact methods)
owner = client.boarding.owners.retrieve(owner_id=12345)

for contact_method in owner.contact_methods:
    # Check the type discriminator
    if contact_method.type == "email":
        print(f"Email: {contact_method.value}")
    elif contact_method.type == "phone":
        print(f"Phone: {contact_method.value}")
    elif contact_method.type == "mobile":
        print(f"Mobile: {contact_method.value}")
    elif contact_method.type == "fax":
        print(f"Fax: {contact_method.value}")
```

You can also use `isinstance()` to check the specific type:

```python
from payroc.types import ContactMethod_Email, ContactMethod_Phone

for contact_method in owner.contact_methods:
    if isinstance(contact_method, ContactMethod_Email):
        # Type checker knows this is an email
        print(f"Email: {contact_method.value}")
    elif isinstance(contact_method, ContactMethod_Phone):
        # Type checker knows this is a phone
        print(f"Phone: {contact_method.value}")
```

Common polymorphic types in the API include:
- **Payment methods** - Card, secure token, digital wallet, single-use token
- **Contact methods** - Email, phone, mobile, fax
- **Card details** - Keyed, swiped, ICC (chip), raw (encrypted)
- **Identifiers** - SSN, EIN, passport, driver's license

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
import os
from payroc import Payroc

api_key = os.environ.get("PAYROC_API_KEY")
if not api_key:
    raise Exception("Payroc API Key not found")

client = Payroc(api_key=api_key)

response = client.card_payments.payments.with_raw_response.create(...)
print(response.headers)  # access the response headers
print(response.data)  # access the underlying object

pager = client.card_payments.payments.list(...)
print(pager.current_page)  # Page dataclass for the first response
for item in pager:
    print(item)  # access every item while walking forward
for page in pager.get_next_pages():
    for item in page:
        print(item)
for page in pager.get_previous_pages():
    for item in page:
        print(item)
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

A request is deemed retryable when any of the following HTTP status codes is returned:

- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) (Internal Server Errors)

Use the `max_retries` request option to configure this behavior.

```python
from payroc.core.request_options import RequestOptions

client.card_payments.payments.create(
    ...,
    request_options=RequestOptions(
        max_retries=1
    )
)
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python
import os
from payroc import Payroc
from payroc.core.request_options import RequestOptions

api_key = os.environ.get("PAYROC_API_KEY")
if not api_key:
    raise Exception("Payroc API Key not found")

client = Payroc(
    api_key=api_key,
    timeout=20.0,
)

# Override timeout for a specific method
client.card_payments.payments.create(
    ...,
    request_options=RequestOptions(
        timeout_in_seconds=1
    )
)
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import os
import httpx
from payroc import Payroc

api_key = os.environ.get("PAYROC_API_KEY")
if not api_key:
    raise Exception("Payroc API Key not found")

client = Payroc(
    api_key=api_key,
    httpx_client=httpx.Client(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!

For details on setting up your development environment, running tests, and code quality standards, please see [CONTRIBUTING.md](./CONTRIBUTING.md).

## References

The Payroc API SDK is generated via [Fern](https://www.buildwithfern.com/).

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fpayroc%2Fpapi-sdk-python)
