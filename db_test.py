from dbModel import UserAccounts, Message, db
from flask import Flask, session, redirect, render_template, request, flash, url_for, json, Response

# # user_id = session.get('user_id')

# message_data = db.session.query(
#     Message,
#     UserAccounts.MugShot
# ).join(
#     UserAccounts,
#     UserAccounts.UserName == Message.UserName
# ).all()
# print(type(message_data[0]))
# print(message_data)

user_id = '666'
UserAccounts.query.delete()
Message.query.delete()
# (UserAccounts.query.all())
print("XXXXXXXXXXXXXXXXXXXXXXXXXXX")
# print(user)
# print(user[10])
print("XXXXXXXXXXXXXXXXXXXXXXXXXXX")
# mug_shot_title = UserAccounts.query.filter_by(
#     UserName=user_id).first().MugShot
# print(mug_shot_title)

# print(UserAccounts.query)
# user = UserAccounts.query.filter_by(UserName=username).first()


# def clear_data(session):
#     meta = db.metadata
#     for table in reversed(meta.sorted_tables):
#         print('Clear table %s' % table)
#         session.execute(table.delete())
#     session.commit()


# clear_data(session)
