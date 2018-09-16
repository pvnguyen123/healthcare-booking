import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';
import AuthenticatedRouteMixin from 'ember-simple-auth/mixins/authenticated-route-mixin';

export default Route.extend(AuthenticatedRouteMixin, {
    session: service(),
    model: function() {
        let username = this.get('session.data.authenticated.username');
        return this.store.findRecord('user', username)
    },
});
