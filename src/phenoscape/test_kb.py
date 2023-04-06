import unittest
from unittest.mock import patch, Mock
import phenoscape.kb as pkb


class TestTermFunctions(unittest.TestCase):
    @patch("phenoscape.kb.requests")
    def test_get_term(self, mock_requests):
        response = Mock()
        mock_requests.get.return_value = response
        response.json.return_value = {"@id": "someIRI"}

        result = pkb.get_term(iri="http://purl.obolibrary.org/obo/UBERON_0011618")

        self.assertEqual(result, {"@id": "someIRI"})
        mock_requests.get.assert_called_with(
            f"{pkb.KB_API_URL}/term",
            params={"iri": "http://purl.obolibrary.org/obo/UBERON_0011618"},
        )

    @patch("phenoscape.kb.requests")
    def test_term_search(self, mock_requests):
        response = Mock()
        mock_requests.get.return_value = response
        response.json.return_value = {
            "results": [
                {"@id": "someIRI", "matchType": "exact"},
                {"@id": "otherIRI", "matchType": "broad"},
            ]
        }

        result = pkb.term_search(text="dorsal fin", match_types=["exact"])

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], {"@id": "someIRI", "matchType": "exact"})
        mock_requests.get.assert_called_with(
            f"{pkb.KB_API_URL}/term/search", params={"text": "dorsal fin"}
        )

    @patch("phenoscape.kb.requests")
    def test_term_search_bad_match_types(self, mock_requests):
        response = Mock()
        mock_requests.get.return_value = response
        response.json.return_value = {
            "results": [
                {"@id": "someIRI", "matchType": "exact"},
                {"@id": "otherIRI", "matchType": "broad"},
            ]
        }
        with self.assertRaises(ValueError) as raised_exception:
            pkb.term_search(text="dorsal fin", match_types=["best"])
        expected_error = "Invalid match_types parameter (['best']). Valid match types are 'exact', 'partial', and 'broad'."
        self.assertEqual(str(raised_exception.exception), expected_error)


if __name__ == "__main__":
    unittest.main()
