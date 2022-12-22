import unittest
from pds.api_client import Configuration
from pds.api_client import ApiClient

from pds.api_client.apis.paths.classes_class_identifier_members import ClassesClassIdentifierMembers

class MyTestCase(unittest.TestCase):

    def setUp(self):
        # create an instance of the API class
        configuration = Configuration()
        configuration.host = 'http://localhost:8080'
        api_client = ApiClient(configuration)
        self.classes_members = ClassesClassIdentifierMembers(api_client)

    def test_collection_members(self):
        results = self.classes_members.get(
            path_params={'class': 'collections', 'identifier': 'urn:nasa:pds:insight_rad:data_derived::7.0'},
            accept_content_types=('application/json',)
        ).body

        self.assertEqual(len(results), 2)  # add assertion here


if __name__ == '__main__':
    unittest.main()
