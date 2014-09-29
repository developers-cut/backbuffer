// Backbuffer.dart
// Main Dart file for Backbuffer.
import 'dart:html';

// Represents Data locally.
/*class DataModel {
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
}*/

ButtonElement add_label_button;
Element label_fields_container;
Element first_label_field;

void main() {
    add_label_button = querySelector('#add-label-button');
    label_fields_container = querySelector('#label-fields-container');
    first_label_field = querySelector(
        '#label-fields-container input[name="label"]');
    add_label_button.onClick.listen(addLabelField);
}

void addLabelField(Event e) {
    label_fields_container.append(first_label_field.clone(true));
}
