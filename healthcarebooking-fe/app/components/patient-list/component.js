import Component from '@ember/component';
import { inject } from '@ember/service';
export default Component.extend({
    store: inject(),
    didInsertElement() {
        console.log('didInsertElement')
        console.log(this.get('patients.firstObject'))
    },
}).reopenClass({
    positionalParams: ['clients']
});

