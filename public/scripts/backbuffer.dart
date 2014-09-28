// Backbuffer.dart
// Main Dart file for Backbuffer.
import 'dart:html';

ButtonElement add_label_button;
Element label_fields_container;

void main() {
    add_label_button = querySelector('#add-label-button');
    label_fields_container = querySelector('#label-fields-container');
    add_label_button.onClick.listen(addLabelField);
}

void addLabelField(Event e) {
    TextInputElement new_label_field = new TextInputElement();
    new_label_field.setAttribute('name', 'label');
    label_fields_container.append(new_label_field);
}
