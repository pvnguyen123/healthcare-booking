import Component from '@ember/component';
import { inject as service } from '@ember/service';
import { alias } from '@ember/object/computed';

export default Component.extend({
  session: service(),
  tagName: '',
  homeSubmenuCollapse: true,
  pageSubmenuCollapse: true,

  username: alias('session.data.authenticated.username'),
  authenticated: alias('session.session.isAuthenticated'),
  actions: {
    logout() {
      this.get('session').invalidate();
    }
  }
});
