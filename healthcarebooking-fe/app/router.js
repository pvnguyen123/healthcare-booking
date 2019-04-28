import EmberRouter from '@ember/routing/router';
import config from './config/environment';

const Router = EmberRouter.extend({
  location: config.locationType,
  rootURL: config.rootURL
});

Router.map(function() {
  this.route('login');
  this.route('protected', function() {
    this.route('bookings');
    this.route('requests');
    this.route('history');
    this.route('providers');
    this.route('clients');
    this.route('tasks');
    this.route('profiles', { path: 'profiles/:id' });
  });
  this.route('admin');

  this.route('registercompany');

  this.route('register');

});

export default Router;
