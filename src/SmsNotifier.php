<?php
namespace App;

class SmsNotifier implements NotifierInterface {
    private string $apiKey;

    public function __construct(string $apiKey) {
        $this->apiKey = $apiKey;
    }

    public function send(Task $task): void {
        echo "SMS sent (API Key: {$this->apiKey}) for task: {$task->title}\n";
        echo "To: {$task->assignedTo}\n";
        echo "Message: New task assigned - {$task->title}\n";
        echo "---\n";
    }
}