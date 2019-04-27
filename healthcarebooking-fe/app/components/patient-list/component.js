import Component from '@ember/component';
import { inject } from '@ember/service';
export default Component.extend({
    store: inject(),
    didInsertElement() {
        console.log('didInsertElement')
        this.store.query('user', {}).then(records => {
            this.set('patients', records);
        })
    },
});
