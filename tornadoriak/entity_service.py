# -*- coding: utf-8 -*-
"""

    tornado-riak

    by hgschmidt

    Copyright (c) 2012-2013 apitrary

"""
import logging
from tornadoriak.header_service import HeaderService
from tornadoriak.errors import RiakObjectNotFoundException
from tornadoriak.errors import RiakObjectIdNotProvidedException
from tornadoriak.riak_entity_repository import RiakEntityRepository


class EntityService(HeaderService):
    """
        Handle all calls in order to work with entities (from Riak)
    """

    def __init__(self, headers, riak_client, bucket, bucket_name):
        """
            Additionally, add the RiakService.
        """
        super(EntityService, self).__init__(headers)
        self.riak_client = riak_client
        self.bucket_name = bucket_name
        self.bucket = bucket

        self.repository = RiakEntityRepository(riak_client=riak_client, bucket=bucket, bucket_name=bucket_name)

    def get(self, object_id):
        """
            GET a single object with given object ID
        """
        result = None
        try:
            result = self.repository.fetch(object_id)
        except RiakObjectIdNotProvidedException(), e:
            logging.error('Provided object ID is invalid. Error: {}'.format(e))
        except RiakObjectNotFoundException, e:
            logging.error('Object with provided Id not found in database. Error: {}'.format(e))
        return result

    def get_all(self):
        """
            Get all objects from this bucket
        """
        return self.repository.fetch_all()

    def add(self, object_id, data):
        """
            Create an object in database
        """
        return self.repository.add(object_id=object_id, data=data)

    def update(self, object_id, data):
        """
            Update a given object. Runs the same steps as in post.
        """
        return self.repository.add(object_id=object_id, data=data)

    def delete(self, object_id):
        """
            Delete an object with given object id.
        """
        return self.repository.remove(object_id=object_id)

    def search(self, search_query):
        """
            Search within this entity's bucket.

            Used in GET (EntityHandlers).
        """
        search_query = self.riak_client.search(self.bucket_name, search_query)
        logging.debug('search_query: {}'.format(search_query))
        search_response = []
        for result in search_query.run():
            # Getting ``RiakLink`` objects back.
            obj = result.get()
            obj_data = obj.get_data()
            kv_object = {'_id': result._key, '_data': obj_data}
            search_response.append(kv_object)

        return search_response
