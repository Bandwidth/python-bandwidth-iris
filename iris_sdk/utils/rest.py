#!/usr/bin/env python

from future.utils import raise_from

import requests
from xml.etree import ElementTree

ERROR_TAG = "ErrorList"
ERROR_TEMPLATE = "{} Iris error: {}"
HEADERS = {"content-type": "application/xml"}
HTTP_OK = 200
HTTP_OK_MAX = 299

class RestError(Exception):
    pass

class RestClient(object):

    """
    HTTP requests wrapper.
    """

    def request(self, method, url, auth, params=None, data=None,headers=None):

        assert method in ("GET", "POST", "DELETE", "PUT")

        response = None
        try:
            response = requests.request(method, url, auth=auth,
                headers=(HEADERS if headers is None else headers),
                data=data, params=params)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as http_exception:
            # Logical errors in response body
            if (response is not None and
                not response.content == b"" and
                response.status_code>HTTP_OK_MAX):
                error_msg = None
                try:
                    root = ElementTree.fromstring(response.content)
                    msg_node = root
                    # Data responses
                    el = root.find(ERROR_TAG)
                    if el is None:
                        children = root.getchildren()
                        for elem in children:
                            el = elem.find(ERROR_TAG)
                            if el is not None:
                                break
                    msg_node = (el if el is not None else msg_node)
                    error_msg = ERROR_TEMPLATE.format(
                        msg_node[0][0].text, msg_node[0][1].text)
                except:
                    error_msg = response.content
                # Suppress the HTTP exception
                raise_from(RestError(error_msg), None)
            else:
                raise http_exception