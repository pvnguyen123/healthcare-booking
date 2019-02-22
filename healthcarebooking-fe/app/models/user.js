import DS from 'ember-data';

export default DS.Model.extend({
    username: DS.attr(),
    email: DS.attr(),
    active: DS.attr(),
    password: DS.attr(),
});
