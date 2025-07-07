<?php
namespace App;

class TaskService {
    private NotifierInterface $notifier;

    public function __construct(NotifierInterface $notifier) {
        $this->notifier = $notifier;
    }

    public function createTask(string $title, string $description): Task {
        $task = new Task($title, $description);
        $this->notifier->send($task);
        return $task;
    }
}
