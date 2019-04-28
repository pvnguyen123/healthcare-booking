import Route from '@ember/routing/route';

export default Route.extend({
    model(params) {
        return this.store.findRecord('company', params.id)
    },
    setupController(controller, model) {
        // Call _super for default behavior
        this._super(controller, model);
        // Implement your custom setup after
        let data = {
            datasets: [{
                data: [10, 20, 30],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                ],
            }],

            // These labels appear in the legend and in the tooltips when hovering different arcs
            labels: [
                'Open',
                'Completed',
                'In Progress'
            ]
        };

        controller.set('data', data)
      }
});
