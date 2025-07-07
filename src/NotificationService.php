<?php
namespace App;

// Open/Closed Principle
class NotificationService {
    private array $notifiers = [];

    public function addNotifier(NotifierInterface $notifier): void {
        $this->notifiers[] = $notifier;
    }

    public function notifyAll(Task $task): void {
        foreach ($this->notifiers as $notifier) {
            $notifier->send($task);
        }
    }
}