from unittest import IsolatedAsyncioTestCase

import demo_raw


class ExampleTest(IsolatedAsyncioTestCase):
    async def test_example(self):
        assert demo_raw