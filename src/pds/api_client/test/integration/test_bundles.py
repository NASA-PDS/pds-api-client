import unittest
from pds.api_client import Configuration
from pds.api_client import ApiClient
from pds.api_client.apis.paths.bundles_identifier_collections_all import BundlesIdentifierCollectionsAll
from pds.api_client.apis.paths.classes_class_identifier_members import ClassesClassIdentifierMembers

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # create an instance of the API class
        configuration = Configuration()
        configuration.host = 'http://localhost:8080'
        api_client = ApiClient(configuration)
        self.bundlesCollections = ClassesClassIdentifierMembers(api_client)

    def test_collections_of_a_bundle_default(self):

        results = self.bundlesCollections.get(
            path_params={
                'class': 'bundles',
                'identifier': 'urn:nasa:pds:insight_rad::2.1'
            },
            query_params={'fields': ['ops:Data_File_Info.ops:file_ref']},
            accept_content_types=('application/json',)
        ).body
        for collection in results.data:
            urls = collection['properties']['ops:Data_File_Info.ops:file_ref']
            for url in urls:
                print(url)

    def test_all_collections_of_a_bundle_as_deep_archive_does(self):

        def get_collections(bundle_lidvid):
            _apiquerylimit = 50
            _propdataurl = "ops:Data_File_Info.ops:file_ref"
            _propdatamd5 = "ops:Data_File_Info.ops:md5_checksum"
            _proplabelurl = "ops:Label_File_Info.ops:file_ref"
            _proplabelmd5 = "ops:Label_File_Info.ops:md5_checksum"
            _fields = [_propdataurl, _propdatamd5, _proplabelurl, _proplabelmd5]

            start = 0

            found_something = True
            while found_something:
                page = self.bundlesCollections.get(
                    path_params={
                        'class': 'bundles',
                        'identifier': bundle_lidvid
                    },
                    query_params={'start': start, 'limit':_apiquerylimit, 'fields': _fields},
                    accept_content_types=('application/json',)
                ).body

                found_something = False
                for c in page.data:
                    found_something = True
                    yield c
                start += len(page.data)

        n = 0
        for collection in get_collections("urn:nasa:pds:insight_rad::2.1"):
            print(collection['id'])
            n += 1

        assert n == 2  # 2 collections found in this bundle


if __name__ == '__main__':
    unittest.main()
