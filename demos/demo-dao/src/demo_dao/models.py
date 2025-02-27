from tortoise import fields
from tortoise.fields.relational import ForeignKeyFieldInstance

from dipdup.models import Model


class DAO(Model):
    address = fields.CharField(36, pk=True)


class User(Model):
    address = fields.CharField(36, pk=True)
    balance = fields.IntField()


class Proposal(Model):
    id = fields.IntField(pk=True)
    dao: ForeignKeyFieldInstance[DAO] = fields.ForeignKeyField('models.DAO', 'proposals')
    # upvotes = fields.IntField(default=0)
    # downvotes = fields.IntField(default=0)
    # start_date = fields.DatetimeField()
    # metadata = fields.JSONField()
    # proposer = fields.ForeignKeyField('models.Address', 'proposals')


class Vote(Model):
    id = fields.IntField(pk=True)
    proposal: ForeignKeyFieldInstance[Proposal] = fields.ForeignKeyField('models.Proposal', 'votes')
    amount = fields.IntField()
