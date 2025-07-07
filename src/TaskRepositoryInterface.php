<?php

namespace App;

interface TaskRepositoryInterface {
    public function save(Task $task): void;
    public function findById(int $id): ?Task;
    public function findAll(): array;
    public function findByStatus(TaskStatus $status): array;
    public function findOverdueTasks(): array;
}