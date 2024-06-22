from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class IPersistenceManager(ABC):
    """
    Interface for a persistence manager.
    """

    @abstractmethod
    def save(self, entity):
        """
        Save an entity.

        Args:
            entity: The entity to be saved.
        """
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
        """
        Get an entity.

        Args:
            entity_id: The ID of the entity.
            entity_type: The type of the entity.

        Returns:
            The retrieved entity.
        """
        pass

    @abstractmethod
    def update(self, entity):
        """
        Update an entity.

        Args:
            entity: The entity to be updated.
        """
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):
        """
        Delete an entity.

        Args:
            entity_id: The ID of the entity.
            entity_type: The type of the entity.
        """
        pass