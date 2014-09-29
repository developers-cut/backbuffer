// Backbuffer.dart
// Main Dart file for Backbuffer.
import 'dart:html';
import 'dart:convert';

// Represents Data locally.
class DataModel {
    String title;
    String description;
    bool closed;
    List<String> label_list;
}

class TaskListViewController {
    List<Data> data_list;

    // Constructor loads
    TaskListViewController() {

    }
}



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
