"""User model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py


from app import app
import os
from unittest import TestCase

from models import db, User, Message, Follows, Favorite

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"


# Now we can import app


# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()

NEW_USER = User(
    email="test@test.com",
    username="testuser",
    password="HASHED_PASSWORD"
)

NEW_USER_2 = User(
    email="test12@test.com",
    username="testuser12",
    password="HASHED_PASSWORD",
)


class UserModelTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Message.query.delete()
        Follows.query.delete()
        Favorite.query.delete()

        user1 = User(
            email="test1@test.com",
            username="testuser1",
            password="HASHED_PASSWORD"
        )

        user2 = User(
            email="test2@test.com",
            username="testuser2",
            password="HASHED_PASSWORD",
        )

        db.session.add_all([user1, user2])
        db.session.commit()

        self.client = app.test_client()
        self.user1 = user1
        self.user2 = user2

    def test_user_model(self):
        """Does basic model work?"""

        db.session.add(NEW_USER)
        db.session.commit()

        # User should have no messages & no followers
        self.assertEqual(len(NEW_USER.messages), 0)
        self.assertEqual(len(NEW_USER.followers), 0)

    def test_repr(self):
        """Test for a repr"""

        self.assertEqual(
            repr(NEW_USER), f'<User #{NEW_USER.id}: testuser, test@test.com>')

    def test_is_following(self):
        """Test if a user is following another user"""

        NEW_USER.following.append(User.query.get(NEW_USER_2.id))
        # PAUSE HERE.

        db.session.commit()

        self.assertEqual(NEW_USER.is_following(NEW_USER_2), True)
        self.assertEqual(NEW_USER_2.is_following(NEW_USER), False)

    # def test_is_followed_by(self):
    #     """Test if a user is followed by another user"""

    #     NEW_USER.following.append(NEW_USER_2.id)
    #     db.session.commit()

    #     self.assertEqual(NEW_USER.is_followed_by(NEW_USER_2), False)
    #     self.assertEqual(NEW_USER_2.is_followed_by(NEW_USER), True)

    # def test_User_create(self):
    #     """ Tests if new user created with valid credentials """

    #     u = User(
    #         email="test@test.com",
    #         username="testuser",
    #         password="HASHED_PASSWORD"
    #     )

    #     db.session.add(u)
    #     db.session.commit()

    #     users = User.query.all()

    #     # users table should have 1 user
    #     self.assertEqual(len(users), 1)
