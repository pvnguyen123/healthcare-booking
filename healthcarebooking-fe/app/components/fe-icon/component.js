import Component from '@ember/component';

export default Component.extend({
    tagName: "icon",
    height: 24,
    width: 24,
    "stroke-width": 2,

}).reopenClass({
    positionalParams: ['name']
});
