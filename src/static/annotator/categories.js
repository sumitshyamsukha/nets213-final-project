var bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; },
  extend = function(child, parent) { for (var key in parent) { if (hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; },
  hasProp = {}.hasOwnProperty;

Annotator.Plugin.Categories = (function(superClass) {
  extend(Categories, superClass);

  Categories.prototype.events = {
    'annotationCreated': 'setHighlights'
  };

  Categories.prototype.field = null;

  Categories.prototype.input = null;

  Categories.prototype.options = {
    categories: {}
  };

  function Categories(element, categories) {
    this.setAnnotationCat = bind(this.setAnnotationCat, this);
    this.updateField = bind(this.updateField, this);
    this.options.categories = categories;
  }

  Categories.prototype.pluginInit = function() {
    var cat, color, i, isChecked, ref;
    if (!Annotator.supported()) {
      return;
    }
    i = 0;
    ref = this.options.categories;
    for (cat in ref) {
      color = ref[cat];
      if (i === 0) {
        isChecked = true;
      } else {
        isChecked = false;
      }
      i = i + 1;
      this.field = this.annotator.editor.addField({
        type: 'radio',
        label: cat,
        value: cat,
        hl: color,
        checked: isChecked,
        load: this.updateField,
        submit: this.setAnnotationCat
      });
    }
    this.viewer = this.annotator.viewer.addField({
      load: this.updateViewer
    });
    if (this.annotator.plugins.Filter) {
      this.annotator.plugins.Filter.addFilter({
        label: 'Categories',
        property: 'category',
        isFiltered: Annotator.Plugin.Categories.filterCallback
      });
    }
    return this.input = $(this.field).find(':input');
  };

  Categories.prototype.setViewer = function(viewer, annotations) {
    var v;
    return v = viewer;
  };

  Categories.prototype.setHighlights = function(annotation) {
    var cat, h, highlights, j, len, results;
    cat = annotation.category;
    highlights = annotation.highlights;
    if (cat) {
      results = [];
      for (j = 0, len = highlights.length; j < len; j++) {
        h = highlights[j];
        results.push(h.className = h.className + ' ' + this.options.categories[cat]);
      }
      return results;
    }
  };

  Categories.prototype.updateField = function(field, annotation) {
    var category;
    category = '';
    if (field.checked = 'checked') {
      category = annotation.category;
    }
    return this.input.val(category);
  };

  Categories.prototype.setAnnotationCat = function(field, annotation) {
    if (field.childNodes[0].checked) {
      return annotation.category = field.childNodes[0].id;
    }
  };

  Categories.prototype.updateViewer = function(field, annotation) {
    field = $(field);
    if (annotation.category != null) {
      return field.addClass('annotator-category').html(function() {
        var string;
        return string = $.map(annotation.category, function(cat) {
          return '<span class="annotator-hl annotator-hl-' + annotation.category + '">' + Annotator.$.escape(cat).toUpperCase() + '</span>';
        }).join('');
      });
    } else {
      return field.remove();
    }
  };

  return Categories;

})(Annotator.Plugin);