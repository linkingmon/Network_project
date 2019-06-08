from dbModel import UserAccounts, Message, db
from flask import Flask, session, redirect, render_template, request, flash, url_for, json, Response

# user_id = session.get('user_id')

message_data = db.session.query(
    Message,
    UserAccounts.MugShot
).join(
    UserAccounts,
    UserAccounts.UserName == Message.UserName
).all()
print(type(message_data[0]))
print(message_data)

# user_id = '666'
mug_shot_title = UserAccounts.query.filter_by(
    UserName=user_id).first().MugShot
print(mug_shot_title)

print(UserAccounts.query)
# user = UserAccounts.query.filter_by(UserName=username).first()
