import Component from '@ember/component';
import { inject as service } from '@ember/service';
import { alias } from '@ember/object/computed';

export default Component.extend({
    classNames: ['comp-page-header'],
    session: service(),
    username: alias('session.data.authenticated.username'),
    authenticated: alias('session.session.isAuthenticated'),

    actions: {
        logout() {
            this.get('session').invalidate();
        }
    }
});
