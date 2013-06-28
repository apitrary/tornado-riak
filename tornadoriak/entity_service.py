# -*- coding: utf-8 -*-
"""

    pygenapi

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
import logging
from tornadoriak.errors import RiakObjectIdNotProvidedException, RiakObjectNotFoundException
from tornadoriak.riak_entity_repository import RiakEntityRepository
from tornadoriak.header_service import HeaderService


class EntityService(HeaderService):
    """
        Handle all calls in order to work with entities (from Riak)
    """

    def __init__(self, headers, riak_client, bucket, bucket_name):
        """
            Additionally, add the RiakService.
        """
        super(EntityService, self).__init__(headers)

        # Set the Riak client, bucket name and bucket
        self.riak_client = riak_client
        self.bucket_name = bucket_name
        self.bucket = bucket

        # Establish the repository to Riak
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
