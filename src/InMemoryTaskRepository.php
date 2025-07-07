<?php
namespace App;

class InMemoryTaskRepository implements TaskRepositoryInterface {
    private array $tasks = [];
    private int $nextId = 1;

    public function save(Task $task): void {
        $this->tasks[$this->nextId] = $task;
        $this->nextId++;
    }

    public function findById(int $id): ?Task {
        return $this->tasks[$id] ?? null;
    }

    public function findAll(): array {
        return array_values($this->tasks);
    }

    public function findByStatus(TaskStatus $status): array {
        return array_filter($this->tasks, fn($task) => $task->status === $status);
    }

    public function findOverdueTasks(): array {
        return array_filter($this->tasks, fn($task) => $task->isOverdue());
    }
}
