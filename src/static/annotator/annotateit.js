var $, AnnotateItPermissions, Annotator, Permissions,
  bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; },
  extend = function(child, parent) { for (var key in parent) { if (hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; },
  hasProp = {}.hasOwnProperty,
  indexOf = [].indexOf || function(item) { for (var i = 0, l = this.length; i < l; i++) { if (i in this && this[i] === item) return i; } return -1; };




$ = Annotator.Util.$;

AnnotateItPermissions = (function(superClass) {
  extend(AnnotateItPermissions, superClass);

  function AnnotateItPermissions() {
    this._setAuthFromToken = bind(this._setAuthFromToken, this);
    this.updateAnnotationPermissions = bind(this.updateAnnotationPermissions, this);
    this.updatePermissionsField = bind(this.updatePermissionsField, this);
    this.addFieldsToAnnotation = bind(this.addFieldsToAnnotation, this);
    return AnnotateItPermissions.__super__.constructor.apply(this, arguments);
  }

  AnnotateItPermissions.prototype.options = {
    showViewPermissionsCheckbox: true,
    showEditPermissionsCheckbox: true,
    groups: {
      world: 'group:__world__',
      authenticated: 'group:__authenticated__',
      consumer: 'group:__consumer__'
    },
    userId: function(user) {
      return user.userId;
    },
    userString: function(user) {
      return user.userId;
    },
    userAuthorize: function(action, annotation, user) {
      var action_field, permissions, ref, ref1, ref2, ref3;
      permissions = annotation.permissions || {};
      action_field = permissions[action] || [];
      if (ref = this.groups.world, indexOf.call(action_field, ref) >= 0) {
        return true;
      } else if ((user != null) && (user.userId != null) && (user.consumerKey != null)) {
        if (user.userId === annotation.user && user.consumerKey === annotation.consumer) {
          return true;
        } else if (ref1 = this.groups.authenticated, indexOf.call(action_field, ref1) >= 0) {
          return true;
        } else if (user.consumerKey === annotation.consumer && (ref2 = this.groups.consumer, indexOf.call(action_field, ref2) >= 0)) {
          return true;
        } else if (user.consumerKey === annotation.consumer && (ref3 = user.userId, indexOf.call(action_field, ref3) >= 0)) {
          return true;
        } else if (user.consumerKey === annotation.consumer && user.admin) {
          return true;
        } else {
          return false;
        }
      } else {
        return false;
      }
    },
    permissions: {
      'read': ['group:__world__'],
      'update': [],
      'delete': [],
      'admin': []
    }
  };

  AnnotateItPermissions.prototype.addFieldsToAnnotation = function(annotation) {
    if (annotation) {
      annotation.permissions = this.options.permissions;
      if (this.user) {
        annotation.user = this.user.userId;
        return annotation.consumer = this.user.consumerKey;
      }
    }
  };

  AnnotateItPermissions.prototype.updatePermissionsField = function(action, field, annotation) {
    var authzAnyone, input;
    field = $(field).show();
    input = field.find('input').removeAttr('disabled');
    if (!this.authorize('admin', annotation)) {
      field.hide();
    }
    authzAnyone = this.authorize(action, annotation || {}, {
      userId: '__nonexistentuser__',
      consumerKey: this.user.consumerKey
    });
    if (this.user && authzAnyone) {
      return input.attr('checked', 'checked');
    } else {
      return input.removeAttr('checked');
    }
  };

  AnnotateItPermissions.prototype.updateAnnotationPermissions = function(type, field, annotation) {
    var dataKey, group;
    if (!annotation.permissions) {
      annotation.permissions = this.options.permissions;
    }
    dataKey = type + '-permissions';
    if ($(field).find('input').is(':checked')) {
      if (type === 'read') {
        group = this.options.groups.world;
      } else {
        group = this.options.groups.consumer;
      }
      return annotation.permissions[type] = [group];
    } else {
      return annotation.permissions[type] = [];
    }
  };

  AnnotateItPermissions.prototype._setAuthFromToken = function(token) {
    return this.setUser(token);
  };

  return AnnotateItPermissions;

})(Permissions);

Annotator.Plugin.register('AnnotateItPermissions', AnnotateItPermissions);

module.exports = AnnotateItPermissions;