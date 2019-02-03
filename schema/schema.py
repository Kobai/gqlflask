import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import *

# Objects
class BidFileObject(SQLAlchemyObjectType):
	class Meta:
		model = BidFile
		interfaces = (graphene.relay.Node, )

# Queries 
class Query(graphene.ObjectType):
	node = graphene.relay.Node.Field()
	all_bids = SQLAlchemyConnectionField(BidFileObject)


# Mutations
class CreateBid(graphene.Mutation):
	class Arguments:
		channel = graphene.String(required=True)
		stored_at = graphene.String(required=True)
	bid = graphene.Field(lambda: BidFileObject)

	def mutate(self, info, channel, stored_at):
		bid = BidFile(channel=channel, stored_at=stored_at)
		db.session.add(bid)
		db.session.commit()
		return CreateBid(bid=bid)

class Mutation(graphene.ObjectType):
	create_bid = CreateBid.Field() 



