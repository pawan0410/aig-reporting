from datetime import datetime

from emr.extensions import db
from emr.medsteamdb.mssql import med_streaming_emr_db_connection
from emr.medsteamdb.mssql import med_streaming_emr_db


class Resources(db.Model):
    __tablename__ = 'resources'

    id = db.Column(db.Integer, primary_key=True)
    resource_id = db.Column(db.Integer, unique=True)
    resource_name = db.Column(db.String(255))
    last_execution = db.Column(db.Date)

    @staticmethod
    def load():
        r = Resources.query.\
            filter(Resources.last_execution == datetime.today().strftime('%Y-%m-%d')).\
            first()

        if not r and med_streaming_emr_db_connection:
            med_streaming_emr_db.execute("EXEC GetResource @OnlyActive=1")
            rows = med_streaming_emr_db.fetchall()
            context = {row['RESOURCEID']: row['RESOURCENAME'] for row in rows}

            db.session.query(Resources).delete(synchronize_session='evaluate')
            db.session.add_all(
                [Resources(
                    resource_id=c,
                    resource_name=context[c],
                    last_execution=datetime.today().strftime('%Y-%m-%d')
                ) for c in context]
            )
            db.session.commit()

    @staticmethod
    def resources():
        rows = Resources.query.all()
        return {row.resource_id: row.resource_name for row in rows}


class GroupResource(db.Model):
    __tablename__ = 'group_resource'

    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(255), unique=True)
    group_order = db.Column(db.Integer)

    @staticmethod
    def save(group_name, group_order):
        group = GroupResource(group_name=group_name, group_order=group_order)
        db.session.add(group)
        db.session.commit()
        return group.id


class ResourceGroup(db.Model):
    __tablename__ = 'resource_group'

    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer)
    resource_id = db.Column(db.Integer)

    @staticmethod
    def save(group_id, resources):
        ResourceGroup.query.filter(ResourceGroup.group_id == group_id).delete()
        db.session.add_all([ResourceGroup(group_id=group_id, resource_id=r) for r in resources])
        db.session.commit()


class ResourcesSlots(db.Model):
    __tablename__ = 'resource_slots'

    id = db.Column(db.Integer, primary_key=True)
    resource_id = db.Column(db.Integer)
    value = db.Column(db.Integer)

    """
    Defines resources slots
    """

    @staticmethod
    def save(context):
        db.session.add_all([ResourcesSlots(resource_id=c, value=context[c]) for c in context])
        db.session.commit()

    @staticmethod
    def slots():
        return {r.resource_id: r.value for r in ResourcesSlots.query.all()}
