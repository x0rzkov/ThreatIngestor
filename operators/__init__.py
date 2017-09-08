class Operator:
    """Base class, see method documentation"""

    def __init__(self):
        """Override with the same signature
            
        Example:
        
        >>> self.artifact_types = [artifacts.IPAddress, artifacts.Domain]
        """
        self.artifact_types = []

    def handle_artifact(self, artifact):
        """Override with the same signature"""
        raise NotImplementedError()

    def process(self, artifacts):
        """Process all applicable artifacts"""
        for artifact in artifacts:
            if any(isinstance(artifact, t) for t in self.artifact_types):
                self.handle_artifact(artifact)
