"“”Message model tests.“”"
# run these tests like:
#
#    python -m unittest test_user_model.py
import os
from unittest import TestCase
from models import db, User, Message, Follows, Favorite
# BEFORE we import our app, let’s set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database
os.environ[‘DATABASE_URL’] = “postgresql: // /warbler-test”

from app import app

db.create_all()


class MessageModelTestCase(TestCase):
    “”"Test for the Message model.“”"

    def setUp(self):
        User.query.delete()
        Message.query.delete()
        Follows.query.delete()
        self.client = app.test_client()
        user1 = User.signup(
            email=“alaa@alaa.com”,
            username=“amohamed”,
            password=‘PASSWORD’,
            image_url=None
        )
        db.session.add(user1)
        db.session.commit()
        test_message = Message(user1.id, text=‘Hello World’,
                               user_id=user1.id, timestamp=datetime.utcnow())
        db.session.add(test_message)
        db.session.commit()
        self.user1 = user1
        self.test_message = test_mess

    def test_message_model(self):
        self.assertEqual(Message.query.count(), 1)

    def test_text(self):
        test_query = Message.query.filter_by(username=“amohamed”).one()
        self.assertEqual(test_query.text, ‘Hello World’)
        self.assertNotEqual(test_query.text, ‘Hello World2’)

    def test_user_id(self):
        test_query = Message.query.filter_by(username=“amohamed”).one()
        self.assertEqual(test_query.user_id, 1)
        self.assertNotEqual(test_query.user_id, 2)
