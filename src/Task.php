<?php
namespace App;

class Task {
    public string $title;
    public string $description;
    public TaskStatus $status;
    public string $assignedTo;
    public \DateTime $createdAt;
    public ?\DateTime $dueDate;

    public function __construct(
        string $title, 
        string $description, 
        string $assignedTo = '',
        ?\DateTime $dueDate = null
    ) {
        $this->title = $title;
        $this->description = $description;
        $this->status = TaskStatus::PENDING;
        $this->assignedTo = $assignedTo;
        $this->createdAt = new \DateTime();
        $this->dueDate = $dueDate;
    }

    public function markAsCompleted(): void {
        $this->status = TaskStatus::COMPLETED;
    }

    public function markAsInProgress(): void {
        $this->status = TaskStatus::IN_PROGRESS;
    }

    public function isOverdue(): bool {
        if ($this->dueDate === null) {
            return false;
        }
        return $this->dueDate < new \DateTime() && $this->status !== TaskStatus::COMPLETED;
    }
}