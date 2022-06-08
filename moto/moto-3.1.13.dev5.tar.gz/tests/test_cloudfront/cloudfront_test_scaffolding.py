# Example distribution config used in tests in both test_cloudfront.py
# as well as test_cloudfront_distributions.py.


def example_distribution_config(ref):
    """Return a basic example distribution config for use in tests."""
    return {
        "CallerReference": ref,
        "Origins": {
            "Quantity": 1,
            "Items": [
                {
                    "Id": "origin1",
                    "DomainName": "asdf.s3.us-east-1.amazonaws.com",
                    "S3OriginConfig": {"OriginAccessIdentity": ""},
                }
            ],
        },
        "DefaultCacheBehavior": {
            "TargetOriginId": "origin1",
            "ViewerProtocolPolicy": "allow-all",
            "MinTTL": 10,
            "ForwardedValues": {"QueryString": False, "Cookies": {"Forward": "none"}},
        },
        "Comment": "an optional comment that's not actually optional",
        "Enabled": False,
    }
