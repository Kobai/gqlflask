from models import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.schema import Index
import uuid
import datetime

class BidFile(db.Model):
	__tablename__ = 'bid_file'
	__table_args__ = (Index('bookings_partner_name_partner_id_index', 'channel', 'uploaded_at', unique=True), )

	# id = db.Column(UUID(as_uuid=True), unique=True, nullable=False, primary_key=True)
	id = db.Column(UUID(as_uuid=True), unique=True, default=uuid.uuid4(), primary_key=True)
	channel = db.Column(db.String, index=True)
	created_at = db.Column(db.DateTime(timezone=True), default=db.func.now())
	uploaded_at = db.Column(db.DateTime(timezone=True), default=db.func.now())
	updated_at = db.Column(db.DateTime(timezone=True), default=db.func.now(), onupdate=db.func.now())
	stored_at = db.Column(db.String)

	def __repr__(self):
		return str(self.id)


