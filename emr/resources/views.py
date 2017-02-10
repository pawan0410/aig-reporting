import json
from collections import defaultdict
from operator import itemgetter

from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask_login import login_required

from emr.models.resources import Resources
from emr.models.resources import GroupResource
from emr.models.resources import ResourceGroup
from emr.models.resources import ResourcesSlots
from emr.extensions import db


resources_blueprint = Blueprint('resources', __name__, url_prefix='/resources')


@resources_blueprint.route('', methods=['GET', 'POST'])
@resources_blueprint.route('/<int:id>', methods=['GET', 'POST'])
@login_required
def index(id=None):
    Resources.load()

    resources = Resources.resources()
    resources_group_raw = [{'id': rg.id, 'name': rg.group_name, 'order': rg.group_order} for rg in GroupResource.query.all()]

    group_resource_data = [{rgq.group_id: rgq.resource_id} for rgq in ResourceGroup.query.filter(ResourceGroup.group_id.in_(
        [_r['id'] for _r in resources_group_raw]
    )).all()]

    group_resource = defaultdict(list)
    for grd in group_resource_data:
        for i, v in grd.items():
            group_resource[i].append(v)

    resources_group = []
    for rgr in resources_group_raw:
        resources_group.append({
            'id': rgr['id'],
            'name': rgr['name'],
            'count': len(group_resource[rgr['id']]),
            'order': rgr['order']
        })

    resources_group = sorted(resources_group, key=itemgetter('order'))
    group_name = ''
    selected_resources = []
    if request.method == 'POST':
        name = request.form.get('name', type=str)
        selected_resources = request.form.getlist('resources[]')

        if id:
            g = GroupResource.query.get(id)
            g.group_name = name
            db.session.add(g)
            db.session.commit()
            group_id = g.id
        else:
            group_id = GroupResource.save(name, 0)

        if group_id:
            ResourceGroup.save(group_id, selected_resources)

        return redirect(url_for('resources.index'))

    if id:
        group_name = GroupResource.query.get(id).group_name
        selected_resources = [
            ri.resource_id for ri in ResourceGroup.query.filter(ResourceGroup.group_id == id).all()
            ]
    resources_slots = {rs.resource_id: rs.value for rs in ResourcesSlots.query.all()}
    return render_template(
        'resources/index.html',
        resources=resources,
        resources_group=resources_group,
        id=id,
        group_name=group_name,
        selected_resources=selected_resources,
        resources_slots=resources_slots
    )


@resources_blueprint.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id=None):
    GroupResource.query.filter(GroupResource.id == id).delete()
    ResourceGroup.query.filter(ResourceGroup.group_id == id).delete()
    db.session.commit()
    return redirect(url_for('resources.index'))


@resources_blueprint.route('/group_order', methods=['POST'])
def group_order():
    orders = json.loads(request.form.get('orders'))

    for i, v in orders.items():
        g = GroupResource.query.get(i)
        g.group_order = v
        db.session.add(g)
    db.session.commit()
    return 'success'


@resources_blueprint.route('/slots', methods=['GET', 'POST'])
def slots():
    if request.method == 'POST':
        db.session.query(ResourcesSlots).delete(synchronize_session='evaluate')
        context = json.loads(request.form.get('slots', type=str))
        ResourcesSlots.save(context)
        return 'success'

    return ''

