import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default Route.extend({
    session: service(),
    actions : {
        authenticate(identification, password) {
            // let { identification, password } = this.getProperties('identification', 'password');
            this.get('session').authenticate('authenticator:oauth2', identification, password)
                .then( ()=> {
                    this.transitionTo('protected.profiles')
                })
                .catch((reason) => {
                  this.set('errorMessage', reason.error || reason);
                });
        }
    }
});
