from models import *


def populate():
  db.session.add(User(
      email='user1@example.com',
      password='12345',
      name='Vidu'
  ))
  db.session.add(User(
      email='user2@example.com',
      password='12345',
      name='Rahul'
  ))

  db.session.add(Post(
      user_id=1,
      body='Hello, this is postbook'
  ))
  db.session.add(Post(
      user_id=1,
      body='Hello, this is postbook-2'
  ))
  db.session.add(Post(
      user_id=2,
      body='Hello, I am rahul.'
  ))

  db.session.add(Like(
      post_id=1,
      user_id=1
  ))

  db.session.add(Like(
      post_id=2,
      user_id=1
  ))
  db.session.add(Like(
      post_id=2,
      user_id=2
  ))
  db.session.commit()
