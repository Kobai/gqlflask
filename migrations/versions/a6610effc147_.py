"""empty message

Revision ID: a6610effc147
Revises: 
Create Date: 2019-02-02 13:23:32.433757

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a6610effc147'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bid_file',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('channel', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('uploaded_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('stored_at', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index('bookings_partner_name_partner_id_index', 'bid_file', ['channel', 'uploaded_at'], unique=True)
    op.create_index(op.f('ix_bid_file_channel'), 'bid_file', ['channel'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_bid_file_channel'), table_name='bid_file')
    op.drop_index('bookings_partner_name_partner_id_index', table_name='bid_file')
    op.drop_table('bid_file')
    # ### end Alembic commands ###