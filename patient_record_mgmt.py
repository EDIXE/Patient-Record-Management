import csv
import graphviz
from binary_search_tree import BinarySearchTree, Node

class PatientRecord:
    def __init__(self, patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.blood_pressure = blood_pressure
        self.pulse = pulse
        self.body_temperature = body_temperature

    def __str__(self):
        return (f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, "
                f"Diagnosis: {self.diagnosis}, Blood Pressure: {self.blood_pressure}, "
                f"Pulse: {self.pulse}, Body Temperature: {self.body_temperature}")

class PatientRecordManagementSystem:
    def __init__(self):
        self.bst = BinarySearchTree()

    def add_patient_record(self, patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature):
        patient_record = PatientRecord(patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature)
        self.bst.insert(Node(patient_id, patient_record))

    def search_patient_record(self, patient_id):
        node = self.bst.search(patient_id)
        if node:
            return str(node.value)
        return f"Patient ID {patient_id} not found."

    def delete_patient_record(self, patient_id):
        self.bst.remove(patient_id)

    def display_all_records(self):
        print("Patient Records (Inorder Traversal):")
        self.bst.inorder_traversal(self.bst.root)

    def build_tree_from_csv(self, file_path):
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.add_patient_record(
                    int(row['PatientID']),
                    row['Name'],
                    int(row['Age']),
                    row['Diagnosis'],
                    row['BloodPressure'],
                    int(row['Pulse']),
                    float(row['BodyTemperature'])
                )

    def visualize_tree(self, output_file="tree"):
        dot = graphviz.Digraph(format='png')  # Specify the format upfront for clarity
        self._add_nodes(dot, self.bst.root)
        dot.render(output_file, cleanup=True)  # Render the graph to file and remove temporary files
        print(f"Tree visualization saved as {output_file}.png")

    def _add_nodes(self, dot, node):
        if node:
        # Correct the label to show both patient ID and name
            label = f"{node.value.patient_id}: {node.value.name}"
        
        # Create the node with the correct label format
            dot.node(str(node.key), label=label)
        
        # Recursively add left and right child nodes
            if node.left:
                dot.edge(str(node.key), str(node.left.key))
                self._add_nodes(dot, node.left)
            if node.right:
                dot.edge(str(node.key), str(node.right.key))
                self._add_nodes(dot, node.right)


