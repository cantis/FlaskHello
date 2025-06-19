from .extensions import db


# Model for storing test values
class TestValue(db.Model):
    """Model for a test value entry."""

    def __init__(self, value: str) -> None:
        super().__init__()
        self.value = value

    id: int = db.Column(db.Integer, primary_key=True)
    value: str = db.Column(db.String(120), nullable=False)
