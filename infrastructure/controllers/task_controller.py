from flask import Blueprint, request, jsonify
from application.services import TaskService
from infrastructure.repositories.in_memory_task_repository import InMemoryTaskRepository

task_blueprint = Blueprint('tasks', __name__)
repository = InMemoryTaskRepository()
task_service = TaskService(repository=repository)

@task_blueprint.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task = task_service.create_task(data['title'], data['description'])
    return jsonify(task.__dict__), 201

@task_blueprint.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = task_service.get_task(task_id)
    return jsonify(task.__dict__) if task else ('', 404)

@task_blueprint.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    task = task_service.update_task(task_id, data['title'], data['description'], data['status'])
    return jsonify(task.__dict__) if task else ('', 404)

@task_blueprint.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    result = task_service.delete_task(task_id)
    return ('', 204) if result else ('', 404)

@task_blueprint.route('/tasks', methods=['GET'])
def list_tasks():
    tasks = task_service.list_tasks()
    return jsonify([task.__dict__ for task in tasks])
