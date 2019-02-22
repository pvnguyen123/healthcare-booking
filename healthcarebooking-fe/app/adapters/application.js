import DS from 'ember-data';
import config from '../config/environment';
import DataAdapterMixin from 'ember-simple-auth/mixins/data-adapter-mixin';

export default DS.JSONAPIAdapter.extend(DataAdapterMixin, {
  namespace: 'api/v1',
  host: config.mainAPIServer,

  authorize(xhr) {
    let {
      access_token
    } = this.get('session.data.authenticated');
    xhr.setRequestHeader('Authorization', `Bearer ${access_token}`);
  },

  ajaxOptions: function () {
    let hash = this._super.apply(this, arguments);
    if (config.environment === 'development') {
      hash.xhrFields = {
        withCredentials: true
      };
    }
    return hash;
  },
});
