import Route from '@ember/routing/route';
import AuthenticatedRouteMixin from 'ember-simple-auth/mixins/authenticated-route-mixin';
import { alias } from '@ember/object/computed';
import { inject as service } from '@ember/service';

export default Route.extend(AuthenticatedRouteMixin, {
    session: service(),
    model: function() {
        // let username = this.get('session.data.authenticated.username');
        // return this.store.findRecord('user', username)
    },
});
