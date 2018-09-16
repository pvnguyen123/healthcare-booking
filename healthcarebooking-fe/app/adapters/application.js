import DS from 'ember-data';
import config from '../config/environment';
import DataAdapterMixin from 'ember-simple-auth/mixins/data-adapter-mixin';


export default DS.JSONAPIAdapter.extend(DataAdapterMixin, {
    namespace: 'api/v1',
    host: config.mainAPIServer,

    authorize(xhr) {
        let { access_token } = this.get('session.data.authenticated');
        xhr.setRequestHeader('Authorization', `Bearer ${access_token}`);
    },

    ajaxOptions: function () {
        var hash = this._super.apply(this, arguments);
        hash.xhrFields = {
          withCredentials: true
        };
        return hash;
    },
    handleResponse (status, headers, payload, requestData) {
        if(!this.isSuccess(status, headers, payload)) {
            if(payload.message) {
                // Normalize the error response where payload is {message: ''}
                return new DS.AdapterError([{detail: payload.message}]);
            }
        }
        return this._super(...arguments);
    }
});
