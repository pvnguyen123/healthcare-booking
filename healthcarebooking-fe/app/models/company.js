import DS from 'ember-data';

export default DS.Model.extend({
    name: DS.attr(),
    email: DS.attr(),
    phone: DS.attr(),
    active: DS.attr(),
    address_id: DS.attr(),
    created: DS.attr(),
    last_updated: DS.attr(),

    clients: DS.hasMany('profile', {async: true}),
    providers: DS.hasMany('profile', {async: true})
});
