import Route from '@ember/routing/route';

export default Route.extend({
    model() {
        return this.store.createRecord('user');
    },
    actions: {
        submit(model) {
            // Todo validate form
            model.save().then(user => {
                this.transitionTo('login');
            });
        }
    }
});
