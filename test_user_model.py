"""User model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py


import os
from unittest import TestCase

from models import db, User, Message, Follows

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"


# Now we can import app

from app import app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()

user1 = User(
    email="test@test.com",
    username="testuser",
    password="HASHED_PASSWORD"
)

user2 = User(
    email="test2@test.com",
    username="testuser2",
    password="HASHED_PASSWORD",
)

class UserModelTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Message.query.delete()
        Follows.query.delete()

        self.client = app.test_client()

    def test_user_model(self):
        """Does basic model work?"""

        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()

        # User should have no messages & no followers
        self.assertEqual(len(u.messages), 0)
        self.assertEqual(len(u.followers), 0)

    def test_repr(self):
        """Test for a repr"""
        self.assertEqual(repr(user1), f'<User #{user1.id}: testuser, test@test.com>')

    def test_is_following(self):
        """Test if a user is following another user"""
        user1.following.append(user2)
        db.session.commit()

        # self.assertEqual(user2.is_following(self, user1), False)
        self.assertEqual(self.is_following(self,user2), True)





