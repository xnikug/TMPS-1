<?php
namespace App;

class TaskService {
    private NotifierInterface $notifier;
    private TaskRepositoryInterface $repository;

    public function __construct(NotifierInterface $notifier, TaskRepositoryInterface $repository) {
        $this->notifier = $notifier;
        $this->repository = $repository;
    }

    public function createTask(
        string $title, 
        string $description, 
        string $assignedTo = '',
        ?\DateTime $dueDate = null
    ): Task {
        $task = new Task($title, $description, $assignedTo, $dueDate);
        $this->repository->save($task);
        
        if (!empty($assignedTo)) {
            $this->notifier->send($task);
        }
        
        return $task;
    }

    public function completeTask(int $taskId): bool {
        $task = $this->repository->findById($taskId);
        if ($task === null) {
            return false;
        }

        $task->markAsCompleted();
        $this->repository->save($task);
        return true;
    }

    public function getTasksByStatus(TaskStatus $status): array {
        return $this->repository->findByStatus($status);
    }

    public function getOverdueTasks(): array {
        return $this->repository->findOverdueTasks();
    }
}